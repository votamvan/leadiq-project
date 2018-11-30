#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================================== #
from __future__ import print_function
import multiprocessing
import os
import signal
import subprocess
import sys

cpu_count = 1 # multiprocessing.cpu_count()
model_server_timeout = os.environ.get('MODEL_SERVER_TIMEOUT', 60)
model_server_workers = int(os.environ.get('MODEL_SERVER_WORKERS', cpu_count))

def sigterm_handler(gunicorn_pid):
    try:
        os.kill(gunicorn_pid, signal.SIGTERM)
    except OSError:
        pass

    sys.exit(0)

def start_server():
    gunicorn = subprocess.Popen(['gunicorn',
                                 '--timeout', str(model_server_timeout),
                                 '-k', 'gevent',
                                 '-b', '0.0.0.0:8080',
                                 '-w', str(model_server_workers),
                                 'app:app', '--reload'])

    signal.signal(signal.SIGTERM, lambda a, b: sigterm_handler(gunicorn.pid))

    # If either subprocess exits, so do we.
    pids = set([gunicorn.pid])
    while True:
        pid, _ = os.wait()
        if pid in pids:
            break

    sigterm_handler(gunicorn.pid)
    print('Inference server exiting')

# The main routine just invokes the start function.
if __name__ == '__main__':
    start_server()

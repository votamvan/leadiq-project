#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================================== #
import logging
import json
import falcon
import numpy as np
import tensorflow as tf
from keras.models import load_model
from common import model_file, feature_labels, ErrorMessage

logger = logging.getLogger()
model = load_model(model_file)
model.summary()
graph = tf.get_default_graph()


class HomePage(object):
    def on_post(self, req, resp, **kwargs):
        logger.info("POST %s", req.path)
        try:
            # 1. read data
            request_data = read_request_data(req)
            if "error" in request_data:
                resp.media = request_data
                resp.status = falcon.HTTP_400
                return
            # 2. extract features
            input_data = extract_features(request_data, feature_labels)
            logger.debug("input_data <%s>", input_data)
            if "error" in input_data:
                resp.media = input_data
                resp.status = falcon.HTTP_400
                return
            # 3. predict
            X_test = np.array([input_data])
            global graph
            with graph.as_default():
                Y_pred = model.predict(X_test)
            Y_pred = np.round(Y_pred).astype(int).reshape(1, -1)[0]
            # 4. response
            winner = "False"
            if Y_pred[0] > 0:
                winner = "True"
            resp.media = {
                "winner": winner
            }
        except Exception as err:
            logger.error(err, exc_info=True)
            resp.media = ErrorMessage.INTERNAL_ERROR
            resp.status = falcon.HTTP_500

def read_request_data(req):
    request_data = None
    try:
        body = req.stream.read()
        logger.info("BODY <%s>", body)
        if not body:
            return ErrorMessage.EMPTY_BODY
        request_data = json.loads(body.decode('utf-8'))
    except Exception as err:
        logger.error(err, exc_info=True)
        return ErrorMessage.INVALID_JSON

    return request_data

def extract_features(data_json, labels):
    try:
        ret_data = []
        for label in labels:
            ret_data.append(float(data_json[label]))
        return ret_data
    except Exception as err:
        logger.error(err, exc_info=True)
        return ErrorMessage.INVALID_DATA

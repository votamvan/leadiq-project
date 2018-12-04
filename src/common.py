#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================================== #
import json
import os

base_dir = "/opt/ml"
# data downloaded from https://www.kaggle.com/pravallika30/kaggel-champs#finalproject_training.csv
data_file= os.path.join(base_dir, "input/finalproject_training.csv")
config_file = os.path.join(base_dir, "input/hyperparameters.json")
model_file = os.path.join(base_dir, "model/final_model.h5")
score_file = os.path.join(base_dir, "model/score.json")

# load hyperparameters
with open(config_file, "r") as f:
    config_data = json.load(f)
hidden_layers = config_data.get("hidden_layers" , [7, 1])
epochs = config_data.get("epochs", 100)
dropout = config_data.get("dropout", 0.3)
target_label = "winner"
feature_labels = [
    "item0",
    "item1",
    "item2",
    "item3",
    "item4",
    "item5",
    "item6",
]


class ErrorMessage(object):
    EMPTY_BODY = {
        "error": {
            "code": "EMPTY_BODY",
            "message": "Empty request body"
        }
    }
    INVALID_JSON = {
        "error": {
            "code": "INVALID_JSON",
            "message": "request data is not json format"
        }
    }
    INTERNAL_ERROR = {
        "error": {
            "code": "INTERNAL_ERROR",
            "message": "Internal error"
        }
    }
    INVALID_DATA = {
        "error": {
            "code": "INVALID_DATA",
            "message": "invalid input parameters"
        }
    }

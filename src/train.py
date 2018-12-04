#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================================== #
import json
import numpy as np
import pandas as pd
from keras import models
from keras.layers import Dense, Dropout
from sklearn.cross_validation import train_test_split
from common import data_file, model_file, score_file
from common import feature_labels, target_label, hidden_layers, epochs, dropout

# create deep learning model
def create_model(hidden_layers):
    _model = models.Sequential()
    layers_len = len(hidden_layers)
    for i in range(1, layers_len - 1):
        if i == 1:
            _model.add(Dense(hidden_layers[i], activation='relu', input_dim=hidden_layers[0]))
        else:
            _model.add(Dense(hidden_layers[i], activation='relu'))
        _model.add(Dropout(dropout))

    _model.add(Dense(hidden_layers[-1], activation="sigmoid"))
    _model.compile(optimizer='rmsprop', loss="binary_crossentropy", metrics=['accuracy'])
    return _model

# load dataset
raw_data = pd.read_csv(data_file)

# remove sample with wrong target
raw_data = raw_data.loc[raw_data[target_label].isin(["False", "True"])]
dataset = raw_data[feature_labels + [target_label]]

# map target from string to number
target_map = {"False": 0, "True": 1}
dataset[target_label] = dataset[target_label].map(target_map)

# divide dataset into x(input) and y(output)
X = dataset[feature_labels]
y = dataset[target_label]

# divide dataset into training set, cross validation set, and test set
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train, X_val, Y_train, Y_val = train_test_split(X_train, Y_train, test_size=0.2, random_state=42)

# create model
model = create_model(hidden_layers)

# train model
history = model.fit(np.array(X_train), np.array(Y_train),
                    epochs=epochs,
                    validation_data=(np.array(X_val), np.array(Y_val)),
                    verbose=1)
model.save(model_file)

# save accuracy score
history_dict = history.history
with open(score_file, "w") as f:
    json.dump(history_dict, f)

print("Finish training")
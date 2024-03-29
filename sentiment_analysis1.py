# -*- coding: utf-8 -*-
"""sentiment_analysis1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wPJFnPEZwl1-Va79VD5GH_wxiqynzZ0e
"""

# Commented out IPython magic to ensure Python compatibility.
# %tensorflow_version 2.x

import tensorflow as tf
import tensorflow_datasets as tfds
import tensorflow_hub as hub

train_data, validation_data, test_data = tfds.load(
    name="imdb_reviews", 
    split=('train[:60%]', 'train[60%:]', 'test'),
    as_supervised=True)

type(train_data)

train_examples_batch, train_labels_batch = next(iter(train_data.batch(10)))
train_examples_batch

train_labels_batch

pretrained_model = "https://tfhub.dev/google/tf2-preview/gnews-swivel-20dim/1"
hub_layer = hub.KerasLayer(pretrained_model, input_shape=[], dtype=tf.string, trainable=True)

hub_layer(train_examples_batch[:2])

train_examples_batch[:2]

model = tf.keras.Sequential()
model.add(hub_layer)
model.add(tf.keras.layers.Dense(16,activation="relu"))
model.add(tf.keras.layers.Dense(1,activation="sigmoid"))
model.summary()

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

model.fit(train_data.shuffle(10000).batch(512),
         epochs=20,
         validation_data=validation_data.batch(512),
         verbose=1)

model.predict(["This is the worst movie I have ever seen",
              "An excellent movie that I enjoyed a lot",
              "how can one make such a horrible movie? there is no story, acting direction everything is very poor"])

model.predict(["An excellent movie that I enjoyed a lot"])
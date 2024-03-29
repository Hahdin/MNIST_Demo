# -*- coding: utf-8 -*-
"""MNIST Example.ipynb
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/
"""
import numpy as np
#MNIST
# Import tensorflow
import tensorflow as tf
# Import tensorflow's MNIST data handle
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

# show some information
type(mnist)
mnist.train.images.shape 
mnist.train.num_examples

import matplotlib.pyplot as plt
# %matplotlib inline  # uncomment this when using Jupyter Notebook

# the original 784 pixels in a vector
mnist.train.images[1].shape
plt.imshow(mnist.train.images[783].reshape(784,1), cmap='inferno', aspect=0.02)

# reshaped to 28 X 28 to match the input area
mnist.train.labels[783]
plt.imshow(mnist.train.images[783].reshape(28,28), cmap='inferno', aspect=1)

x = tf.placeholder(dtype=tf.float32, shape=[None, 784])# will send X amounts in 784X1
W = tf.Variable(tf.zeros(shape=[784, 10]))# Weights - 10 possible labels (numbers)
b = tf.Variable(tf.zeros(shape=[10]))# bias

# x * W + b
y = tf.matmul(x,W) + b

# true labels
y_true = tf.placeholder(tf.float32, shape=[None, 10]) 

# cross entropy
x_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=y_true, logits=y))

# gradient descent optimizer
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.5)# lower takes longer, but is more accurate

# train the model
train = optimizer.minimize(x_entropy)
init = tf.global_variables_initializer()

#run the model on our data, collect and print the results
with tf.Session() as sess:
  sess.run(init)
  for step in range(1000):
    batch_x, batch_y = mnist.train.next_batch(100)
    sess.run(train, feed_dict={x: batch_x, y_true: batch_y})
  matches = tf.equal(tf.argmax(y,1), tf.argmax(y_true, 1))
  acc = tf.reduce_mean(tf.cast(matches, tf.float32))
  print(sess.run(acc, feed_dict={x:mnist.test.images, y_true: mnist.test.labels}))


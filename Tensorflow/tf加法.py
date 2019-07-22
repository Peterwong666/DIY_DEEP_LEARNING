

from __future__ import print_function

import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

g = tf.Graph()

with g.as_default():
  x = tf.constant(8, name="x_const")
  y = tf.constant(5, name="y_const")
  z = tf.constant(4, name="z_const")
  sum = tf.add(x,y,z,name="x_y_sum")

  with tf.Session() as sess:
    print(sum.eval())
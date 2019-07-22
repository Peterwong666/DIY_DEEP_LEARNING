from __future__ import print_function

import tensorflow as tf
try:
	tf.contrib.eager.enable_eager_execution()
	print("TF import with eager execution!")

except ValueError:
	print("TF already imported with eager execution!")

import tensorflow as tf
W = tf.Variable(tf.zeros([1, 3]), dtype=tf.float32, name="W")
B = tf.constant([[1, 2, 3]], dtype=tf.float32, name="B")
act = tf.add(W, B)
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    sess.run(act)
    writer = tf.summary.FileWriter("./graphs", sess.graph)
writer.close()

#Access tensorboard by running this command in the pwd: tensorboard --logdir=graphs

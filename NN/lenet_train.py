# -*- coding: utf-8 -*-
import os
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import lenet_inference

batch_size = 100
learning_rate_base = 0.8
learning_rate_decay = 0.99
regularization_rate = 0.0001
training_steps = 30000
moving_average_decay = 0.99

model_save_path = "./model/"
model_name = "model.ckpt"

def train(mnist):
    x = tf.placeholder(
        tf.float32, [
        None,
        lenet_inference.image_size,
        lenet_inference.image_size,
        lenet_inference.num_channels], name='x-input')

    y_ = tf.placeholder(
        tf.float32, [None, mnist_inference.output_node], name='y-input')

    regularizer = tf.contrib.layers.l2_regularizer(regularization_rate)
    y = mnist_inference(x, regularizer)

    global_step = tf.Variable(0, trainable=False)

    variable_averages = tf.train.ExponentialMovingAverage(
        moving_average_decay, global_step)
    variable_averages_op = variable_averages.apply(
        tf.trainable_variables())

    cross_entropy = tf.nn.softmax_cross_entropy_with_logits(y, y_)
    cross_entropy_mean = tf.reduce_mean(cross_entropy)

    loss = cross_entropy_mean + tf.add_n(tf.get_collection("losses"))
    learing_rate = tf.train.exponential_decay(
        learing_rate_base,
        global_step,
        mnist.train.num_examples / batch_size,
        learning_rate_decay)

    train = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss,
        global_step=globa_step)
    train_op = tf.group(train, variable_averages_op)

    saver = tf.train.Saver()
    init_op = tf.initialize_all_variables()

    with tf.Session() as sess:
        sess.run(init_op)

        for i in range(training_steps):
            xs, ys = mnist.train.next_batch(batch_size)
            reshaped_xs = np.reshape(xs, (
                  batch_size,
                  lenet_inference.image_size,
                  lenet_inference.image_size,
                  lenet_inference.num_channels))

            _, loss_value, step = sess.run([train_op, loss, global_step],
                feed_dict={x: reshaped_xs, y_:ys})

            if i % 1000 == 0:
                print("after {} steps, loss is {}".format(step, loss_value))
                saver.save(
                    sess, os.path.join(model_save_path, model_name),
                    global_step=tep)

def main(argv=None):
    mnist = input_data.read_data_sets("./mnist_data", one_hot=True)
    train(mnist)

if __name__ == "__main__":
    tf.app.run()

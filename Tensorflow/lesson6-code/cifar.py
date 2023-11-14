#!/usr/bin/python
# -*- coding:utf8 -*-

import tensorflow as tf
import os
import cPickle
import numpy as np
FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_string("ckp_dir", '', 'where to save tensorboard')
tf.app.flags.DEFINE_string('cifar_dir', '', 'dir to store cifar py data')

class CifarData:
    def __init__(self, data_dir):
        self.train_data_fns = [os.path.join(data_dir, 'data_batch_%d' % (i)) for i in range(1, 6)]
        self.test_data_fn = os.path.join(data_dir, 'test_batch')
        self.current_pos = 0

    def load(self):
        train_data_arr = []
        train_label_arr = []
        for fn in self.train_data_fns:
            with open(fn, 'rb') as f:
                train_data_dict = cPickle.load(f)
                train_data_arr.append(train_data_dict['data'])
                train_label_arr.append(train_data_dict['labels'])
        with open(self.test_data_fn, 'rb') as f:
            test_data_dict = cPickle.load(f)
            test_data = test_data_dict['data']
            test_label = test_data_dict['labels']
            test_label = np.array(test_label)
        train_data = np.vstack(train_data_arr)
        train_label = np.hstack(train_label_arr)
        train_label_one_hot = self.one_hot(train_label)
        test_label_one_hot  = self.one_hot(test_label)
        self.origin_train_data = train_data
        self.origin_train_label = train_label_one_hot
        self.test_data = test_data
        self.test_label = test_label_one_hot
        self.num_train_examples = self.origin_train_data.shape[0]
        
        p = np.random.permutation(len(self.origin_train_data))
        self.train_data = self.origin_train_data[p]
        self.train_label = self.origin_train_label[p]

    def one_hot(self, label):
        num_label = len(label)
        one_hot_label = np.zeros((num_label, 10))
        for i in range(num_label):
            one_hot_label[i][label[i]] = 1
        return one_hot_label

    def next_batch(self, batch_size):
        if batch_size > self.num_train_examples:
            raise Exception("batch_size is bigger than train example num")
        if self.current_pos + batch_size >= self.num_train_examples:
            assert len(self.train_data) == len(self.train_label)
            p = np.random.permutation(len(self.train_data))
            self.train_data = self.train_data[p]
            self.train_label = self.train_label[p]
            self.current_pos = 0
        result_data = self.train_data[self.current_pos: self.current_pos+batch_size]
        result_label = self.train_label[self.current_pos: self.current_pos + batch_size]
        self.current_pos += batch_size
        return result_data, result_label

        
def variable_summaries(var):
    with tf.name_scope('summaries'):
        mean = tf.reduce_mean(var)
        with tf.name_scope('stddev'):
            stddev = tf.sqrt(tf.reduce_mean(tf.square(var - mean)))
        tf.summary.scalar('mean', mean)
        tf.summary.scalar('stddev', stddev)
        tf.summary.scalar('min', tf.reduce_min(var))
        tf.summary.scalar('max', tf.reduce_max(var))
        tf.summary.histogram('histogram', var)

def feature_map_summary(conv, dim, name):
    conv_channels = tf.split(conv, num_or_size_splits=dim, axis=3)
    with tf.name_scope(name):
        len_channel = len(conv_channels)
        for i in range(len_channel):
            tf.summary.image('channel-%d' % (i), conv_channels[i], max_outputs=1)


def conv2d(x, output_dim, k_h=5, k_w=5, s_h=1, s_w=1, stddev=0.02, name="conv2d"):
    with tf.variable_scope(name):
        w = tf.get_variable('w', [k_h, k_w, x.get_shape()[-1], output_dim],
                initializer = tf.contrib.keras.initializers.glorot_normal())
        conv = tf.nn.conv2d(x, w, strides=[1, s_h, s_w, 1], padding="SAME")
        biases = tf.get_variable('biases', [output_dim],
                initializer = tf.constant_initializer(0.0))
        conv = conv + biases
        '''
        with tf.name_scope('w'):
            variable_summaries(w)
        with tf.name_scope('biases'):
            variable_summaries(biases)
        with tf.name_scope('conv'):
            variable_summaries(conv)
        '''
        return conv

def max_pool_2d(x, k_h=2, k_w=2, s_h=2, s_w=2, name="max_pool"):
    with tf.name_scope(name):
        result = tf.nn.max_pool(
                x,
                ksize=[1, k_h, k_w, 1],
                strides=[1, s_h, s_w, 1],
                padding="SAME",
                name='pool')
        # variable_summaries(result)
        return result

def dense(x, output_dim, stddev=0.02, name="dense"):
    with tf.variable_scope(name):
        w = tf.get_variable('w', [x.get_shape()[-1], output_dim],
                initializer = tf.contrib.keras.initializers.glorot_normal())
        biases = tf.get_variable('biases', [output_dim],
                initializer = tf.constant_initializer(0.0))
        result = tf.matmul(x, w) + biases
        # variable_summaries(w)
        # variable_summaries(biases)
        # variable_summaries(result)
        return result

def lrelu(x, name="lrelu"):
    with tf.name_scope(name):
        result = tf.maximum(x, 0.2 * x)
        # variable_summaries(result)
        return result

cifar_data = CifarData(FLAGS.cifar_dir)
cifar_data.load()

with tf.name_scope("input_x"):
    x = tf.placeholder(tf.float32, [None, 3072])
    x_image = tf.reshape(x, [-1, 3, 32, 32])
    x_image = tf.transpose(x_image, perm=[0, 2, 3, 1])
conv1 = lrelu(conv2d(x_image, 32, name="conv1"), name='lrelu1')
# feature_map_summary(conv1, 32, "conv1_feature_map")
pool1 = max_pool_2d(conv1, name="pool1")
conv2 = lrelu(conv2d(pool1, 64, name="conv2"), name='lrelu2')
# feature_map_summary(conv2, 64, "conv2_feature_map")
pool2 = max_pool_2d(conv2, name="pool2")
with tf.name_scope("flatten"):
    pool2_flatten = tf.reshape(pool2, [-1, 8*8*64])
fc1 = lrelu(dense(pool2_flatten, 1024, name="fc1"), name='lrelu3')
dropout_fc1 = tf.nn.dropout(fc1, 0.5)
logits = dense(dropout_fc1, 10, name="fc2")

with tf.name_scope("input_y"):
    y_ = tf.placeholder(tf.float32, [None, 10])
with tf.name_scope("metrics"):
    cross_entropy = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=logits, labels=y_))
    correct_prediction = tf.equal(tf.argmax(logits,1), tf.argmax(y_,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
cross_entropy_summary = tf.summary.scalar('cross_entropy', cross_entropy)
accuracy_summary = tf.summary.scalar('accuracy', accuracy)
tf.summary.image("input_image", x_image)
merged_summary = tf.summary.merge_all()
merged_summary_test = tf.summary.merge([cross_entropy_summary, accuracy_summary])
with tf.name_scope("train_op"):
    train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    if not os.path.exists(FLAGS.ckp_dir):
        os.mkdir(FLAGS.ckp_dir)
    train_log_dir = os.path.join(FLAGS.ckp_dir, "train")
    test_log_dir  = os.path.join(FLAGS.ckp_dir, "test")
    if not os.path.exists(train_log_dir):
        os.mkdir(train_log_dir)
    if not os.path.exists(test_log_dir):
        os.mkdir(test_log_dir)
    train_writer = tf.summary.FileWriter(train_log_dir, sess.graph)
    test_writer  = tf.summary.FileWriter(test_log_dir)
    sess.run(init)
    for i in range(5000):
        batch_xs, batch_ys = cifar_data.next_batch(20)
        cross_entropy_val, _, summary_str = sess.run(
                [cross_entropy, train_step, merged_summary],
                feed_dict={x: batch_xs, y_: batch_ys})
        print '[Train] Epoch %4d: cross_entropy: %4.8f' % (i, cross_entropy_val)
        if (i+1) % 100 == 0:
            accuracy_val, summary_str = sess.run(
                    [accuracy, merged_summary],
                    feed_dict={x: cifar_data.origin_train_data[0:200], y_: cifar_data.origin_train_label[0:200]})
            train_writer.add_summary(summary_str, i)
            print "[Train] Epoch %4d: accuracy: %4.8f" % (i, accuracy_val)
        if (i+1) % 100 == 0:
            accuracy_val, summary_str = sess.run(
                    [accuracy, merged_summary_test],
                    feed_dict={x: cifar_data.test_data[0:200], y_: cifar_data.test_label[0:200]})
            test_writer.add_summary(summary_str, i)
            print "[Test]  Epoch %4d: accuracy: %4.8f" % (i, accuracy_val)

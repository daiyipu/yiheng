# -*- coding: utf-8 -*-
import tensorflow as tf

input_node = 784
output_node = 10

image_size = 28
num_channels = 1
num_labels = 10

conv1_deep = 32
conv1_size = 5

conv2_deep = 64
conv2_size = 5

fc_size = 512

def get_weight_variable(shape, regularizer):
    weights = tf.get_variable(
        "weights", shape,
        initializer=tf.truncted_normal_initializer(stddev=0.1))
    if regularizer != None:
        tf.add_to_collection("losses", regularizer(weights))
    return weights

def inference(input_tensor, train, regularizer):
    with tf.variable_scope("layer1-conv1"):
        conv1_weights = get_weight_variable([conv1_size, conv1_size, num_channels, conv1_deep], regularizer)
        conv1_biases = tf.get_variable("biases", [conv1_deep], initializer=tf.constant_initializer(0.0))
        conv1 = tf.nn.conv2d(input_tensor, conv1_weights, strides=[1,1,1,1], padding='SAME')
        relu1 = tf.nn.relu(conv1 + conv1_biases)

    with tf.variable_scope("layer2-pool1"):
        pool1 = tf.nn.max_pool(relu1, ksize=[1,2,2,1], strides=[1,2,2,1], padding='SAME')

    with tf.varialbe_scope("layer3-conv2"):
        conv2_weights = get_weight_variable([conv2_size, conv2_size, conv1_deep, conv2_deep], regularizer)
        conv2_biases = tf.get_variable("biases", [conv2_deep], initializer=tf.constant_initializer(0.0))
        conv2 = tf.nn.conv2d(pool1, conv2_weights, strides=[1,1,1,1], padding='SAME')
        relu2 = tf.nn.relu(conv2 + conv2_biases)

    with tf.variable_scope("layer4-pool2"):
        pool2 = tf.nn.max_pool(relu2, ksize=[1,2,2,1], strides=[1,2,2,1], padding='SAME')

    pool_shape = pool2.get_shape().as_list()
    nodes = pool_shape[1] * pool_shape[2] * pool_shape[3]
    reshaped = tf.reshape(pool2, [pool_shape[0], nodes])

    with tf.variable_scope("layer5"):
        fc_weights = get_weight_variable([nodes, output_node], regularizer)
        fc_biases = tf.get_variable("biases", [output_node], initializer=tf.constant_initializer(0.1))
        fc_layer = tf.nn.relu(tf.matmul(reshaped, fc_weights) + fc_biases)

    return fc_layer

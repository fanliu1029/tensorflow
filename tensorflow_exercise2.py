# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 09:31:12 2017

@author: 15696
"""
import tensorflow as tf 
W=tf.Variable(tf.random_normal([1]),name="Weight")
b=tf.Variable(tf.random_normal([1]),name="bias")
X=tf.placeholder(tf.float32,shape=[None])
Y=tf.placeholder(tf.float32,shape=[None])
htpothesis=X*W+b
cost=tf.reduce_mean(tf.square(hypothesis))
optimizer=tf.train.GradientDescentOptimizer(learning_rate=0.01)
train=optimizer.minimize(cost)
sess=tf.Session()
sess.run(tf.global_variables_initializer())
for step in range(2001):
    cost_val,W_val,b_val,_=sess.run([cost,W,b,train],feed_dict={X:[1,2,3,5,6],Y:[2.1,3.1,4.1,5.1,6.1]})
    if step%20==0:
        print(step,cost_val,W_val,b_val)
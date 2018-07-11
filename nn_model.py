
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 09:40:23 2018

@author: xxiu
"""

import numpy as np
import helper
import tensorflow as tf


header = ['course', 'school', 'sex', 'age','address', 'famsize', 'Pstatus', 'Medu', 'Fedu', 'Mjob', 'Fjob', 'reason', 'guardian', 'traveltime', 'studytime', 'failures', 'schoolsup', 'famsup', 'paid', 'activities', 'higher', 'internet', 'romantic', 'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health', 'absences', 'G1', 'G2', 'G3']

df = helper.adding_header('data.csv',header)

df = helper.handle_non_numerical_data(df)

print(df.head())

#neural networks 
n_nodes_hl1 = 13
n_nodes_hl2 = 27

n_classes = 1
batch_size =10

x =tf.placeholder('float',shape = (None,32))
y =tf.placeholder('float')

y_train = np.array(df['G3'])
df = df.drop(columns =['G3'],axis =1)
X_train= np.array(df)
print(X_train)


def neural_network_model(data):
    
    hidden_1_layer = {'weights':tf.Variable(tf.random_normal([32,n_nodes_hl1])),
                      'biases':tf.Variable(tf.random_normal([n_nodes_hl1]))}
    
    hidden_2_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl1,n_nodes_hl2])),
                      'biases':tf.Variable(tf.random_normal([n_nodes_hl2]))}
    
    output_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl2,n_classes])),
                    'biases':tf.Variable(tf.random_normal([n_classes]))}
   
    l1 = tf.add(tf.matmul(data,hidden_1_layer['weights']), hidden_1_layer['biases'])
    
    l1 = tf.nn.sigmoid(l1)
    
    l2 = tf.add(tf.matmul(l1,hidden_2_layer['weights']), hidden_2_layer['biases'])
   
    l2 = tf.nn.sigmoid(l2)
    
    output = tf.add(tf.matmul(l2,output_layer['weights']), output_layer['biases'])
  

    print('------------------------------------------s')
   
    return output

def train_neural_network(x):
    #rememer the output is onehot array
    prediction = neural_network_model(x)    
    
   
    cost = tf.reduce_mean(tf.square(prediction-y))
    #optimizer = tf.train.GradientDescentOptimizer(0.00001).minimize(cost)
    optimizer = tf.train.AdamOptimizer(learning_rate=0.001).minimize(cost)
     
    hm_epochs = 10
    
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        
        for epoch in range(hm_epochs):
            
            epoch_loss = 0
            
            for row in range(int(len(X_train))):
                
                     
                    _, c = sess.run([optimizer, cost], feed_dict = {x:X_train[row][:].reshape(1,32),y:y_train[row]})
                    #print('act',y_train[row])
                    
            epoch_loss += c
              
            
            print('Epoch', epoch,'completed out of',hm_epochs,'loss',epoch_loss)
              
     
        correct = tf.equal(tf.argmax(prediction,1),y_train)
       
        accuracy = tf.reduce_mean(tf.cast(correct,'float'))
        print("accuracy  ", accuracy.eval({x:X_train,y:y_train}))
        
        
        
        

train_neural_network(x)


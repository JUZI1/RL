import tensorflow as tf
example_id=1
inputs=[0,2,2,4,6,3,2,4,2,3,7]
hiddens=[0,20,20,40,50,30,20,50,20,30,50]
outputs=[0,1,1,1,2,1,1,2,1,1,1]
a_bound=[0,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3]
input=tf.zeros((1,inputs[example_id]),dtype=tf.float32)
h = tf.layers.dense(input, hiddens[example_id], activation=tf.nn.relu,trainable=False,name='w1')
a = tf.layers.dense(h, outputs[example_id], activation=tf.nn.tanh,trainable=False,name='w2')
action=tf.multiply(a, a_bound[example_id])
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    saver = tf.compat.v1.train.Saver()
    saver.restore(sess, 'save/ddpg/ex3/model')
    variables=tf.get_collection(tf.GraphKeys.GLOBAL_VARIABLES, )
    for v in variables:
        w = sess.run(v)
        print(v.name)
        print(w)
        print('-----------------------------------------------------------------------')

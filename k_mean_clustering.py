
# coding: utf-8

# In[66]:


import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
import sklearn.model_selection as sk


# In[67]:


spring_csv = "/home/liujinzhao/anaconda3/output.csv"


# In[68]:


datasets = np.loadtxt(fname=spring_csv,delimiter=',')


# In[69]:


datasets = tf.convert_to_tensor(datasets)
N = datasets.shape[0].value
K = 10
Max_iter = 1000


# In[70]:


cluster_assignments = tf.Variable(tf.zeros([N],dtype=tf.int64))
#have to change here
centroids = tf.random_crop(datasets,[10,50])#
#changed to under,you have to understand the meaning of Variable.
centroids = tf.Variable(tf.slice(datasets,[0,0],[K,50]))
centroids = tf.Variable(tf.slice(tf.random_shuffle(datasets),[0,0],[K,50]))


# In[71]:


rep_centroids = tf.reshape(tf.tile(centroids,[N,1]),[N,K,50])
rep_points = tf.reshape(tf.tile(datasets,[1,K]),[N,K,50])
sum_squares = tf.reduce_sum(tf.square(rep_points - rep_centroids),reduction_indices=2)


# In[72]:


best_centroids = tf.argmin(sum_squares,1)
did_assignment_changed = tf.reduce_any(tf.not_equal(best_centroids,cluster_assignments))


# In[73]:


def bucket_mean(data, bucket_ids, num_buckets):
    total = tf.unsorted_segment_sum(data,bucket_ids,num_buckets)
    count = tf.unsorted_segment_sum(tf.ones_like(data),bucket_ids,num_buckets)
    
    return total / count


# In[74]:


#
means = bucket_mean(datasets,best_centroids,K)


# In[75]:


with tf.control_dependencies([did_assignment_changed]):
    do_updates = tf.group(centroids.assign(means),cluster_assignments.assign(best_centroids))


# In[76]:


init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)


# In[77]:


changed = True
iter = 0


# In[78]:


while changed and iter < Max_iter:
    iter+=1
    [changed,_] = sess.run([did_assignment_changed,do_updates])
    print(iter)
    


# In[79]:


[centers,assignment] = sess.run([centroids,cluster_assignments])


# In[80]:


print("Centroids:")
print (centers)
print ("Cluster assignments:", assignment)


# In[81]:


#tf.contrib.learn.KMeansClustering(num_clusters=10,initial_clusters=,distance_metric=,use_mini_batch=True,mini_batch_steps_per_iteration=1,kmeans_plus_plus_num_retries=2)


# In[ ]:





# In[ ]:





# In[ ]:





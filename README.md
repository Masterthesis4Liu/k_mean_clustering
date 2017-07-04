# k_mean_clustering
output.csv is the stiffness of springs, each raw is a model, from model1 to model586
using a k_mean_clustering method
the stiffness of 50 springs in 586 models

when you guys have any idea or think the algorithm not good.
Just write down in this README.md file.

thanks a lot.


%%Matlab code.
The 3 .jpg 'k_mean_clustering_plus.jpg', 'k_mean_clustering_sample.jpg', 'k_mean_clustering_uniform.jpg' show the result of using 3 different methods for choosing initial cluster centroid positions(or seeds).

'plus(default)':Select k seeds by implementing the k-means++ algorithm for cluster center initialization.
'sample': Select k observations from X at random.
'uniform': Select k points uniformly at random from the range of X. Not valid with the Hamming distance.

As we can see, the method of choosing initial cluster centroids has big influence on the result. But we cannot judge the performence of
each method.

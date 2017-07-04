clear;
clc;
%idx = kmeans(X,k) performs k-means clustering to partition the observations of the n-by-p data matrix X into k clusters, 
%and returns an n-by-1 vector (idx) containing cluster indices of each observation. Rows of X correspond to points and columns
%correspond to variables.
%By default, kmeans uses the squared Euclidean distance measure and the k-means++ algorithm for cluster center initialization.
data = csvread('output_without_y.csv');

%parallel computing,need permission.
% pool = parpool;
% stream = Randstream('mlfg6331_64');
% options = statset('UseParallel',1,'UseSubstreams',1,...
%     'Streams',stream);
%add 'Options',options in kmeans function.


%Determine the correct number of clusters.
%From cluster 3 to cluster 10.

list_average_silhouette = [];
for i=3:30
    %decide the Distance algorithm and the Replicates.
    idx = kmeans(data,i,'Distance','correlation','Start','uniform','MaxIter',10000,'Display','iter','Replicates',50);
    figure(i);
    [silh,h] = silhouette(data,idx,'correlation');
    h = gca;
    h.Children.EdgeColor = [0.8 0.8 1];
    xlabel('Silhouette Value');
    ylabel('Cluster')   
    mean_silh = mean(silh);
    fprintf('The average silhouette of Cluster%d is:%d\n',i,mean_silh);
    list_average_silhouette(end+1) = mean_silh;
end
disp(list_average_silhouette');
plot(3:30,list_average_silhouette,'b--o');
xlabel('Number of clusters');
ylabel('Average silhouette of Cluster');


%Distance measure, in p-dimensional space, used for minimization, specified as the comma-separated pair consisting of 
%'Distance' and 'sqeuclidean'(Squared Euclidean distance as default), 'cityblock', 'cosine', 'correlation', or 'hamming'.
%C:centroid locations k-by-p matrix C.
%D:Disrance from each point to every centroid in the n-by-k matrix.
%sumd:the within-cluster sums od point-to-centroid distances in the k-by-1
%vector
tic,
[idc,C,sumd,D] = kmeans(data,3,'Distance','correlation','Start','sample','MaxIter',10000,'Replicates',50,'Display','final');
toc,
% figure(1);
% hold on;
% plot3(test_data(:,1),test_data(:,2),test_data(:,3),'r.');
% plot3(C(:,1),C(:,2),C(:,3),'kx');
% bar(idc);
% hold off;
% plot(1:586,idc,'r.');
% xlabel('Model index');
% ylabel('Group index');

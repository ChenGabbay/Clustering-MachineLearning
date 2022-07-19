# Clustering-MachineLearning

This project use <strong>k-means clustering algorithm</strong> as an image compression algorithm.

![image](https://user-images.githubusercontent.com/105008868/179601584-eedd0d9f-6768-45d4-b263-a21cdb650400.png)

We use the image above and transform her to be represented with a small subset of colors.

For this process we perform unsupervised learning using K means and K means++ clustering algorithms 




## K means algorithm:
We randomly select centroids.
Than we use the Minkowski distance function that will help us to measure the distances between each point in the RGB space to the centroids.
Each point belongs to the centroid that is most close to her.
We calculate the average of the data points to each centroid and define the new centroids

repeat this steps until there is no change in the centroids.

## K means++ :
Same as k means except for the initialization.
Instead of randomly selecting centroids, we choose a random point from the data to be the first centroid.
We define probabilities - a distance of data point from centroid divided by the total distances of all the data points.

Then choosing by probability the next centroids. 
repeat until we reach k centroids.



<strong>*In the end, we display a graph comparing the results of Kmeans with the improved Kmeans++*</strong>

![image](https://user-images.githubusercontent.com/105008868/179603400-49f17e66-5768-4a71-8ac3-da07d7ee7733.png)


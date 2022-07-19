# Clustering-MachineLearning

This project used <strong>k-means clustering algorithm</strong> as an image compression algorithm.

![image](https://user-images.githubusercontent.com/105008868/179601584-eedd0d9f-6768-45d4-b263-a21cdb650400.png)

We used the image above and compressed it to be represented with a small subset of colors.

The compressing was implemented by using K means and K means++ clustering algorithms 




## K means algorithm:
Centroids were randomly selected.
We used the Minkowski distance function for measuring the distances between each point in the RGB space to the appropriate centroid.
Each point belongs to the centroid that is most close to her.
For each centroid, We calculated the average of its data points to be the new centroid

This steps has being repeated until there is no change in the centroids.

## K means++ :
Same as k means except for the initialization.
Instead of randomly selecting centroids, we chose a random point from the data to be the first centroid.
We defined the probabilities by measuring the distance of data points from the centroid and divided by the total distances of all the data points.

The next centroid was calculated using the calculated probabilities. 
This steps has being repeated until we reach k centroids.



<strong>*Finally, we display a graph which describe the comparision between Kmeans and the improved Kmeans++*</strong>

![image](https://user-images.githubusercontent.com/105008868/179603400-49f17e66-5768-4a71-8ac3-da07d7ee7733.png)


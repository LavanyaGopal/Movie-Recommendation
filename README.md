# Movie-Recommendation

This project is done as part of my college course assignment. Below is the details of the results, the dataset details are attached in the Dataset Readme file.

#####################################################################################

The py file contains the code for second assignment first question. 

Note: keep the datasets to be run in the same directory where the program exists.


The functionality achieved in the code:::

1. Run the py file in any py file.
2. loaded the data and found the list of the movies which are seen  by the user_a.
3. Collected the user_i who have rated the same movies as the user_a
4. Took the list of user_i and selected the users who have rated more movies (top 25)
5. Found the list of users who have rated the movie that we are about to predict 

The ipynb file for second question knn classifier can be run in jypiter.

The paramters tried and their respective accuracy and error is present in the code file. 
 Parameter : n_neighbors 
 value  accuracy  error
 3      0.9705    2.949999999999997
 5      0.9688    3.1200000000000006
 10     0.9665    3.3499999999999974
 25     0.9609    3.9100000000000024
 1      0.9691    3.090000000000004


The parameter weights = 'distance' and 'uniform' both have same effect on the acuuracy.
The algo parameter takes more computational time.

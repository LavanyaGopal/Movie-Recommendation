import numpy
import numpy as np
import pandas as pd
from heapq import nlargest
import prun as prun

# taking the input form the file and storing it in the dataframe

file_name = "C:/Users/glava/UTD/Sem1/ML/HW2-Oct11-Mon-due/netflix2/TrainingRatings.txt"
colnames = ["userid","movieid","rating"]
train_dataframe = pd.read_csv(file_name,names=colnames, header=None, dtype={'userid': 'str', 'movieid': 'str','rating':'float'})
print("***************************** train_dataframe.head()", train_dataframe.head())

print("***************************** train_dataframe.count()", train_dataframe.count())


user_a = input("Enter the userid ")
movie_a = input("Enter the movie id to be predicted for rating ")


# get the set of movies on which the user_i has given the rating


#user_a_data = train_dataframe.loc[train_dataframe['userid'] == user_a ]
#print(user_a_data)

# Give me windspeed and event in dataframe where my temperature >= 32
#df[['windspeed','event']][df.temperature >= 32]

user_a_data = train_dataframe[['userid','movieid','rating']][train_dataframe.userid == user_a]
print("***************************** user_a_data::: " ,user_a_data)

user_a_movies = user_a_data[['movieid']]
print("***************************** user_a_movies", user_a_movies)

user_a_data['rating'] = user_a_data['rating'].astype(float)

# mean vote for user i
sum_a = user_a_data["rating"].sum()
print("***************************** sum_a", sum_a)
total_ratedMovies_a = user_a_data['movieid'].count()
print("***************************** total_ratedMovies_a", total_ratedMovies_a)

mean_vote_a = sum_a/total_ratedMovies_a
print("*****************************mean vote of active user is : ",mean_vote_a)

#total_movies_rated_a = user_a_movies['movieid'].count
#print(total_movies_rated_a)
#sum_vote_a = user_a_data[user_a_data['rating'].sum()]

# saving few rows of data in this var
RT_train_df = train_dataframe.head(10000)
print("***************************** RT_train_df", RT_train_df)

#%%prun
matching_123 = pd.DataFrame(columns = colnames)
for (columnName, columnData) in user_a_data.iteritems():
    if columnName == "movieid" :
        for movie in columnData :
            for movie_all in RT_train_df.movieid:
                #print("movie_all: ", movie_all, "movie : ",movie)
                if movie_all == movie:
                    #print("============================movie_all: ", movie_all, "movie : ",movie)
                    entry = RT_train_df.loc[RT_train_df['movieid']== movie_all]
                    matching_123 = matching_123.append([entry])
                    #print("**********************",matching_123)

matching_456 = matching_123[matching_123.userid != user_a]
print("***************************** matching_456::: ", matching_456)




# df with users who have rated the movie that we want to predict
movie_a_allusercommon = pd.DataFrame(columns = colnames)
entry2 = RT_train_df.loc[RT_train_df['movieid']== '1148143']
movie_a_allusercommon = movie_a_allusercommon.append([entry2])
print("***************************** entry2 :: ", entry2)
print("***************************** movie_a_allusercommon:: ", movie_a_allusercommon)
print(" ***************************** movie_a_allusercommon.count()",movie_a_allusercommon.count())



#%%prun
print(type(matching_456))
print(matching_456.count())
print(len(pd.unique(matching_456['userid'])))
print(matching_456['userid'].value_counts().to_dict())
print(matching_456['userid'].value_counts().to_dict())
corres_users = matching_456['userid'].value_counts().to_dict()
print("***************************** type(corres_users)", type(corres_users))
#corres_users1 = corres_users.head()
#print(corres_users1)

# get N= 25 users with largest movies rated in common to active user
N = 25
n_commonUsers_list = nlargest(N, corres_users, key = corres_users.get)
print("***************************** n_commonUsers_list", n_commonUsers_list)

vi = pd.DataFrame(columns = colnames)
print(type(vi))
for user_i in n_commonUsers_list:
    for (columnName, columnData) in user_a_data.iteritems():
        if columnName == "movieid" :
            for movie in columnData :
                for user_i in matching_456.userid:
                    entry3 =  matching_456[matching_456['movieid'] ==movie]
                    vi.append([entry3])
#vi.append[RT_train_df[RT_train_df['userid'] == user_i and RT_train_df[RT_train_df['movieid']== movie]]]
print("***************************** vi", vi)

print("*****************************  user_a_daat",user_a_data)


# pandas count distinct values in column
matching_456['userid'].value_counts()
unique_movies_a = pd.unique(matching_456['movieid'])
print("***************************** unique_movies_a", unique_movies_a)
print("***************************** type(unique_movies_a", type(unique_movies_a))

# count of unique movies for user a
print("***************************** np.count_nonzero", np.count_nonzero(unique_movies_a,axis= 0))


#%%prun
print("***************************** matching_456.head()", matching_456.head())

# mean vote for user i
sum_i = matching_456['rating'].sum()
print("sum:: ", sum_i)
total_ratedMovies_i = matching_456['movieid'].count()
print("total : ", total_ratedMovies_i)

mean_vote_i = numpy.true_divide(sum_i,total_ratedMovies_i)
print("mean vote of ith user is : ",mean_vote_i)
#print(matching_456.groupby(['userid']))


matching_456.describe(include=object)

numpy_array = train_dataframe.to_numpy()


print("***************************** numpy_array", numpy_array)
print("***************************** numpy_array.size", numpy_array.size)


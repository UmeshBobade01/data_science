#-----------------------------Entertainment Recommendation system------
"""
business objective:
    Maximize: Maximize the acuuracy of model.
             - Maximize Sales Revenue
    Minimize: Minimize the Prediction Errors.
    
    constraints: Sales Revenue,Scalability etc.
"""


#import lib
import pandas as pd

#EDA

df = pd.read_csv("Entertainment.csv")

df.head()

df.dtypes
"""Out[93]: 
Id            int64
Titles       object
Category     object
Reviews     float64
dtype: object"""

df.shape
# you will get 51 record and 4 columns.

df.info()
#it has 0 not null values

df.isnull().sum()
"""
Out[98]: 
Id          0
Titles      0
Category    0
Reviews     0
dtype: int64"""

df.columns
#Out[95]: Index(['Id', 'Titles', 'Category', 'Reviews'], dtype='object')

df.Category
#it has  Action, Comedy, School, Shounen type movies.
# Here we will consider only category

#here data in categorical format we not need to check oulier

#----------------Model Building

#1)create TfidfVectorizer to separate all stop words

#for that used TfidfVectorizer lib
from sklearn.feature_extraction.text import TfidfVectorizer

# This is term frequency inverse document
# Each row is treated as document
tfidf = TfidfVectorizer(stop_words = 'english')

# It is going to create TfidfVectorizer to separate all stop words
# It is going to separate
# out all words from the row
# Now let us check is there any null value
df['Category'].isnull().sum()
# There are 0 null values

#2)create tfidf_matrix
# Now let us create tfidf_matrix
tfidf_matrix = tfidf.fit_transform(df.Category)

tfidf_matrix.shape
# You will get 51, 34
# It has created sparse matrix, it means
# that we have 34 category
# on this particular matrix, 
# we want to do item based recommendation, if a user has
# watched action movie, then you can recommend Jumanji (1995) like movies.

from sklearn.metrics.pairwise import linear_kernel
cosine_sim_matrix = linear_kernel(tfidf_matrix, tfidf_matrix)

# each element of tfidf_matrix is compared
# with each element of tfidf_matrix only
# output will be similarity matrixof size 51 X 51 size
# Here in cosine_sim_matrix,
# there are no movie names only index are provided
# We will try to map movie name with movie index given
# for that purpose custom function is written
# Check the size of the matrix
import numpy as np
matrix_size = np.shape(cosine_sim_matrix)
print("Size of the cosine similarity matrix:", matrix_size)

ent_index = pd.Series(df.index, index = df['Titles']).drop_duplicates()

# We are converting ent_index into series format, we want index and corresponding Category
# We are converting anime_index into series format, we want index and corresponding genre

ent_id = ent_index['Jumanji (1995)']
ent_id
#id of jumanji movie is 1

#create get_recommendation function
def get_recommendation(Name, topN):
    ent_id = ent_index[Name]
    #We want to capture whole row of given movie
    #name , its score and column id
    #For that purpose we are applying cosine_sin_matrix to enumerate function
    #Enumerate function create a object, 
    #which we need to create in list form
    #we are using enumerate function ,
    #what enumerate does , suppose we have given
    # (2,10,15,18) , if we apply to enumerate then it will create a list
    # (0,2,   1,10,   3,15,   4,18) 
    
    cosine_scores = list(enumerate(cosine_sim_matrix[ent_id]))
    #The cosine score captured , we want to arrange in descending order
    #so that
    #we can recommend top 10 based on highest similarity i.e. score
    #x[0]=index and x[1] is cosine score
    #we wnat arrange tuples according to decreasing order
    #of the score not index
    #Sorting the cosine_similarity score based on the scores i.e. x[1]
    
    cosine_scores = sorted(cosine_scores, key = lambda x : x[1], reverse = True)
    #Get the scores of top N most similar movies
    #To capture TopN movies ,  you need to give topN+1
    cosine_scores_N = cosine_scores[0:topN + 1]
    #getting the movie index
    ent_idx = [i[0] for i in cosine_scores_N]
    #getting cosine score
    ent_score = [i[1] for i in cosine_scores_N]
    
    #we are going to use this information to create a daatframe
    #create a empty dataframe
    ent_similar_show = pd.DataFrame(columns = ['Titles', 'score'])
    ent_similar_show['Titles'] = df.loc[ent_idx, 'Titles']
    ent_similar_show['score'] = ent_score
    #while assigning values, it is by default capturing original
    #index of the movie 
    #we want to reset the index
    
    ent_similar_show.reset_index(inplace = True)
    print(ent_similar_show)
    
get_recommendation('Jumanji (1995)',5)
"""   
index                    Titles     score
0      1            Jumanji (1995)  1.000000
1     24  Leaving Las Vegas (1995)  0.537426
2     35           Clueless (1995)  0.426853
3     15             Casino (1995)  0.343851
4      6            Sabrina (1995)  0.320244
5     13              Nixon (1995)  0.318409"""
# Action, Adventure, Shounen, Super Power

#---------------------Benifit of model
#to get any category movie recommendation.
#used in many platforms like youtube,netflix etc.
#-----------------------------Game Recommendation system-------------------
"""
business objective:
    Maximize: Maximize Sales Revenue
    Minimize: Minimize the Prediction Errors.
    
    constraints: Sales Revenue,Scalability etc.
"""

#import lib
import pandas as pd

#EDA

df = pd.read_csv("game.csv")

df.head()

df.dtypes
"""Out[134]: 
userId      int64
game       object
rating    float64
dtype: object"""

df.shape
# you will get 5000 record and 3 columns.

df.info()
#it has 0 not null values

df.isnull().sum()
# Dataset not contains the null values

df.columns
#Out[138]: Index(['userId', 'game', 'rating'], dtype='object')

df.game
# Here we will consider only game col

#here data in categorical format we not need to check oulier

#----------------Model Building

#1)create TfidfVectorizer to separate all stop words

#for that used TfidfVectorizer lib
from sklearn.feature_extraction.text import TfidfVectorizer

# This is term frequency inverse document
# Each row is treated as document
tfidf = TfidfVectorizer(stop_words = 'english')

# It is going to create TfidfVectorizer to separate all stop words
# Now let us check is there any null value
df['game'].isnull().sum()
# There are 0 null values
# Now let us create tfidf_matrix

tfidf_matrix = tfidf.fit_transform(df.game)
tfidf_matrix.shape
# You will get 5000, 3068
# It has created sparse matrix, it means
# that we have 3068 category
# on this particular matrix

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
game_index = pd.Series(df.index, index = df['game']).drop_duplicates()

# We are converting game_index into series format, we want index and corresponding Category
# We are converting game_index into series format, we want index and corresponding game

game_id = game_index['SoulCalibur']
game_id
#this game id is 3 and 3925
game_index

def get_recommendation(Game, topN):
    game_id = game_index[Game]
    #We want to capture whole row of given movie
    #name , its score and column id
    #For that purpose we are applying cosine_sin_matrix to enumerate function
    #Enumerate function create a object, 
    #which we need to create in list form
    #we are using enumerate function ,
    #what enumerate does , suppose we have given
    # (2,10,15,18) , if we apply to enumerate then it will create a list
    # (0,2,   1,10,   3,15,   4,18) 
    
    cosine_scores = list(enumerate(cosine_sim_matrix[game_id]))
    #The cosine score captured , we want to arrange in descending order
    #so that
    #we can recommend top 10 based on highest similarity i.e. score
    #x[0]=index and x[1] is cosine score
    #we wnat arrange tuples according to decreasing order
    #of the score not index
    #Sorting the cosine_similarity score based on the scores i.e. x[1]
    
    cosine_scores = sorted(cosine_scores, key=lambda x: x[1][0], reverse=True)
    #Get the scores of top N most similar games
    #To capture TopN games,  you need to give topN+1
    cosine_scores_N = cosine_scores[0:topN + 1]
    #getting the game index
    game_idx = [i[0] for i in cosine_scores_N]
    #getting cosine score
    game_score = [i[1] for i in cosine_scores_N]
    
    #we are going to use this information to create a daatframe
    #create a empty dataframe
    game_similar_show = pd.DataFrame(columns = ['game', 'score'])
    game_similar_show['game'] = df.loc[game_idx, 'game']
    game_similar_show['score'] = game_score
    #while assigning values, it is by default capturing original
    #index of the game
    #we want to reset the index
    
    game_similar_show.reset_index(inplace = True)
    print(game_similar_show)
    

get_recommendation("SoulCalibur", 10)
"""   
index                    game                           score
0      0    The Legend of Zelda: Ocarina of Time  [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, ...
1     1     Tony Hawk's Pro Skater 2              [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0., ...
"""
#---------------------Benifit of model
#to get any category game recommendation.
#used in many platforms like playstore etc.

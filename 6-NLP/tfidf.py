"""TF-IDF using TfidfVectorizer"""
from sklearn.feature_extraction.text import TfidfVectorizer

corpus = ['Thar eating pizza, Loki is eating pizza, Ironman ate pizza already',
          'Apple is announcing new iphone tommorow',
          'Tesla is announcing new model-3 tommorow',
          'Google is announcing new pixel-6 tommorow',
          'Microsoft is announcing new surface tommorow',
          'Amazon is announcing new eco-dot tommorow',
          'I am eating biryani and you are eatinjg grapes']

#let create the vectorizer and fit the corpus and transform them according
v = TfidfVectorizer()
v.fit(corpus)
transform_output = v.transform(corpus)

#let's print the vocabulary
print(v.vocabulary_)

#lets print idf of each word
all_feature_names = v.get_feature_names_out()
for word in all_feature_names:
    #lets get the index in the vocabulary
    index = v.vocabulary_.get(word)
    #get the score
    idf_score = v.idf_[index]
    print(f'{word} : {idf_score}')

###############################################################################

"""TF-IDF using TfidfTransformer"""
#imoport libraries
import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

corpus = ['The mouse has a tiny little mouse','The cat saw the mouse',
          'The cat catch the mouse','The end of mouse story']

#step 1 >> initialize the countvectorizer
cv = CountVectorizer()
#to count the total no. of TF
word_count_vector = cv.fit_transform(corpus)
word_count_vector.shape

#step 2 >> apply IDF
tfidf_transformer = TfidfTransformer(smooth_idf=True,use_idf=True)
tfidf_transformer.fit(word_count_vector)

#this matrix is in raw matrix form, let us convert it in dataframe
df_idf = pd.DataFrame(tfidf_transformer.idf_,index=cv.get_feature_names_out(),
                      columns=['idf-weights'])

#sort ascending
df_idf.sort_values(by=['idf-weights'])
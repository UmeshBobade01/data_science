""" NLP """

s='we are learning textmining from sanjivani AI'

#if we want to know the postion of learning
s.index('learning')
#Out[19]: 7
#here above just finding the index of letter

#we want to know position of word
s.split().index('textmining')
#Out[22]: 3

#print any word in reverse order
s.split()[2][::-1]

#suppose want to print forst and last word
words=s.split()
f_word=words[0]
f_word
l_word=words[-1]
l_word

#now we want to concate the first and last word
concate_word=f_word+' '+l_word
concate_word

#we want to print even words from senetence using list comprh
[words[i] for i in range(len(words)) if i%2==0]
#words having add length will not be printed

s[-3:]
#Out[34]: ' AI'
#it will start from -3,-2,-1 i.e.->AI

#revese the sentence
s[::-1]
#Out[35]: 'IA inavijnas morf gninimtxet gninrael era ew'

words
print(" ".join(word[::-1] for word in words))
#ew era gninrael gninimtxet morf inavijnas IA

#tokenizing
#punkt-> it is a sentence tokenizer
#it divide list 
import nltk
nltk.download('punkt')
from nltk import word_tokenize
words=word_tokenize('I am reading Nlp fundamentals')
print(words)

#Parts Of Speech(POS) tagging
nltk.download("averaged_perceptron_tagger")
nltk.pos_tags(words)

#stop words from NLTK library
from nltk.corpus import stopwords
stop_words = stopwords.words("English")
print(stop_words)

#
s1 = 'I am learning NLP:It is one of the most popular library in Python'
#tokenize
sentence_words = word_tokenize(s1)
print(sentence_words)
#remove stop words
sentence_no_stops = " ".join([words for words in sentence_words if words not in stopwords.words("English")])
print(sentence_no_stops)
s1

#Tokenization using Keras 
#sentence5
sentence5='The cute little boy is playing with kittle'
from keras.preprocessing.text import text_to_word_sequence 
text_to_word_sequence(sentence5)

################################
#Tokenization using TextBlob 
from textblob import TextBlob
blob = TextBlob(sentence5)
blob.words
################################
#Tweet Tokenizer
from nltk.tokenize import TweetTokenizer 
tweet_tokenizer = TweetTokenizer()
tweet_tokenizer.tokenize(sentence5)
################################
#Multi-word_Expression 
from nltk.tokenize import MWETokenizer 
sentence5
mwe_tokenizer=MWETokenizer([('republic','day')])
mwe_tokenizer=tokenizer(sentence5.split())
mwe_tokenizer=tokenizer(sentence5.replace('/',' ').split())
##################################
#Regular Expression Tokenizer 
from nltk.tolenizer import TegexpTokenizer
reg_tokenizer = RegexpTokenizer('\w+/\$[\d\.]+/\S+')
reg_tokenizer.tokenize(sentence5)
##################################
#White space tokenizer
from nltk.tolennizer import WhitespaceTokenizer
wh_tokenizer=WhitespaceTokenizer()
wh_tokenizer.tokenizer(sentence5)

###################################
from nltk.tokenize import WorkPunctTokenizer
wp_tokenizer =WordPunctTokenizer()
wp_tokenizer.tokenizer(senctence5)
###################################
sentence6="I love playing cricket.Cricket players practices hard in their inning"
from nltk.strem import TegexStemmer
regex_stemmer = RegexpStemmer('ing$')
" ".join(regex_stemmer.stem(wd) for wd in sentence6.split())
####################################

sentence7 = 'Before eating ,it would be nice to sanitize your hand with a sanitizer'
from nltk.stem.porter import PorterStemmer 
ps_stemmer = PorterStemmer()
words=sentence7.split()
" " .join([ps_stemmer.stem(wd) for wd in words])

######################################
#Lemmatization 
import nltk 
from nltk.stem import WordNetLemmatizer 
from nltk import woed_tokenize 
nltk.download('wordnet')
lemmatizer=WordNetLemmatizer()
sentence8 = "The codes executed today are far better than what we execute generally"
words = word_tokenize(sentence8)
" ".join([lemmatizer.lemmatize(word) for word in words])
#######################################
#singularize and pluralization 
from textblob import TextBlob
sentence9 = TextBlob("She sells seashells on the seashore")
words = sentence9.words
##we want to make word[2] i.e. seashells in singular form 
sentence9.words[2].singularize()
##we want word 5 i.e seashore i plural form 
sentence9.words[5].pluralize() 
#######################################
#language translation from spanish to English 
from textblob import TextBlob 
en_blob = TextBlob(u'muy bien')
en_blob.translate(from_lang='es', to='en')
#es:spanish en:English
#######################################
##custom stopwords removal 
from nltk import word_tokenize
sentence9="She sells seashells on the seashore"
custom_stop_word_list = ['she','on','the','am','is']
words = word_tokenize(sentence9)
" ".join([word for word in words if word.lower() not in custom_stop_word_list])
#select words which are not in defined list

#identify the number of words
import pandas as pd
df = pd.DataFrame([['the vaccinefor covid-19 will be announced on 1 st August'],
                   ['Do you know how much expections the world population is having from this research'],
                   ['The risk of virus will come to an end on 31st July']])

df.columns=['text']
df

from textblob import TextBlob
df['number_of_words'] = df['text'].apply(lambda x:len(TextBlob(x).words))
df['number_of_words']

#detect presence of any word in sentence
#detect the wh-words
wh_words = set(['why','who','which','what','where','when','how'])
#df['is_wh-word_present'] = df['text'].apply(lambda x: True if len(set(TextBlob(str(x)))))


#polarity of the sentence
df['polarity'] = df['text'].apply(lambda x:TextBlob(str(x)).sentiment.polarity)
df['polarity']

sentence = 'i like this example very much'
pol = TextBlob(sentence).sentiment.polarity
pol

#subjectivity  of sentence
df['subjectivity'] = df['text'].apply(lambda x:TextBlob(str(x)).sentiment.subjectivity)
df['subjectivity']

#to check language
df['language'] = df['text'].apply(lambda x:TextBlob(str(x)).detect_language())
df['language']


























import nltk
from nltk import word_tokenize
from nltk import pos_tag
import string
nltk.download('punkt')
nltk.download('universal_tagset')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import stopwords
nltk.download('stopwords')

str=input("Enter data:")
tokenized_word=word_tokenize(str)
print("Extracting all the word with punctuation:")
print(tokenized_word)
print("Extracting all the word with out punctuation:")
list=[]
for i in tokenized_word:
  if i not in string.punctuation:
    list.append(i)

print(list)
punc=[]
for i in list:
  punc=pos_tag(i)
print(punc)
print("Words without stopwords")
msg=[i for i in list if i.lower() not in stopwords.words() ]
print(msg)

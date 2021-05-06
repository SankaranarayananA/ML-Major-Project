import streamlit as st
import sklearn
import joblib
import spacy
import string
from spacy.lang.en.stop_words import STOP_WORDS
stopwords= list(STOP_WORDS)
nlp= spacy.load("en_core_web_sm")
punct = string.punctuation
def text_cleaning(vario): # accept only 1 review at a run
  doc = nlp(vario) # calling spacy model to work on a SENTENCE 
 
  
  tokens = [] # list of tokens

  # lowering case all tokens 
  
  for token in doc:

# if root form(token) of that word is not pronoun then it is going to convert that into lowercase
    if token.lemma_ !="-PRON-":
      temp = token.lemma_.lower().strip()
    else:
# If that word is proper noun,then it directly taking lower case, because there is no lemma for proper noun
      temp = token.lower_
    tokens.append(temp)



  cleaned_tokens= [] 
  # removing all punctuation and stopword tokens  
  for token in tokens:
    if token not in stopwords and token not in punct:
      cleaned_tokens.append(token)
  return cleaned_tokens  
model = joblib.load('Sentia')
st.title('Sentiment Analysis')
ip = st.text_input("Enter the Review")
op = model.predict([ip])
if st.button('Work'):
    st.title(op[0])

    

import streamlit as st 
import nltk 
from transformers import pipeline
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

chatbot = pipeline("text-generation",  model="distilgpt2" )

def health(user_input):
     if "symptom" in user_input :
        return "Please consult docter for accurate advice "
     elif "appointemnt" in user_input :
         return " would u like to schedule an appointment with docter"
     elif "medication" in user_input:
         return "it is important to take prescribed medicines regularly please consult your docter "
     else :
         response = chatbot(user_input, max_length = 500 , num_return_sequences = 1)
         return response[0]['generated_text']
     

def main():
    st.title("Healthcare Assistant chatbot ")
    user_input = st.text_input("how can i assist you today ")
    if st.button("Submit"):
        if user_input:
            st.write("User : ", user_input)
            with st .spinner("Please wait for the response"):
              response = health(user_input)
            st.write("CARETAKER : ", response)
            print(response)
        else:
            st.write("please enter a msg to get a response")    

main()
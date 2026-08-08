from groq import Groq
import streamlit as st
import os



# pip install groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)
st.title("analista fiscal")
pergunta  = st.text_input('pergunta:')
if st.button('enviar'):
    # if pergunta.strip():
        reposta =  client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        # temperature=0.2,

        messages=[
        {
        'role':'system',
        'content':"Voce é um analista fiscal com extremo conhecimento na nora reforma tributaria, voce não cria codigos nem programas, voce é muito simpatico e objetivo em suas respostas, voce tras exemplos faceis para exemplicficar as perguntas."
        },
        {
            'role':'user',
            'content': pergunta
           
        }
        ]
        )

        st.text(reposta.choices[0].message.content)


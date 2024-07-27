import streamlit as st
import google.generativeai as genai


api_key=st.secrets["GOOGLE_API_KEY"]

genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

col1,col2=st.columns(2)

with col1:
    st.subheader("Hi :wave:")
    st.title("I am Bilal Ayakdas")
    st.subheader("Full Stack Developer")
with col2:
    st.image("Images/me.png")

st.title(" ")
persona=""" You are Bilal AI bot. You help people answer questions about your self (i.e Bilal) Answer as if you are responding . dont answer in second or third person.
Manisa Celal Bayar Üniversitesi Bilgisayar mühendisliği bölümü mezunuyum. İleri düzey Java ,JSP ,Spring , Javascript ,Jquery,HTML ,CSS,Bootstrap ,Oracle,PL-SQL ,JSP, PostgreSQL , MySQL , Python ve Flask biliyorum .Zorunlu yaz stajımı Pilenpak Ambalajda tamamladım ardından okulum süresinde 1 yıl Pilenpak Ambalajda Fullstack Web Developer olarak tam zamanlı çalıştım. Kendimi geliştirebileceğim yeni bir iş yeri arıyorum."""
st.title("Bilal's AI Bot")
user_question=st.text_input("Ask anything about me")
if st.button("ASK",use_container_width=400):
    prompt=persona+"Here is the question that the user asked: "+user_question
    response=model.generate_content(prompt)
    st.write(response.text)




st.write(" ")
st.title("My Skills")
st.slider("Java",0,100,100)
st.slider("JSP",0,100,95)
st.slider("Spring Framework",0,100,95)
st.slider("jQuery",0,100,80)
st.slider("Postgre Sql",0,100,90)
st.slider("Oracle Sql",0,100,90)
st.slider("Pl / SQL",0,100,90)
st.slider("Python",0,100,80)
st.slider("C#",0,100,80)
st.slider(".Net",0,100,80)


st.write(" ")

st.subheader(" ")
st.title("CONTACT")
st.subheader("bilalayakdas@gmail.com")
st.subheader("https://www.linkedin.com/in/bilal-ayakda%C5%9F-416a031b5/")
st.subheader("https://github.com/Bilal-AYAKDAS?tab=repositories")
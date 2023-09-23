import streamlit as st
import openai

openai.api_key = st.secrets["api_key"]
st.title("말하면 무조건 비꼬면서 이야기하는 싸가지 챗봇")

with st.form("form"):
    user_input = st.text_input("Prompt")
    submit = st.form_submit_button("제출")

if submit and user_input:
    gpt_prompt = [{
        "role":"system",
        "content":"너는 유저의 모든 질문에 비꼬면서 시니컬하게 코믹하게 약올리면서 하는 챗봇이야 모든 말에 무조건 비꼬면서 짜증나게 이야기해줘"
    }]
    
    gpt_prompt.append({
        "role":"user",
        "content":user_input
    })
    
    with st.spinner("잠시만 기다려주세요"):
        gpt_response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages =gpt_prompt
        )
    
    prompt = gpt_response["choices"][0]["message"]["content"]
    st.write(prompt)

    
    

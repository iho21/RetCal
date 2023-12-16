import streamlit as st
import pandas as pd
import requests as rq
from openai import OpenAI

st.title("Retire With FIRE")
st.caption("Financial indepenendence, retire early")

## TODO: Write starting questionnaire.

if True:
    questionnaire = st.container()

    with st.expander("Stuck?"):
        st.title("Chatbot")
        st.caption("🚀 powered by OpenAI LLM")
        openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")

        if "messages" not in st.session_state:
            st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
        
        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg["content"])
            if prompt := st.text_input("Your Question"):
                if not openai_api_key:
                    st.info("Please add your OpenAI API key to continue.")
                    st.stop()
                
                client = OpenAI(api_key=openai_api_key)
                
                st.session_state.messages.append({"role": "user", "content": prompt})
                st.chat_message("user").write(prompt)
                response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
                msg = response.choices[0].message
                st.session_state.messages.append(msg)
                st.chat_message("assistant").write(msg.content)


    ## TODO: Add ChatGPT help line. 

    ## TODO: Take current or planned starting income.

    ## TODO: Take expected income increase.

    ## TODO: Take estimated cost of living.

    ## TODO: Take mutex fund info.

    ## TODO OPTIONAL: Take 401k match info.

    ## TODO OPTIONAL: Take IRA info.

    ## TODO OPTIONAL: Take treasury bond info.

    ## TODO: Take savings accounts, money market accounts, and cash.
    
    ## TODO: Take planned retirement year.

    ## TODO OPTIONAL: Take number of years planned to be retired. 



## TODO: Write graphical results and calculator interface. 

#if False:
    ## TODO: Write income per year while retired and maximum number of years before money runs out.

    ## TODO: Display line graph of mean income from accounts versus annual cost of living. 

    ## TODO: Allow adjustments in sidebar. 

    ## TODO OPTIONAL: Save CSV. 

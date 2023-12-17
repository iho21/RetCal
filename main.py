import streamlit as st
import numpy as np
import pandas as pd
import requests as rq
import backoff
from openai import OpenAI
import openai

st.title("Retire With FIRE")
st.caption("Financial indepenendence, retire early")

## TODO: Write starting questionnaire.
hi = False
if hi:
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

    ## TODO OPTIONAL: Take current debts.

    ## TODO: Take savings accounts, money market accounts, and cash.
    
    ## TODO: Take planned retirement year.

    ## TODO OPTIONAL: Take number of years planned to be retired. 



## TODO: Write graphical results and calculator interface. 

else:
    ## TODO: Write income per year while retired and maximum number of years before money runs out.
    with st.sidebar:
        st.write("Done")

        with st.expander("Explain My Results"):
            st.caption("powered by OpenAI LLM")
            openai_api_key = st.text_input("OpenAI Key", type="password")

            if "messages" not in st.session_state:
                st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
            
            for msg in st.session_state.messages:
                st.chat_message(msg["role"]).write(msg["content"])
                if prompt := st.text_input("Ask Questions"):
                    if not openai_api_key:
                        st.info("Please add your OpenAI API key.")

                    else:
                        try:
                            client = OpenAI(api_key=openai_api_key)

                            st.session_state.messages.append({"role": "user", "content": prompt})
                            st.chat_message("user").write(prompt)

                            @backoff.on_exception(backoff.expo, openai.RateLimitError)
                            def completions_with_backoff(**kwargs):
                                return client.chat.completions.create(**kwargs)
                            
                            response = completions_with_backoff(model="gpt-3.5-turbo", messages=st.session_state.messages)

                            msg = response.choices[0].message
                            st.session_state.messages.append(msg)
                            st.chat_message("assistant").write(msg.content)

                        finally:
                            st.chat_message("assistant").write("Sorry, an error occured. Try again in a moment.")
    ## TODO: Display line graph of mean income from accounts versus annual cost of living. 
    col1, col2 = st.columns(2)

    with col1:
        st.metric("When you retire you'll make", "$50,000 per year")
        st.metric("The most expensive metro area you can live in is", "West Balm Peach")
        st.metric("For investing $500,000 you will get back", "$1,200,000")
    
    with col2:
        chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
        st.line_chart(chart_data)

        st.dataframe(chart_data)
    ## TODO: Allow adjustments in sidebar. 

    ## TODO OPTIONAL: Save CSV. 

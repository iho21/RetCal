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
if not hi:
    questionnaire = st.container()

    with st.expander("Stuck?"):
        st.title("Chatbot")
        st.caption("🚀 powered by OpenAI LLM")
        openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")

        if "messages" not in st.session_state:
            st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
        
        for msg in st.session_state.messages:

            st.chat_message(msg["role"]).write(msg["content"])
            if prompt := st.text_input("Your Question", key="form_help"):

                if not openai_api_key:
                    st.info("Please add your OpenAI API key to continue.")
                    st.stop()
                
                client = OpenAI(api_key=openai_api_key)

                st.session_state.messages.append({"role": "user", "content": prompt})
                # st.chat_message("user").write(prompt)
                response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
                msg = response.choices[0].message
                st.session_state.messages.append(msg)
                # st.chat_message("assistant").write(msg.content)


    ## TODO: Add ChatGPT help line. 

    ## TODO: Take current or planned starting income.

    ## TODO: Take expected income increase.

    ## TODO: Take estimated cost of living.

    ## TODO: Take mutex fund info.
    principal = st.number_input("Principal")

    ## TODO OPTIONAL: Take 401k match info.

    ## TODO OPTIONAL: Take IRA info.

    ## TODO OPTIONAL: Take treasury bond info.
    interest = st.number_input("Interest rate")

    ## TODO OPTIONAL: Take current debts.

    ## TODO: Take savings accounts, money market accounts, and cash.
    
    ## TODO: Take planned retirement year.
    years_to_retirement = st.number_input("Years to retire")

    result = principal * pow(1 + interest / 100, years_to_retirement)

    if st.button("Start"):
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
                    if prompt := st.text_input("Ask Questions", key="results_help"):
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
            st.metric("When you retire you'll make", f"${result} per year")
            st.metric("The most expensive metro area you can live in is", "West Balm Peach")
            st.metric(f"For investing ${principal} you will get back", f"${result - principal}")
        
        with col2:
            chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
            st.line_chart(chart_data)

            st.dataframe(chart_data)
        ## TODO: Allow adjustments in sidebar. 

        ## TODO OPTIONAL: Save CSV. 

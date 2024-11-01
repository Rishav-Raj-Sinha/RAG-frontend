import streamlit as st


# # Set page configuration and hide headers/footers
st.set_page_config(page_title="DetectiNator", layout="wide", initial_sidebar_state="collapsed")
hide_decoration_bar_style = '''<style>header {visibility: hidden;}
</style><style>footer{visibility: hidden;}</style>'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)


st.title("RAG-LLM")
with st.container(border =True,height = 750):

    with st.container(border = True,height = 150):
        user_data = st.file_uploader("Upload your data")
    with st.container(border = True,height = 550):
        prompt = st.chat_input("Say something") # "prompt" variable takes the user input

        if prompt:
            if user_data:
                input = st.chat_message("User")
                input.write(prompt )
                output = st.chat_message("assistant")
                output.write("Hello human") #this line gives the output that is generated using the llm
            else:
                st.warning("No data was found", icon="⚠️")

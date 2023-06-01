import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from haystack.nodes import PromptNode, PromptTemplate, PromptModelInvocationLayer, PromptModel
from haystack.nodes.prompt.invocation_layer import HFLocalInvocationLayer
from haystack.nodes import BM25Retriever
from haystack.pipelines import Pipeline
import os
import psutil
import time
from HayDocumentStore import initialize_document_store

st.set_page_config(page_title="Procu-Chat - Powered by Deep Learning!")

# Sidebar contents
with st.sidebar:
    st.title('🚀 Procu-Chat App')
    st.markdown('''
    ## About
    This rocket specs🚀:
    - InMemoryDocumentStore
    - BM25Retriever
    - Google Flan T5 Large LLM
    💡
    ''')
    add_vertical_space(5)

    if st.button('Clear Chat History'):
        # Clear the chat history lists
        st.session_state['generated'] = []
        st.session_state['past'] = []

    st.write('Made with sheer willpower 💥')

# Generate empty lists for generated and past.
## generated stores AI generated responses
if 'generated' not in st.session_state:
    st.session_state['generated'] = ["Hi! I'm PPA-Bot, How may I help you?"]
## past stores User's questions
if 'past' not in st.session_state:
    st.session_state['past'] = ['Hi!']

# Layout of input/response containers
input_container = st.container()
colored_header(label='', description='', color_name='blue-30')
response_container = st.container()

# User input
## Function for taking user provided prompt as input
def get_text():
    input_text = st.text_input("You: ", "", key="input")
    return input_text

## Applying the user input box
with input_container:
    user_input = get_text()

# Load the document store and retriever
document_store, retriever = initialize_document_store()

def Haystack(prompt):
    lfqa_prompt = PromptTemplate(
        name="lfqa",
        prompt_text="""Synthesize a comprehensive answer from the following text for the given question. 
                                Provide a clear and concise response that summarizes the key points and information presented in the text. 
                                Your answer should be in your own words and be no longer than 500 words. 
                                \n\n Related text: {join(documents)} \n\n Question: {query} \n\n Answer:""",
    )

    Directory = r"" + os.getcwd() + "\\GoogleT5"

    #USE THIS!
    google_flant5_prompt_model = PromptModel(
        model_name_or_path=Directory,
        model_kwargs={"task_name":"text2text-generation"},
        invocation_layer_class=HFLocalInvocationLayer
        )

    prompt_node = PromptNode(model_name_or_path=google_flant5_prompt_model , default_prompt_template=lfqa_prompt,)
    pipe = Pipeline()
    pipe.add_node(component=retriever, name="retriever", inputs=["Query"])
    pipe.add_node(component=prompt_node, name="prompt_node", inputs=["retriever"])
    results = []
    output = pipe.run(query=prompt)
    results.append(output["results"])
    output=results[-1]
    return output

# Response output
## Function for taking user prompt as input followed by producing AI generated responses
def generate_response(prompt):
    Amended_prompt = prompt
    response = Haystack(Amended_prompt)
    return response

## Conditional display of AI generated responses as a function of user provided prompts
with response_container:
    if user_input:
        response = generate_response(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)
        
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated']))[::-1]:
            message(st.session_state["generated"][i], key=str(i))
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')

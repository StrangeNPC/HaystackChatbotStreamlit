
# Haystacks Streamlit Chatbot


The Haystacks Streamlit Chatbot is a chatbot powered by deep learning. It utilizes the Haystack framework and the Google Flan T5 Large LLM model to provide AI-generated responses to user prompts. The app is designed to be user-friendly and easy to use.







## Installation

1. Clone to your repository:

```bash
https://github.com/StrangeNPC/HaystackChatbotStreamlit.git

```

2. Install the requirements needed in the terminal:
```bash
pip install -r requirements.txt

```
3. Make sure you have the necessary files in your project directory:

- Notice.txt: The text file containing the document you want to index and search.
- Google T5 Flan model downloaded from Huggingface and placed in the same directory/folder as these files.

4. Run the 'StreamlitX.py' file to start the app:

```bash
streamlit run main.py

```
## Usage
1. Once the app is running, you will see a sidebar on the left with some information about the app.

2. To clear the chat history, click the "Clear Chat History" button in the sidebar.

3. Type your question or prompt in the input box and press Enter

4. The app will generate AI-generated responses based on your input and display them in the response container.

5. The user's questions and AI-generated responses will be stored in the chat history and displayed in the response container.

## Notes
- The app uses an InMemoryDocumentStore to store and index the documents. The Notice.txt file is converted into a format suitable for indexing using the TextConverter and PreProcessor components.

- The app uses the BM25Retriever for document retrieval based on the user's queries.

- The Google Flan T5 Large LLM model is used for generating responses. It is loaded from the GoogleT5 directory.

- The app is built using the Streamlit framework, which provides a user-friendly web interface.

- The app allows you to have interactive conversations with the chatbot, and you can clear the chat history whenever needed.
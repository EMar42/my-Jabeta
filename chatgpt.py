import sys
import os

from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader
from langchain.vectorstores import Chroma
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.indexes import VectorstoreIndexCreator

# Set OpenAI API key "<ENTER YOUR KEY>"
os.environ["OPENAI_API_KEY"] = "<ENTER YOUR KEY>"

# Enable to save to disk & reuse the model (for repeated queries on the same data)
PERSIST = False

def initialize_chain(persist=False):
    # Check if index persistence is enabled and index already exists
    if persist and os.path.exists("persist"):
        print("Reusing index...\n")
        vectorstore = Chroma(persist_directory="persist", embedding_function=OpenAIEmbeddings())
        index = VectorStoreIndexWrapper(vectorstore=vectorstore)
    else:
        # Load documents from a directory
        loader = DirectoryLoader("data/")
        if persist:
            # Create vectorstore with persistent storage
            index = VectorstoreIndexCreator(vectorstore_kwargs={"persist_directory": "persist"}).from_loaders([loader])
        else:
            # Create vectorstore without persistent storage
            index = VectorstoreIndexCreator().from_loaders([loader])

    # Create ConversationalRetrievalChain with OpenAI language model and vectorstore retriever
    chain = ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(model="gpt-3.5-turbo"),
        retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
    )

    return chain

def get_user_input():
    # Get user input for query
    query = input("Prompt: ")
    return query

def run_chatbot():
    # Initialize chain and chat history
    chain = initialize_chain(PERSIST)
    chat_history = []

    while True:
        # Get user input
        query = get_user_input()

        # Check for exit command
        if query in ['quit', 'q', 'exit']:
            sys.exit()

        # Retrieve answer from chain based on user query
        result = chain({"question": query, "chat_history": chat_history})
        print(result['answer'])

        # Append user query and answer to chat history
        chat_history.append((query, result['answer']))

if __name__ == "__main__":
    run_chatbot()

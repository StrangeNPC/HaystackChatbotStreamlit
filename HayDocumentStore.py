from haystack.document_stores import InMemoryDocumentStore
from haystack.nodes import BM25Retriever
from haystack.nodes import PreProcessor
from haystack.nodes import TextConverter, PDFToTextConverter, DocxToTextConverter, PreProcessor

import os
import time
import psutil

def initialize_document_store():
    document_store = InMemoryDocumentStore(use_bm25=True)
    
    # Initialize and configure other components like TextConverter, PreProcessor, etc.
    converter = TextConverter(remove_numeric_tables=True, valid_languages=["en"])
    doc_txt = converter.convert(file_path="Notice.txt", meta=None)[0]
    preprocessor = PreProcessor(
        clean_empty_lines=True,
        clean_whitespace=True,
        clean_header_footer=False,
        split_by="word",
        split_length=100,
        split_respect_sentence_boundary=True,
    )
    docs_default = preprocessor.process([doc_txt])
    
    # Index the documents
    document_store.write_documents(docs_default)
    
    # Initialize the retriever
    retriever = BM25Retriever(document_store=document_store, top_k=2)

    # Return the initialized components
    return document_store, retriever

if __name__ == "__main__":
    # Run the initialization function
    document_store, retriever = initialize_document_store()
    
    # Start any other necessary components or services
    # For example, if you have a T5 model, you can start it here
    
    # Check if called from Streamlit
    if psutil.Process().name() == "StreamlitX":
        # Increase process priority when called from Streamlit
        psutil.Process().nice(psutil.HIGH_PRIORITY_CLASS)
        print('High!')

    else:
        # Decrease process priority when called as a standalone script
        psutil.Process().nice(psutil.IDLE_PRIORITY_CLASS)
        print('idle!')
    
    # Keep the process running
    while True:
        time.sleep(10)  # Add a delay to avoid high CPU usage

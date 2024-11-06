from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
import os
import shutil
from langchain.docstore.document import Document


class regulation_ingestion_class:
    # Function to move a file to the archive folder after processing
    def move_to_archive(self,file_path,archive_folder):
        if not os.path.exists(archive_folder):
            os.makedirs(archive_folder)
        shutil.move(file_path, os.path.join(archive_folder, os.path.basename(file_path)))
    
    def ingest_regulation_files(self,Azure_Client , regulation_ingestion_dict, regulations_path, chunk_size = 1000, chunk_overlap = 200):
        # Loop through each regulation subfolder
        for regulation_folder in os.listdir(regulations_path):
            regulation_folder_path = os.path.join(regulations_path, regulation_folder)
        
            # Extract regulation name from the folder (assuming folder name starts with 'Reg_X')
            regulation_name = regulation_folder.split()[0]
        
            # Check if ingestion is enabled for the current regulation
            if not regulation_ingestion_dict.get(regulation_name, False):
                print(f"Ingestion for {regulation_name} is disabled.")
                continue
        
            archive_folder_path = os.path.join(regulation_folder_path, "archive")
        
            # Get a list of PDF files in the current regulation folder, excluding the archive folder
            pdf_files = [f for f in os.listdir(regulation_folder_path) if f.endswith(".pdf") and f != "archive"]
        
            if not pdf_files:
                print(f"No files to ingest for {regulation_folder}.")
                continue
        
            for pdf_file in pdf_files:
                pdf_file_path = os.path.join(regulation_folder_path, pdf_file)
        
                print(f"Processing {regulation_folder} - {pdf_file}...")
        
                # Load the PDF for the current regulation
                reg_loader = PyPDFLoader(pdf_file_path)
                reg_documents = reg_loader.load()
        
                # Split the documents into chunks
                text_splitter = RecursiveCharacterTextSplitter(chunk_size = chunk_size, chunk_overlap = chunk_overlap)
                reg_text_chunks = text_splitter.split_documents(reg_documents)
        
                # Add metadata to each chunk
                for i, chunk in enumerate(reg_text_chunks):
                    chunk.metadata = {
                                        "source": pdf_file_path,
                                        "document_type": "Regulation",
                                        "regulation_name": regulation_folder,  # Use folder name as regulation name
                                        "file_name": pdf_file,
                                        "chunk_index": i  # Track chunk index
                                    }
        
                # Convert the documents to the format Azure Search expects
                azure_documents = [Document(page_content=doc.page_content, metadata=doc.metadata) for doc in reg_text_chunks]
        
                # Upload the chunks to Azure Cognitive Search
                print(f"Uploading {len(azure_documents)} chunks for {pdf_file} to Azure Cognitive Search...")
                Azure_Client.add_documents(azure_documents)
        
                # Move the processed PDF to the archive folder
                self.move_to_archive(pdf_file_path, archive_folder_path)
        
            print(f"All files for {regulation_folder} have been processed and moved to the archive.")
        
        print("All regulation documents uploaded to Azure Cognitive Search.")
        return None
                    
                
                
        
# if __name__ == "__main__":
#     import pandas as pd
#     cart_path         = r'C:\GenAI\CART-Azure-IAAS'
#     regulations_path  = cart_path + '\\regulations'
#     vector_db_path    = cart_path + '\\vector_db\\'
#     employee_id       = "c6400" #getpass.getuser()
#     version           = 1.0
    
#     os.environ["OPENAI_API_VERSION"]      = AZURE_OPENAI_API_VERSION_CHAT
#     os.environ["AZURE_OPENAI_ENDPOINT"]   = AZURE_OPENAI_ENDPOINT
#     os.environ["AZURE_OPENAI_API_KEY"]    = AZURE_OPENAI_API_KEY
    
#     print("Establishing connection with GPT-4 Turbo OpenAI LLM.")
#     llm = AzureChatOpenAI(
#                             deployment_name = deployment_name,
#                             temperature=0.0
#                         )
#     print("Established connection with GPT-4 Turbo OpenAI LLM.")

#     print("Fetching GPT-4 OpenAI Embeddings.")
#     embeddings_model = AzureOpenAIEmbeddings(
#                                                 model          = "text-embedding-ada-002",
#                                                 azure_endpoint = AZURE_OPENAI_ENDPOINT,
#                                                 api_key        = AZURE_OPENAI_API_KEY,
#                                                 openai_api_version = AZURE_OPENAI_API_VERSION_EMBEDDING
#                                             )
#     print("Fetched with GPT-4 OpenAI Embeddings.")
    
#     print("Initializing Azure Search.")

#     Azure_Client = AzureSearch(
#                                      azure_search_endpoint = AZURE_COGNITIVE_SEARCH_SERVICE_ENDPOINT,
#                                      azure_search_key      = AZURE_COGNITIVE_SEARCH_API_KEY,
#                                      index_name            = AZURE_COGNITIVE_SEARCH_INDEX_NAME,
#                                      embedding_function    = embeddings_model.embed_query ,
#                               )
    
#     print("AzureSearch client initialized successfully.")
    
#     import pyodbc
#     #Azure SQL Server Credentials
#     SQL_USER_NAME = "c6400"
#     SQL_PASSWORD  = "Majorda@619316"
#     server        = 'desktop-vonkkuh.database.windows.net'  # e.g., 'localhost\SQLEXPRESS'
#     database      = 'CART'  # e.g., 'CART_DB'
#     driver        = '{ODBC Driver 17 for SQL Server}'  # Ensure you have the correct ODBC driver installed # Ensure you have the correct ODBC driver installed
#     conn          = pyodbc.connect(
#                                         f'DRIVER={driver};'
#                                         f'SERVER={server};'
#                                         f'DATABASE={database};'
#                                         f'UID={SQL_USER_NAME};'
#                                         f'PWD={SQL_PASSWORD};'
#                                         'Encrypt=yes;'  # Ensure encryption is enabled for Azure SQL
#                                         'TrustServerCertificate=no;'  # Recommended for security
#                                         'Connection Timeout=30;'
#                                   )

#     from database_activity import database_activity_class
#     database_activity_class_obj = database_activity_class()  
    

#     table_action = "insert"
#     update_column = None
#     update_column_value = None
#     cart_log_id = database_activity_class_obj.cart_log_entry(conn,table_action,update_column,update_column_value,version,employee_id,cart_log_id = None)
    
#     stored_procedure = '[dbo].[uspload_cart_untagged_complaints]'
#     database_activity_class_obj.generate_untagged_complaints(conn,stored_procedure)
    
#     untagged_complaints_table = '[dbo].[cart_untagged_complaints]'
#     untagged_complaints_df = database_activity_class_obj.import_untagged_complaints(conn,untagged_complaints_table)

#     regulation_ingestion_dict =   {
#                           'Reg_B':True,
#                           'Reg_C':True,
#                           'Reg_D':True,
#                           'Reg_E':True,
#                           'Reg_F':True,
#                           'Reg_G':True,
#                           'Reg_H':True,
#                           'Reg_I':True,
#                           'Reg_J':True,
#                           'Reg_K':True,
#                           'Reg_L':True,
#                           'Reg_M':True,
#                           'Reg_N':True,
#                           'Reg_O':True,
#                           'Reg_P':True,
#                           'Reg_V':True,
#                           'Reg_X':True,
#                           'Reg_Z':True,
#                           'Reg_CC':True,
#                           'Reg_DD':True,
#                           'Reg_AA':True
#                         }
#     regulation_ingestion_class_obj = regulation_ingestion_class()
#     regulation_ingestion_class_obj.ingest_regulation_files(Azure_Client , regulation_ingestion_dict, regulations_path, chunk_size = 1000, chunk_overlap = 200)
    
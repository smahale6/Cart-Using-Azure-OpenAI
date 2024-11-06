import os
import time
import pandas as pd
import numpy as np
import pyodbc
from dotenv import load_dotenv
from datetime import datetime

from langchain.chat_models import AzureChatOpenAI
from langchain.vectorstores import AzureSearch
from langchain_openai import AzureOpenAIEmbeddings

from src.database_activity import database_activity_class
from src.regulation_text_ingestion import regulation_ingestion_class
from src.prompt_retriever_chain_formation import regulation_prompt_retriever_chain_class
from src.fetch_complaints_api import fetch_compalints_class
from src.classify_complaints import classify_complaints_class


# file_path = os.path.abspath("C:\GenAI\CART-Azure-IAAS")
# os.chdir(file_path)


import warnings
warnings.filterwarnings('ignore')


class cart_intersect_class:
    def __init__(self):
        self.cart_path                                   = os.path.dirname(os.path.abspath("CART_AZURE.py"))
        self.version                                     = 1.0
        self.regulations_path                            = self.cart_path  +'\\regulations\\'
        self.regulation_ingestion_class_obj              = regulation_ingestion_class()
        self.database_activity_class_obj                 = database_activity_class()  
        self.regulation_prompt_retriever_chain_class_obj = regulation_prompt_retriever_chain_class()
        self.fetch_compalints_class_obj                  = fetch_compalints_class()
        self.classify_complaints_class_obj               = classify_complaints_class()
        self.regulation_ingestion_dict                   = {'Reg_B':True,'Reg_C':True,'Reg_D':True,'Reg_E':True,'Reg_F':True,
                                                            'Reg_G':True,'Reg_H':True,'Reg_I':True,'Reg_J':True,'Reg_K':True,
                                                            'Reg_L':True,'Reg_M':True,'Reg_N':True,'Reg_O':True,'Reg_P':True,
                                                            'Reg_V':True,'Reg_X':True,'Reg_Z':True,'Reg_CC':True,
                                                            'Reg_DD':True,'Reg_AA':True}
        
    def get_classified_complaints(self,Azure_Client,employee_id,untagged_complaints_df,embeddings_model,llm,complaints_id_field,complaints_text_field,cart_log_id):
        tagged_complaints_final_df = untagged_complaints_df.copy()
        for reg_name in self.regulation_ingestion_dict.keys():
            ## Getting the regulation prompt template ready
            regulation_prompt                            = self.regulation_prompt_retriever_chain_class_obj.get_prompt(reg_name)
            ## Getting the retriever from b=vector store ready
            retriever                                    = self.regulation_prompt_retriever_chain_class_obj.get_retriever(Azure_Client,reg_name,embeddings_model)
            ## Creating a chain
            chain                                        = self.regulation_prompt_retriever_chain_class_obj.chain_formation(regulation_prompt,retriever,llm,reg_name)
            ## Classifying the complaint for each regulation
            tagged_complaints_df                         = self.classify_complaints_class_obj.tag_complaints(untagged_complaints_df,reg_name,complaints_id_field,complaints_text_field,chain)
            tagged_complaints_df                         = tagged_complaints_df.replace({np.nan: 0})
            tagged_complaints_df                         = tagged_complaints_df.replace({None: 0})
            tagged_complaints_final_df                   = pd.merge(tagged_complaints_final_df,tagged_complaints_df,how = 'left', on = complaints_id_field)
        tagged_complaints_final_df['Total_Tags'] = None
        tagged_complaints_final_df['Tagged_Regulations'] = None
        tagged_complaints_final_df['Loaded_By']          = employee_id
        tagged_complaints_final_df['Cart_Log_Id']        = cart_log_id
        tagged_complaints_final_df                       = tagged_complaints_final_df.replace({np.nan: None})
        #tagged_complaints_final_df.to_csv(r"C:\GenAI\CART-Azure-IAAS\data.csv")
        return tagged_complaints_final_df

    def run_cart(self,employee_id,date_received_min,date_received_max,company,size):
        start_time = time.time()
        ######################################################### Fetching Environmental Variables ############################################################
        load_dotenv() # Load environment variables from the .env file
        deployment_name                       = os.getenv('deployment_name')
        AZURE_OPENAI_API_KEY                  = os.getenv("AZURE_OPENAI_API_KEY")
        AZURE_OPENAI_ENDPOINT                 = os.getenv("AZURE_OPENAI_API_BASE")
        AZURE_OPENAI_API_VERSION              = os.getenv("AZURE_OPENAI_API_VERSION_CHAT")
        AZURE_OPENAI_API_VERSION_EMBEDDING    = os.getenv("AZURE_OPENAI_API_VERSION_EMBEDDING")
        SQL_USER_NAME                         = os.getenv("SQL_USER_NAME")
        SQL_PASSWORD                          = os.getenv("SQL_PASSWORD")
        ############################################################# Connecting to SQL Server ################################################################
        print("Connecting to SQL Server.")
        server    = 'desktop-vonkkuh.database.windows.net'  # e.g., 'localhost\SQLEXPRESS'
        database  = 'CART'  # e.g., 'CART_DB'
        driver    = '{ODBC Driver 17 for SQL Server}'  # Ensure you have the correct ODBC driver installed
        conn = pyodbc.connect(
                                    f'DRIVER={driver};'
                                    f'SERVER={server};'
                                    f'DATABASE={database};'
                                    f'UID={SQL_USER_NAME};'
                                    f'PWD={SQL_PASSWORD};'
                                    'Encrypt=yes;'  # Ensure encryption is enabled for Azure SQL
                                    'TrustServerCertificate=no;'  # Recommended for security
                                    'Connection Timeout=60;'
                                )
        print("Established  Connection to the CART Database in SQL Server.")
        
        #############################################################Checking user permissions ################################################################
        user_info_df      = pd.read_sql_query("Select * from [CART].[dbo].[cart_user_profile] where Employee_id = '{}'".format(employee_id),conn)
        if len(user_info_df) == 1:
            user_title        = user_info_df.loc[:,'Title'][0]
            user_first_name   = user_info_df.loc[:,'First_Name'][0]
            user_last_name    = user_info_df.loc[:,'Last_Name'][0]
            permissions       = user_info_df.loc[:,'Permissions'][0]
            manager           = user_info_df.loc[:,'Manager_Name'][0]
        else:
            raise ValueError(("The employee id {} does not have the permissions to use the Model Review Accelerator.".format(employee_id)))
       
        #############################################################Starting the Process################################################################
        print('###################################################################################################################################################')
        print('########################################## Hello {} {} {} #############################################################################'.format(user_title,user_first_name,user_last_name))
        print('################################# Welcome to the Complaints Analysis and Regulation Tool !!!!!!!!! ################################################')
        print('######################################## A product of NFCU Complaints Team ########################################################################')
        print('###################################################################################################################################################')
        time.sleep(5)
       
        if permissions == 1:
        #############################################################Connecting to GPT-4 Open AI LLM################################################################

            print("Establishing connection with GPT-4 Azure OpenAI LLM.")
            os.environ["OPENAI_API_VERSION"]      = AZURE_OPENAI_API_VERSION
            os.environ["AZURE_OPENAI_ENDPOINT"]   = AZURE_OPENAI_ENDPOINT
            os.environ["AZURE_OPENAI_API_KEY"]    = AZURE_OPENAI_API_KEY
            llm = AzureChatOpenAI(
                                     deployment_name = deployment_name,
                                     temperature=0.0
                                 )
            print("Established connection with GPT-4 Azure OpenAI LLM.")
    
        #############################################################Fetching Open AI Embeddings##############################################################################################
            print("Fetching GPT-4 OpenAI Embeddings.")            
            embeddings_model = AzureOpenAIEmbeddings(
                                                        model              = "text-embedding-ada-002",
                                                        azure_endpoint     = AZURE_OPENAI_ENDPOINT,
                                                        api_key            = AZURE_OPENAI_API_KEY,
                                                        openai_api_version = AZURE_OPENAI_API_VERSION_EMBEDDING
                                                    )
            print("Fetched with GPT-4 OpenAI Embeddings.")
        #############################################################Connecting to Azure AI Search################################################################
            AZURE_COGNITIVE_SEARCH_SERVICE_NAME     = os.getenv("AZURE_COGNITIVE_SEARCH_SERVICE_NAME")
            AZURE_COGNITIVE_SEARCH_API_KEY          = os.getenv("AZURE_COGNITIVE_SEARCH_API_KEY")
            AZURE_COGNITIVE_SEARCH_INDEX_NAME       = os.getenv("AZURE_COGNITIVE_SEARCH_INDEX_NAME")
            AZURE_COGNITIVE_SEARCH_SERVICE_ENDPOINT =  f"https://{AZURE_COGNITIVE_SEARCH_SERVICE_NAME}.search.windows.net"
            print("Initializing Azure Search.")
            Azure_Client = AzureSearch(
                                            azure_search_endpoint = AZURE_COGNITIVE_SEARCH_SERVICE_ENDPOINT,
                                            azure_search_key      = AZURE_COGNITIVE_SEARCH_API_KEY,
                                            index_name            = AZURE_COGNITIVE_SEARCH_INDEX_NAME,
                                            embedding_function    = embeddings_model.embed_query ,
                                    )
            print("AzureSearch client initialized successfully.")
        #############################################################Creating a Cart Log Entry################################################################################################
            table_action        = "insert"
            update_column       = None
            update_column_value = None
            cart_log_id         = None
            cart_log_id = self.database_activity_class_obj.cart_log_entry(conn,table_action,update_column,update_column_value,self.version,employee_id,cart_log_id = None)
            
        #############################################################Fetching Complaints from CFPB###########################################################################################
            cart_cfpb_complaints_raw_df = self.fetch_compalints_class_obj.get_cfpb_complaints(employee_id,cart_log_id,date_received_min,date_received_max,company,size)
            
        #############################################################Loading CFPB COmplaints#################################################################################################
            cart_cfpb_complaints_raw_table = 'cart_cfpb_complaints_raw_stage'
            self.database_activity_class_obj.load_cfpb_raw_complaints(conn,cart_cfpb_complaints_raw_df,cart_cfpb_complaints_raw_table)
            
        #############################################################Generating Untagged Complaints###########################################################################################
            untagged_complaints_stored_procedure = '[dbo].[uspload_cart_untagged_complaints]'
            self.database_activity_class_obj.generate_untagged_complaints(conn,untagged_complaints_stored_procedure)
            
            untagged_complaints_table  = 'cart_untagged_complaints'
            untagged_complaints_df     = self.database_activity_class_obj.import_untagged_complaints(conn,untagged_complaints_table)

        #####################################################Ingesting Regulation Data into Vector Stores#####################################################################################
            chunk_size    = 1000
            chunk_overlap = 200
            self.regulation_ingestion_class_obj.ingest_regulation_files(Azure_Client , self.regulation_ingestion_dict, self.regulations_path, chunk_size, chunk_overlap)

        #############################################################Classifying Complaints###################################################################################################
            complaints_id_field           = "Complaint_ID"
            complaints_text_field         = 'Complaint_Text' 
            tagged_complaints_final_df    = self.get_classified_complaints(Azure_Client,employee_id,untagged_complaints_df,embeddings_model,llm,complaints_id_field,complaints_text_field,cart_log_id)
            
        #############################################################Loading Tagged Complaints################################################################################################
            tagged_complaints_stage_table = '[dbo].[cart_cfpb_complaints_reg_stage]'
            self.database_activity_class_obj.load_tagged_complaints(conn, tagged_complaints_final_df, tagged_complaints_stage_table)
            
        #############################################################Updating CART Log Entry################################################################################################
            self.database_activity_class_obj.update_cart_log(conn,tagged_complaints_final_df,cart_log_id,self.regulation_ingestion_dict,self.version,employee_id)
        else:
           print("You do not have the permissions to use the Complaints Analysis and Regulation Tool.")
       

        conn.close()
        print("Connection to the CART Database in SQL Server has been closed.")
        elapsed_time = (time.time() - start_time) / 60
        print('Time taken to run this code {} mins'.format(elapsed_time))
        print('####################################################################################################################################################')
        print('############################### Thank you for using the Complaints Analysis and Regulation Tool !!!!!!!!!! #########################################')
        print('####################################################################################################################################################')
        return None
    
if __name__ == "__main__":
    cart_intersect_class_obj = cart_intersect_class()
    employee_id = 'c6400'
    size = 10
    date_received_min = "2023-03-01"
    date_received_max = "2023-3-31"
    company = "JPMORGAN CHASE & CO."
    from_value = 0
    cart_intersect_class_obj.run_cart(employee_id,date_received_min,date_received_max,company,size)
    #https://www.coursera.org/enroll/learn/team-building-and-leadership-in-project-management/paidmedia?specialization=microsoft-project-management#outcomes

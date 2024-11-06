import pandas as pd
import json



class classify_complaints_class:
    
    def classify_complaint(self, complaint_text, chain):
        try:
            # Invoke the chain and fetch the response content
            response_content = chain.invoke(complaint_text).content
            # Check if the response content is empty or None
            if not response_content:
                #print("Warning: Empty response content received.")
                return None, "No explanation available (empty response)"
            # Try parsing the JSON response
            response = json.loads(response_content)
            # Ensure expected keys are in the response
            if "Answer" not in response or "Explanation" not in response:
                #print("Warning: Missing 'Answer' or 'Explanation' in response:", response)
                return None, "No explanation available (incomplete response)"
            # Determine the answer based on the 'Answer' field
            if response['Answer'].lower() == "yes":
                answer = 1
            elif response['Answer'].lower() == "no":
                answer = 0
            else:
                answer = None
            regulation_explanation = response["Explanation"]
            return answer, regulation_explanation
        except json.JSONDecodeError as e:
            #print("JSON decode error:", e)
            #print("Invalid response content:", response_content)
            return None, "No explanation available (invalid JSON format)"
        except Exception as e:
            #print("Error during complaint classification:", e)
            return None, "No explanation available (unexpected error)"
    
    def tag_complaints(self,complaints_df,reg_name,complaints_id_field,complaints_text_field,chain):
        print("Tagging complaints with {}.".format(reg_name))
        reg_name_explanation                           = reg_name+ "_Explanation"
        complaints_df[[reg_name,reg_name_explanation]] = complaints_df[complaints_text_field].apply(lambda x: pd.Series(self.classify_complaint(x, chain)))
        complaints_df                                  = complaints_df.loc[:,[complaints_id_field,reg_name,reg_name_explanation]]
        print("Completed tagging complaints with {}.".format(reg_name))
        return complaints_df
    


# if __name__ == "__main__":
#     cart_path         = r'C:\GenAI\CART'
#     regulations_path  = cart_path + '\\regulations'
#     vector_db_path    = cart_path + '\\vector_db\\'
#     employee_id       = "c6400" #getpass.getuser()
#     version           = 1.0
#     complaints_id_field = "Complaint_ID"
#     complaints_text_field  = 'Complaint_Text' 
    
#     from langchain_openai import OpenAIEmbeddings, ChatOpenAI
#     key       =  
#     llm       =  ChatOpenAI(openai_api_key = key,model_name = "gpt-4", temperature = 0.0)
#     embedding_function  = OpenAIEmbeddings(api_key = key)
    
#     import pyodbc
#     server    = 'DESKTOP-VONKKUH'  # e.g., 'localhost\SQLEXPRESS'
#     database  = 'CART'  # e.g., 'CART_DB'
#     driver    = '{ODBC Driver 17 for SQL Server}'  # Ensure you have the correct ODBC driver installed
#     conn      = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;')

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
    
#     from regulation_text_ingestion import regulation_ingestion_class
#     regulation_ingestion_class_obj = regulation_ingestion_class()
#     regulation_ingestion_dict =   {
#                                     'Reg_B':True,
#                                     'Reg_C':True,
#                                     'Reg_D':True,
#                                     'Reg_E':True,
#                                     'Reg_F':True,
#                                     'Reg_G':True,
#                                     'Reg_H':True,
#                                     'Reg_I':True,
#                                     'Reg_J':True,
#                                     'Reg_K':True,
#                                     'Reg_L':True,
#                                     'Reg_M':True,
#                                     'Reg_N':True,
#                                     'Reg_O':True,
#                                     'Reg_P':True,
#                                     'Reg_V':True,
#                                     'Reg_X':True,
#                                     'Reg_Z':True,
#                                     'Reg_CC':True,
#                                     'Reg_DD':True,
#                                     'Reg_AA':True
#                                     }
                
#     regulation_ingestion_class_obj.ingest_regulation_files(embedding_function,regulation_ingestion_dict, regulations_path, vector_db_path, chunk_size = 1000, chunk_overlap = 200)
    
#     from prompt_retriever_chain_formation import regulation_prompt_retriever_chain_class
    
#     regulation_prompt_retriever_chain_class_obj = regulation_prompt_retriever_chain_class()
#     classify_complaints_class_obj = classify_complaints_class()
    

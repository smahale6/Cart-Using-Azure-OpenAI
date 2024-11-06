from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough


class regulation_prompt_retriever_chain_class:
    
    def get_prompt(self,reg_name):
        print("Generating the prompt for {}".format(reg_name))
        if reg_name == 'Reg_AA':
            prompt_template = """
                                You are an expert in CFPB regulations. Given data is the context of Regulation AA, Unfair or Deceptive Acts or Practices.
                                Context:{context}
                                Does the following complaint fall under Regulation AA, Unfair or Deceptive Acts or Practices? 
                                Complaint:"{complaint}"       
        
                                Answer with 'Yes' or 'No'. 
        
                                Provide an explanation.The explaination should be based on the context. Make sure the explanation ends in four or less that four sentences.
                                Explanation:
                                
                                Please return the answer in the following dictionary format:
                                {{"Answer": "Yes" or "No", "Explanation": "Your explanation here."}}

                                Do not return anything except the dictionary. Strictly a dictionary.
                             """   
            
        elif reg_name == 'Reg_B':
            prompt_template = """
                                You are an expert in CFPB regulations. Given data is the context of Regulation B, Equal Credit Opportunity Act - ECOA.
                                Context:{context}
                                 Does the following complaint fall under Regulation B, Equal Credit Opportunity Act - ECOA? 
                                Complaint:"{complaint}"       
                
                                Answer with 'Yes' or 'No'. 
                
                                Provide an explanation. The explanation should be based on the context. Make sure the explanation ends in four or less than four sentences.
                                Explanation:
                                
                                Please return the answer in the following dictionary format:
                                {{"Answer": "Yes" or "No", "Explanation": "Your explanation here."}}

                                Do not return anything except the dictionary. Strictly a dictionary.
                             """
                     
        elif reg_name == 'Reg_C':
            prompt_template = """
                                You are an expert in CFPB regulations. Given data is the context of Regulation C, Home Mortgage Disclosure Act - HMDA.
                                Context:{context}
                                Does the following complaint fall under Regulation C, Home Mortgage Disclosure Act - HMDA? 
                                Complaint:"{complaint}"       
        
                                Answer with 'Yes' or 'No'. 
        
                                Provide an explanation.The explaination should be based on the context. Make sure the explanation ends in four or less that four sentences.
                                Explanation:
                                
                                Please return the answer in the following dictionary format:
                                {{"Answer": "Yes" or "No", "Explanation": "Your explanation here."}}

                                Do not return anything except the dictionary. Strictly a dictionary.
                             """
                     
        elif reg_name == 'Reg_CC':
            prompt_template = """
                                You are an expert in CFPB regulations. Given data is the context of Regulation CC, Availability of Funds and Collection of Checks.
                                Context:{context}
                                Does the following complaint fall under Regulation CC, Availability of Funds and Collection of Checks? 
                                Complaint:"{complaint}"       
                
                                Answer with 'Yes' or 'No'. 
                
                                Provide an explanation. The explanation should be based on the context. Make sure the explanation ends in four or less than four sentences.
                                Explanation:
                                
                                Please return the answer in the following dictionary format:
                                {{"Answer": "Yes" or "No", "Explanation": "Your explanation here."}}

                                Do not return anything except the dictionary. Strictly a dictionary.
                             """
                     
                     
        elif reg_name == 'Reg_D':
            prompt_template = """
                                You are an expert in CFPB regulations. Given data is the context of Regulation D, Alternative Mortgage Transaction Parity Act.
                                Context:{context}
                                Does the following complaint fall under Regulation D,  Alternative Mortgage Transaction Parity Act? 
                                Complaint:"{complaint}"       
        
                                Answer with 'Yes' or 'No'. 
        
                                Provide an explanation.The explaination should be based on the context. Make sure the explanation ends in four or less that four sentences.
                                Explanation:
                                
                                Please return the answer in the following dictionary format:
                                {{"Answer": "Yes" or "No", "Explanation": "Your explanation here."}}

                                Do not return anything except the dictionary. Strictly a dictionary.
                             """
                     
        elif reg_name == 'Reg_DD':
            prompt_template = """
                                You are an expert in CFPB regulations. Given data is the context of Regulation DD, Truth in Savings Act - TISA.
                                Context:{context}
                                Does the following complaint fall under Regulation DD, Truth in Savings Act - TISA? 
                                Complaint:"{complaint}"       
                
                                Answer with 'Yes' or 'No'. 
                
                                Provide an explanation. The explanation should be based on the context. Make sure the explanation ends in four or less than four sentences.
                                Explanation:
                                
                                Please return the answer in the following dictionary format:
                                {{"Answer": "Yes" or "No", "Explanation": "Your explanation here."}}

                                Do not return anything except the dictionary. Strictly a dictionary.
                             """
                     
        elif reg_name == 'Reg_E':
            prompt_template = """
                                You are an expert in CFPB regulations. Given data is the context of Regulation E, Electronic Fund Transfer Act - EFTA.
                                Context:{context}
                                Does the following complaint fall under Regulation E, Electronic Fund Transfer Act - EFTA? 
                                Complaint:"{complaint}"       
                
                                Answer with 'Yes' or 'No'. 
                
                                Provide an explanation. The explanation should be based on the context. Make sure the explanation ends in four or less than four sentences.
                                Explanation:
                                
                                Please return the answer in the following dictionary format:
                                {{"Answer": "Yes" or "No", "Explanation": "Your explanation here."}}

                                Do not return anything except the dictionary. Strictly a dictionary.
                             """
                     
        elif reg_name == 'Reg_F':
            prompt_template = """
                                You are an expert in CFPB regulations. Given data is the context of Regulation F, Fair Debt Collection Practices Act - FDCPA.
                                Context:{context}
                                Does the following complaint fall under Regulation F, Fair Debt Collection Practices Act - FDCPA? 
                                Complaint:"{complaint}"       
                
                                Answer with 'Yes' or 'No'. 
                
                                Provide an explanation. The explanation should be based on the context. Make sure the explanation ends in four or less than four sentences.
                                Explanation:
                                
                                Please return the answer in the following dictionary format:
                                {{"Answer": "Yes" or "No", "Explanation": "Your explanation here."}}

                                Do not return anything except the dictionary. Strictly a dictionary.
                             """

                     
        elif reg_name == 'Reg_G':
            prompt_template = """
                                You are an expert in CFPB regulations. Given data is the context of Regulation G, S.A.F.E. Mortgage Licensing Act – Federal Registration of Residential Mortgage Loan Originators.
                                Context:{context}
                                Does the following complaint fall under Regulation G, S.A.F.E. Mortgage Licensing Act – Federal Registration of Residential Mortgage Loan Originators? 
                                Complaint:"{complaint}"       
                    
                                Answer with 'Yes' or 'No'. 
                    
                                Provide an explanation. The explanation should be based on the context. Make sure the explanation ends in four or less than four sentences.
                                Explanation:
                                
                                Please return the answer in the following dictionary format:
                                {{"Answer": "Yes" or "No", "Explanation": "Your explanation here."}}

                                Do not return anything except the dictionary. Strictly a dictionary.
                             """
                     
        elif reg_name == 'Reg_H':
            prompt_template = """
                                You are an expert in CFPB regulations. Given data is the context of Regulation H, S.A.F.E. Mortgage Licensing Act – State Compliance and Bureau Registration System.
                                Context:{context}
                                Does the following complaint fall under Regulation H, SS.A.F.E. Mortgage Licensing Act – State Compliance and Bureau Registration System? 
                                Complaint:"{complaint}"       
                
                                Answer with 'Yes' or 'No'. 
                
                                Provide an explanation. The explanation should be based on the context. Make sure the explanation ends in four or less than four sentences.
                                Explanation:
                                
                                Please return the answer in the following dictionary format:
                                {{"Answer": "Yes" or "No", "Explanation": "Your explanation here."}}

                                Do not return anything except the dictionary. Strictly a dictionary.
                             """
                     
        elif reg_name == 'Reg_I':
            prompt_template = """
                                You are an expert in CFPB regulations. Given data is the context of Regulation I, Disclosure Requirements for Depository Institutions Lacking Federal Deposit Insurance.
                                Context:{context}
                                Does the following complaint fall under Regulation I, Disclosure Requirements for Depository Institutions Lacking Federal Deposit Insurance? 
                                Complaint:"{complaint}"       
                
                                Answer with 'Yes' or 'No'. 
                
                                Provide an explanation. The explanation should be based on the context. Make sure the explanation ends in four or less than four sentences.
                                Explanation:
                                
                                Please return the answer in the following dictionary format:
                                {{"Answer": "Yes" or "No", "Explanation": "Your explanation here."}}

                                Do not return anything except the dictionary. Strictly a dictionary.
                             """
                     
        elif reg_name == 'Reg_J':
            prompt_template = """
                                You are an expert in CFPB regulations. Given data is the context of Regulation J, Land Sales Registration.
                                Context:{context}
                                Does the following complaint fall under Regulation J, Land Sales Registration? 
                                Complaint:"{complaint}"       
                    
                                Answer with 'Yes' or 'No'. 
                    
                                Provide an explanation. The explanation should be based on the context. Make sure the explanation ends in four or less than four sentences.
                                Explanation:
                                
                                Please return the answer in the following dictionary format:
                                {{"Answer": "Yes" or "No", "Explanation": "Your explanation here."}}

                                Do not return anything except the dictionary. Strictly a dictionary.
                             """
                     
        elif reg_name == 'Reg_K':
            prompt_template = """
                                   You are an expert in CFPB regulations. Given data is the context of Regulation K, Purchasers’ Revocation Rights, Sales Practices and Standards.
                                   Context:{context}
                                   Does the following complaint fall under Regulation K, Purchasers’ Revocation Rights, Sales Practices and Standards? 
                                   Complaint:"{complaint}"       
                   
                                   Answer with 'Yes' or 'No'. 
                   
                                   Provide an explanation. The explanation should be based on the context. Make sure the explanation ends in four or less than four sentences.
                                   Explanation:
                                   
                                   Please return the answer in the following dictionary format:
                                   {{"Answer": "Yes" or "No", "Explanation": "Your explanation here."}}

                                   Do not return anything except the dictionary. Strictly a dictionary.
                                """
                                 
        elif reg_name == 'Reg_L':
            prompt_template = """
                                You are an expert in CFPB regulations. Given data is the context of Regulation L, Protection of Nonpublic Personal Information.
                                Context:{context}
                                Does the following complaint fall under Regulation L, Protection of Nonpublic Personal Information? 
                                Complaint:"{complaint}"       
                
                                Answer with 'Yes' or 'No'. 
                
                                Provide an explanation. The explanation should be based on the context. Make sure the explanation ends in four or less than four sentences.
                                Explanation:
                                
                                Please return the answer in the following dictionary format:
                                {{"Answer": "Yes" or "No", "Explanation": "Your explanation here."}}

                                Do not return anything except the dictionary. Strictly a dictionary.
                             """
                     
        elif reg_name == 'Reg_M':
            prompt_template = """
                                You are an expert in CFPB regulations. Given data is the context of Regulation M, Consumer Leasing Act.
                                Context:{context}
                                Does the following complaint fall under Regulation M, Consumer Leasing Act? 
                                Complaint:"{complaint}"       
                
                                Answer with 'Yes' or 'No'. 
                
                                Provide an explanation. The explanation should be based on the context. Make sure the explanation ends in four or less than four sentences.
                                Explanation:
                                
                                Please return the answer in the following dictionary format:
                                {{"Answer": "Yes" or "No", "Explanation": "Your explanation here."}}

                                Do not return anything except the dictionary. Strictly a dictionary.
                             """
                     
        elif reg_name == 'Reg_N':
            prompt_template = """
                                You are an expert in CFPB regulations. Given data is the context of Regulation N, Mortgage Acts and Practices - Advertising Rule).
                                Context:{context}
                                Does the following complaint fall under Regulation N, Mortgage Acts and Practices - Advertising Rule)? 
                                Complaint:"{complaint}"       
                
                                Answer with 'Yes' or 'No'. 
                
                                Provide an explanation. The explanation should be based on the context. Make sure the explanation ends in four or less than four sentences.
                                Explanation:
                                
                                Please return the answer in the following dictionary format:
                                {{"Answer": "Yes" or "No", "Explanation": "Your explanation here."}}

                                Do not return anything except the dictionary. Strictly a dictionary.
                             """
                     
        elif reg_name == 'Reg_O':
            prompt_template = """
                                You are an expert in CFPB regulations. Given data is the context of Regulation O, Mortgage Assistance Relief Services - MARS Rule.
                                Context:{context}
                                Does the following complaint fall under Regulation O, Mortgage Assistance Relief Services - MARS Rule? 
                                Complaint:"{complaint}"       
                
                                Answer with 'Yes' or 'No'. 
                
                                Provide an explanation. The explanation should be based on the context. Make sure the explanation ends in four or less than four sentences.
                                Explanation:
                                
                                Please return the answer in the following dictionary format:
                                {{"Answer": "Yes" or "No", "Explanation": "Your explanation here."}}

                                Do not return anything except the dictionary. Strictly a dictionary.
                             """
                     
        elif reg_name == 'Reg_P':
            prompt_template = """
                                You are an expert in CFPB regulations. Given data is the context of Regulation P, Privacy of Consumer Financial Information.
                                Context:{context}
                                Does the following complaint fall under Regulation P, Privacy of Consumer Financial Information? 
                                Complaint:"{complaint}"        
        
                                Answer with 'Yes' or 'No'. 
        
                                Provide an explanation.The explaination should be based on the context. Make sure the explanation ends in four or less that four sentences.
                                Explanation:
                                
                                Please return the answer in the following dictionary format:
                                {{"Answer": "Yes" or "No", "Explanation": "Your explanation here."}}
                             """
                     
        elif reg_name == 'Reg_V':
            prompt_template = """
                                You are an expert in CFPB regulations. Given data is the context of Regulation V, Fair Credit Reporting Act - FCRA.
                                Context:{context}
                                Does the following complaint fall under Regulation V, Fair Credit Reporting Act - FCRA? 
                                Complaint:"{complaint}"       
                
                                Answer with 'Yes' or 'No'. 
                
                                Provide an explanation. The explanation should be based on the context. Make sure the explanation ends in four or less than four sentences.
                                Explanation:
                                
                                Please return the answer in the following dictionary format:
                                {{"Answer": "Yes" or "No", "Explanation": "Your explanation here."}}

                                Do not return anything except the dictionary. Strictly a dictionary.
                             """
        
        elif reg_name == 'Reg_X':
            prompt_template = """
                                You are an expert in CFPB regulations. Given data is the context of Regulation X, Real Estate Settlement Procedures Act - RESPA.
                                Context:{context}
                                Does the following complaint fall under Regulation X, Real Estate Settlement Procedures Act - RESPA? 
                                Complaint:"{complaint}"       
                
                                Answer with 'Yes' or 'No'. 
                
                                Provide an explanation. The explanation should be based on the context. Make sure the explanation ends in four or less than four sentences.
                                Explanation:
                                
                                Please return the answer in the following dictionary format:
                                {{"Answer": "Yes" or "No", "Explanation": "Your explanation here."}}

                                Do not return anything except the dictionary. Strictly a dictionary.
                             """
        
        elif reg_name == 'Reg_Z':
            prompt_template = """
                                You are an expert in CFPB regulations. Given data is the context of Regulation Z, Truth in Lending Act - TILA.
                                Context:{context}
                                Does the following complaint fall under Regulation Z, Truth in Lending Act - TILA? 
                                Complaint:"{complaint}"       
                
                                Answer with 'Yes' or 'No'. 
                
                                Provide an explanation. The explanation should be based on the context. Make sure the explanation ends in four or less than four sentences.
                                Explanation:
                                
                                Please return the answer in the following dictionary format:
                                {{"Answer": "Yes" or "No", "Explanation": "Your explanation here."}}

                                Do not return anything except the dictionary. Strictly a dictionary.
                             """
                     
        regulation_prompt = PromptTemplate(template=prompt_template, input_variables=["context", "complaint"])
        print("Generated the prompt for {}".format(reg_name))
        return regulation_prompt
            
    
    def get_retriever(self,Azure_Client,reg_name,embeddings_model):
        print("Creating a retriever for {}.".format(reg_name))
        reg_name_modified = reg_name.replace('_',' ')
        search_kwargs_filter = "regulation_name eq '{}'".format(reg_name_modified)
        retriever = Azure_Client.as_retriever(search_type="similarity", search_kwargs={"filter": search_kwargs_filter})
        print("Created a retriever for {}.".format(reg_name))
        return retriever

    def chain_formation(self,regulation_prompt,retriever,llm,reg_name):
        print("Creating a chain for {}.".format(reg_name))
        chain = (
                    {"context": retriever,"complaint": RunnablePassthrough()}
                    | regulation_prompt
                    | llm
                )
        print("Created a chain for {}.".format(reg_name))
        return chain
                 
            
# if __name__ == "__main__":
#     cart_path         = r'C:\GenAI\CART'
#     regulations_path  = cart_path + '\\regulations'
#     vector_db_path    = cart_path + '\\vector_db\\'
#     employee_id       = "c6400" #getpass.getuser()
#     version           = 1.0
    
#     from langchain_openai import OpenAIEmbeddings, ChatOpenAI
#     key       =  
#     llm       =  ChatOpenAI(openai_api_key = key,model_name = "gpt-4", temperature = 0.0)
#     embedding_function  = OpenAIEmbeddings(api_key = key)
    
#     import pyodbc
#     server    = 'DESKTOP-VONKKUH'  # e.g., 'localhost\SQLEXPRESS'
#     database  = 'CART'  # e.g., 'CART_DB'
#     driver    = '{ODBC Driver 17 for SQL Server}'  # Ensure you have the correct ODBC driver installed
#     conn      = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;')

# #     print("Initializing Azure Search.")

# #     Azure_Client = AzureSearch(
# #                                      azure_search_endpoint = AZURE_COGNITIVE_SEARCH_SERVICE_ENDPOINT,
# #                                      azure_search_key      = AZURE_COGNITIVE_SEARCH_API_KEY,
# #                                      index_name            = AZURE_COGNITIVE_SEARCH_INDEX_NAME,
# #                                      embedding_function    = embeddings_model.embed_query ,
# #                               )
    
# #     print("AzureSearch client initialized successfully.")
    
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
    
#     #vector_stores = regulation_ingestion_class_obj.ingest_regulation_files(Azure_Client , regulation_ingestion_dict, regulations_path, chunk_size = 1000, chunk_overlap = 200)
        
#     regulation_prompt_retriever_chain_class_obj = regulation_prompt_retriever_chain_class()
#     for reg_name in regulation_ingestion_dict.keys():
#         regulation_prompt = regulation_prompt_retriever_chain_class_obj.get_prompt(reg_name)
#         retriever = regulation_prompt_retriever_chain_class_obj.get_retriever(Azure_Client,reg_name,embedding_function)
#         chain = regulation_prompt_retriever_chain_class_obj.chain_formation(regulation_prompt,retriever,llm,reg_name)
    

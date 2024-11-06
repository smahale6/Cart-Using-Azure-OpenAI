import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

import warnings
warnings.filterwarnings('ignore')

class database_activity_class:
    
    def cart_log_entry(self,conn,table_action,update_column,update_column_value,version,employee_id,cart_log_id = None):
        if table_action == 'insert':
            print("Generating the Cart Log Id for this run.")
            cart_log_df = pd.read_sql("select * from dbo.cart_log",conn)
            if len(cart_log_df) == 0:
                cart_log_id = 1000
            else:
                cart_log_df = pd.read_sql("select max(Cart_Log_Id) as Cart_Log_Id from dbo.cart_log",conn)
                cart_log_id    = cart_log_df.loc[0,'Cart_Log_Id'] + 1
            print("The Cart Log Id for this run is {}.".format(cart_log_id))
            cart_log                                 = pd.DataFrame([{'Cart_Log_Id':cart_log_id,
                                                                      'Version':version}])
            cart_log['Cart_Log_Status']              = 'Incomplete'
            cart_log['Total_Complaints']             = 0
            cart_log['Reg_B_Count']                  = 0
            cart_log['Reg_C_Count']                  = 0
            cart_log['Reg_D_Count']                  = 0
            cart_log['Reg_E_Count']                  = 0
            cart_log['Reg_F_Count']                  = 0
            cart_log['Reg_G_Count']                  = 0
            cart_log['Reg_H_Count']                  = 0
            cart_log['Reg_I_Count']                  = 0
            cart_log['Reg_J_Count']                  = 0
            cart_log['Reg_K_Count']                  = 0
            cart_log['Reg_L_Count']                  = 0
            cart_log['Reg_M_Count']                  = 0
            cart_log['Reg_N_Count']                  = 0
            cart_log['Reg_O_Count']                  = 0
            cart_log['Reg_P_Count']                  = 0
            cart_log['Reg_V_Count']                  = 0
            cart_log['Reg_X_Count']                  = 0
            cart_log['Reg_Z_Count']                  = 0
            cart_log['Reg_CC_Count']                 = 0
            cart_log['Reg_DD_Count']                 = 0
            cart_log['Reg_AA_Count']                 = 0
            cart_log['Tagged_By']                    = employee_id
            cart_log['Log_Date']                     = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            print("Creating a new log record for the cart log id {}.".format(cart_log_id))
            cursor = conn.cursor()
            for index, row in cart_log.iterrows():
                cursor.execute("SET IDENTITY_INSERT dbo.cart_log ON")
                cursor.execute("INSERT INTO dbo.cart_log (Cart_Log_Id,Version,Cart_Log_Status,Total_Complaints,Reg_B_Count,Reg_C_Count,Reg_D_Count,Reg_E_Count,Reg_F_Count,Reg_G_Count,Reg_H_Count,Reg_I_Count,Reg_J_Count,Reg_K_Count,Reg_L_Count,Reg_M_Count,Reg_N_Count,Reg_O_Count,Reg_P_Count,Reg_V_Count,Reg_X_Count,Reg_Z_Count,Reg_CC_Count,Reg_DD_Count,Reg_AA_Count,Tagged_By,Log_Date)values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", row.Cart_Log_Id,row.Version,row.Cart_Log_Status,row.Total_Complaints,row.Reg_B_Count,row.Reg_C_Count,row.Reg_D_Count,row.Reg_E_Count,row.Reg_F_Count,row.Reg_G_Count,row.Reg_H_Count,row.Reg_I_Count,row.Reg_J_Count,row.Reg_K_Count,row.Reg_L_Count,row.Reg_M_Count,row.Reg_N_Count,row.Reg_O_Count,row.Reg_P_Count,row.Reg_V_Count,row.Reg_X_Count,row.Reg_Z_Count,row.Reg_CC_Count,row.Reg_DD_Count,row.Reg_AA_Count,row.Tagged_By,row.Log_Date)
                cursor.execute("SET IDENTITY_INSERT dbo.cart_log OFF")
            conn.commit()
            cursor.close()
            # bat_run_log.to_sql(con=conn, schema=self.sql_database_schema,if_exists='append', name="bat_run_log", index=False, chunksize=1000)
            print("Completed creating a new log record for the log_id {}.".format(cart_log_id))
            return cart_log_id
        elif table_action == 'update' and type(update_column_value) == str:
            print("Updating the column {} in the dbo.cart_log table.".format(update_column))
            cursor = conn.cursor()
            cursor.execute("Update dbo.cart_log set {} = '{}' where cart_log_id = {}".format(update_column,update_column_value,cart_log_id))
            conn.commit()
            cursor.close()
            print("Completed updating the column {} in the dbo.cart_log table.".format(update_column))
            return None
        elif table_action == 'update' and type(update_column_value) == int:
            print("Updating the column {} in the dbo.cart_log table.".format(update_column))
            cursor = conn.cursor()
            cursor.execute("Update dbo.cart_log set {} = {} where cart_log_id = {}".format(update_column,update_column_value,cart_log_id))
            conn.commit()
            cursor.close()
            print("Completed updating the column {} in the dbo.cart_log table.".format(update_column))
            return None
        
    def load_cfpb_raw_complaints(self,conn, cart_cfpb_complaints_raw_df, cart_cfpb_complaints_raw_table="cart_cfpb_complaints_raw_stage"):
        print(f"Loading data into {cart_cfpb_complaints_raw_table}.")
        # Create a cursor from the pyodbc connection
        cursor = conn.cursor()
        # Step 1: Truncate the table
        cursor.execute(f"TRUNCATE TABLE dbo.{cart_cfpb_complaints_raw_table}")
        conn.commit()
        print(f"Truncated table {cart_cfpb_complaints_raw_table}.")
        # Step 2: Insert DataFrame data in chunks
        for i in range(0, len(cart_cfpb_complaints_raw_df), 1000):
            chunk = cart_cfpb_complaints_raw_df[i:i + 1000]
            # Define columns and placeholders
            columns = ", ".join(chunk.columns)
            placeholders = ", ".join(["?"] * len(chunk.columns))
            insert_query = f"INSERT INTO dbo.{cart_cfpb_complaints_raw_table} ({columns}) VALUES ({placeholders})"
            # Convert rows to list of tuples for executemany
            data = [tuple(row) for row in chunk.itertuples(index=False, name=None)]
            # Execute the batch insert
            cursor.executemany(insert_query, data)
            conn.commit()
        print(f"Data loaded into {cart_cfpb_complaints_raw_table} successfully.")
        # Step 3: Execute the stored procedure
        cursor.execute("EXEC dbo.uspload_cart_cfpb_complaints_raw")
        conn.commit()
        print("Executed stored procedure dbo.uspload_cart_cfpb_complaints_raw.")
        # Close the cursor
        cursor.close()
        return None
        
    def generate_untagged_complaints(self,conn,stored_procedure = '[dbo].[uspload_cart_untagged_complaints]'):
        print("Fetching untagged complaints.")
        cursor = conn.cursor() # Creating a cursor object
        cursor.execute("Execute {}".format(stored_procedure))
        conn.commit()  # Commit the transaction if the stored procedure modifies data
        print("Completed fetching untagged complaints.")           
        return None
    
    def import_untagged_complaints(self,conn,untagged_complaints_table = '[dbo].[cart_untagged_complaints]'):
        # Fetching the untagged complaints
        print("Importing the untagged complaints from {} table.".format(untagged_complaints_table))
        untagged_complaints_df = pd.read_sql('Select * from {}'.format(untagged_complaints_table),conn)
        print("Completed importing the untagged complaints from {} table.".format(untagged_complaints_table))
        print("There are a total of {} complaints that needs to be mapped with regulation(s).".format(len(untagged_complaints_df)))
        return untagged_complaints_df
        
  
    def load_tagged_complaints(self, conn, tagged_complaints_final_df, tagged_complaints_stage_table="cart_cfpb_complaints_reg_stage"):
        print(f"Loading tagged complaints results from DataFrame to {tagged_complaints_stage_table} table in SQL Server.")
        # Step 1: Truncate the table
        cursor = conn.cursor()
        cursor.execute(f"TRUNCATE TABLE {tagged_complaints_stage_table}")
        conn.commit()
        print(f"Truncated table {tagged_complaints_stage_table}.")
        
        # Step 2: Insert DataFrame data in chunks
        for i in range(0, len(tagged_complaints_final_df), 1000):
            chunk = tagged_complaints_final_df[i:i + 1000]
            columns = ", ".join(chunk.columns)
            placeholders = ", ".join(["?"] * len(chunk.columns))
            insert_query = f"INSERT INTO {tagged_complaints_stage_table} ({columns}) VALUES ({placeholders})"
            data = [tuple(row) for row in chunk.itertuples(index=False, name=None)]
            cursor.executemany(insert_query, data)
            conn.commit()
        print(f"Data loaded into {tagged_complaints_stage_table} successfully.")
        
        # Step 3: Execute the stored procedure
        cursor.execute("EXEC dbo.uspload_cart_cfpb_complaints_reg")
        conn.commit()
        print("Executed stored procedure dbo.uspload_cart_cfpb_complaints_reg.")
        cursor.close()
        return None

    def update_cart_log(self,conn,tagged_complaints_final_df,cart_log_id,regulation_ingestion_dict,version,employee_id):
        for reg in regulation_ingestion_dict.keys():
            table_action = 'update'
            update_column = reg + '_Count'
            update_column_value = tagged_complaints_final_df.loc[:,reg].sum()
            self.cart_log_entry(conn,table_action,update_column,update_column_value,version,employee_id,cart_log_id)

        table_action = 'update'
        update_column       = 'Cart_Log_Status'
        update_column_value = 'Complete'
        self.cart_log_entry(conn,table_action,update_column,update_column_value,version,employee_id,cart_log_id)

        table_action = 'update'
        update_column       = 'Total_Complaints'
        update_column_value = len(tagged_complaints_final_df)
        self.cart_log_entry(conn,table_action,update_column,update_column_value,version,employee_id,cart_log_id)
        return None
        


# if __name__ == "__main__":
    # cart_path         = 'C:\GenAI\CART'
    # regulations_path  = cart_path  +'\regulatons'
    # employee_id       = "c6400" #getpass.getuser()
    # version           = 1.0
    
    # from langchain_openai import OpenAIEmbeddings, ChatOpenAI
    # key       =  
    # llm       =  ChatOpenAI(openai_api_key = key,model_name = "gpt-4", temperature = 0.0)
    # embedding_function  = OpenAIEmbeddings(api_key = key)
    
    # import pyodbc
    # server    = 'DESKTOP-VONKKUH'  # e.g., 'localhost\SQLEXPRESS'
    # database  = 'CART'  # e.g., 'CART_DB'
    # driver    = '{ODBC Driver 17 for SQL Server}'  # Ensure you have the correct ODBC driver installed
    # conn      = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;')

    # database_activity_class_obj = database_activity_class()  
    

    # table_action = "insert"
    # update_column = None
    # update_column_value = None
    # cart_log_id = None
    # database_activity_class_obj.cart_log_entry(conn,table_action,update_column,update_column_value,version,employee_id,cart_log_id = None)
    
    # stored_procedure = '[dbo].[uspload_cart_untagged_complaints]'
    # database_activity_class_obj.generate_untagged_complaints(conn,stored_procedure)
    
    # untagged_complaints_table = '[dbo].[cart_untagged_complaints]'
    # untagged_complaints_df = database_activity_class_obj.import_untagged_complaints(conn,untagged_complaints_table)


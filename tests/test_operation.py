import unittest
import os
from src.database_activity import database_activity_class
from src.regulation_text_ingestion import regulation_ingestion_class
from src.prompt_retriever_chain_formation import regulation_prompt_retriever_chain_class
from src.fetch_complaints_api import fetch_compalints_class
from src.classify_complaints import classify_complaints_class
import pandas as pd


class TestCART(unittest.TestCase):
    
    def setUp(self):
        # Instantiate all objects
        self.regulation_ingestion_class_obj = regulation_ingestion_class()
        self.database_activity_class_obj = database_activity_class()  
        self.regulation_prompt_retriever_chain_class_obj = regulation_prompt_retriever_chain_class()
        self.fetch_compalints_class_obj = fetch_compalints_class()
        self.classify_complaints_class_obj = classify_complaints_class()

    def test_database_connection(self):
        try:
            # Attempt to establish a connection using example credentials or environment variables
            conn = None
            SQL_USER_NAME = os.getenv("SQL_USER_NAME")
            SQL_PASSWORD = os.getenv("SQL_PASSWORD")
            
            # Assuming the database_activity_class has a method to create a connection
            conn = self.database_activity_class_obj.connect_to_database(SQL_USER_NAME, SQL_PASSWORD)
            
            # Check that the connection was successfully established
            self.assertIsNotNone(conn, "Failed to establish a database connection.")

            # Optional: Run a simple query to ensure the connection is functional
            cursor = conn.cursor()
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            
            # Verify that the query returns the expected result
            self.assertEqual(result[0], 1, "Database connection test query did not return expected result.")
            
            # Close the cursor and connection
            cursor.close()
            conn.close()

        except Exception as e:
            self.fail(f"Database connection test failed with exception: {e}")
    
    def test_create_cart_log_entry(self):
        try:
            # Assume the employee_id and version for the test
            employee_id = "test_employee"
            version = 1.0

            # Establish a database connection for the test
            SQL_USER_NAME = os.getenv("SQL_USER_NAME")
            SQL_PASSWORD = os.getenv("SQL_PASSWORD")
            conn = self.database_activity_class_obj.connect_to_database(SQL_USER_NAME, SQL_PASSWORD)

            # Step 1: Insert a new log entry
            cart_log_id = self.database_activity_class_obj.cart_log_entry(
                conn,
                table_action='insert',
                update_column=None,
                update_column_value=None,
                version=version,
                employee_id=employee_id
            )

            # Ensure a cart_log_id is returned
            self.assertIsNotNone(cart_log_id, "No cart_log_id was returned after creating a cart log entry.")

            # Step 2: Validate the new log entry in the database
            query = f"SELECT * FROM dbo.cart_log WHERE Cart_Log_Id = {cart_log_id}"
            cart_log_df = pd.read_sql(query, conn)

            # Check if the log entry exists
            self.assertEqual(len(cart_log_df), 1, f"No entry found for Cart_Log_Id {cart_log_id}")

            # Check if the log entry has the expected values
            self.assertEqual(cart_log_df.iloc[0]['Cart_Log_Id'], cart_log_id, "Cart_Log_Id does not match.")
            self.assertEqual(cart_log_df.iloc[0]['Tagged_By'], employee_id, "Employee ID does not match.")
            self.assertEqual(cart_log_df.iloc[0]['Version'], version, "Version does not match.")
            self.assertEqual(cart_log_df.iloc[0]['Cart_Log_Status'], 'Incomplete', "Log status is not 'Incomplete' as expected.")

        except Exception as e:
            self.fail(f"Cart log entry creation test failed with exception: {e}")

        finally:
            # Ensure the connection is closed after the test
            if conn:
                conn.close()
    

    def test_prompt_generation(self):
        # Test prompt generation for a known regulation, e.g., "Reg_AA"
        prompt = self.regulation_prompt_retriever_chain_class_obj.get_prompt("Reg_AA")
        
        # Check if the template includes the expected regulation context
        self.assertIn("Regulation AA", prompt.template, "Prompt template does not contain expected text for Regulation AA.")
        
        # Check if necessary placeholders are present
        self.assertIn("{context}", prompt.template, "Prompt template is missing the '{context}' placeholder.")
        self.assertIn("{complaint}", prompt.template, "Prompt template is missing the '{complaint}' placeholder.")
        
        # Test prompt generation for an unsupported regulation
        try:
            unsupported_prompt = self.regulation_prompt_retriever_chain_class_obj.get_prompt("Reg_UNKNOWN")
            # Assuming the method should raise an error or return None for unsupported regulations
            self.fail("Expected an error or None for unsupported regulation name.")
        except KeyError:
            # Expecting a KeyError if unsupported regulations are not handled within the method
            pass
        except Exception as e:
            self.fail(f"Unexpected exception for unsupported regulation: {e}")

    def test_fetch_complaints_valid(self):
        # Define parameters for a valid API request
        employee_id = "c6400"
        cart_log_id = 1234
        date_received_min = "2023-01-01"
        date_received_max = "2023-01-31"
        company = "JPMORGAN CHASE & CO."
        size = 10  # Limit the number of complaints for testing purposes

        # Fetch complaints with valid parameters
        response = self.fetch_compalints_class_obj.get_cfpb_complaints(
            employee_id, cart_log_id, date_received_min, date_received_max, company=company, size=size
        )
        
        # Check that the response is a DataFrame
        self.assertIsInstance(response, pd.DataFrame, "The response is not a DataFrame as expected.")

        # Check that the DataFrame is not empty (assuming data exists for the parameters used)
        self.assertGreater(len(response), 0, "The DataFrame is empty, but data was expected.")

        # Check that the DataFrame contains expected columns
        expected_columns = [
            "Date_received", "Product", "Sub_product", "Issue", "Sub_issue",
            "Consumer_complaint_narrative", "Company_public_response", "Company",
            "State", "ZIP_code", "Tags", "Consumer_consent_provided", "Submitted_via",
            "Date_sent_to_company", "Company_response_to_consumer", "Timely_response",
            "Consumer_disputed", "Complaint_ID", "Loaded_By", "Cart_Log_Id"
        ]
        
        # Verify each expected column is present in the DataFrame
        for column in expected_columns:
            self.assertIn(column, response.columns, f"Expected column '{column}' is missing from the response DataFrame.")
        
        # Optional: Check the data types of key columns if necessary
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(response["Date_received"]), "Date_received column is not datetime type.")
        self.assertTrue(pd.api.types.is_integer_dtype(response["Complaint_ID"]), "Complaint_ID column is not integer type.")

    
    # Add other test cases similarly...

if __name__ == "__main__":
    unittest.main()

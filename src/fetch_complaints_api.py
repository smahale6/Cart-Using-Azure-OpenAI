import requests
import pandas as pd


class fetch_compalints_class:
    def __init__(self):
        self.api_url = 'https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/'
    
    # Send GET request to the API
    def get_cfpb_complaints(self,employee_id,cart_log_id,date_received_min,date_received_max, company = "JPMORGAN CHASE & CO.",size = 500,from_value = 0):
        print("Fetching a total of {} complaints against {} logged from {} to {}.".format(size,company,date_received_max,date_received_min))
        params = {
                   "size":size,
                   "from": from_value,
                   "company": company,
                   "date_received_min":date_received_min,
                   "date_received_max": date_received_max
                 }
        
        # Send GET request to the API
        response = requests.get(self.api_url, params=params, verify=False)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            if 'hits' in data and 'hits' in data['hits']:
                complaints = data['hits']['hits']
        
                complaint_data = [] # store complaints stuff
        
                for complaint in complaints:
                    Date_received                 = complaint['_source'].get('date_received', None)
                    Product                       = complaint['_source'].get('product', None)
                    Sub_product                   = complaint['_source'].get('sub_product', None)
                    Issue                         = complaint['_source'].get('issue', None)
                    Sub_issue                     = complaint['_source'].get('Sub_issue', None)
                    Consumer_complaint_narrative  = complaint['_source'].get('complaint_what_happened', None)
                    Company_public_response       = complaint['_source'].get('company_public_response', None)
                    Company                       = complaint['_source'].get('company', None)
                    State                         = complaint['_source'].get('state', None)                       
                    ZIP_code                      = complaint['_source'].get('zip_code', None)
                    Tags                          = complaint['_source'].get('tags', None)
                    Consumer_consent_provided     = complaint['_source'].get('consumer_consent_provided', None)
                    Submitted_via                 = complaint['_source'].get('submitted_via', None)
                    Date_sent_to_company          = complaint['_source'].get('date_sent_to_company', None)
                    Company_response_to_consumer  = complaint['_source'].get('Company_response_to_consumer', None)
                    Timely_response               = complaint['_source'].get('timely', None)
                    Consumer_disputed             = complaint['_source'].get('consumer_disputed', None)
                    Complaint_ID                  = complaint['_id'] if '_id' in complaint else None
        
                    
        
                    complaint_data.append({
                                            "Date_received"                 :  Date_received,               
                                            "Product"                       :  Product,                     
                                            "Sub_product"                   :  Sub_product,                 
                                            "Issue"                         :  Issue,                       
                                            "Sub_issue"                     :  Sub_issue,                   
                                            "Consumer_complaint_narrative"  :  Consumer_complaint_narrative,
                                            "Company_public_response"       :  Company_public_response,     
                                            "Company"                       :  Company,                     
                                            "State"                         :  State,                       
                                            "ZIP_code"                      :  ZIP_code,                    
                                            "Tags"                          :  Tags,                        
                                            "Consumer_consent_provided"     :  Consumer_consent_provided,   
                                            "Submitted_via"                 :  Submitted_via,               
                                            "Date_sent_to_company"          :  Date_sent_to_company,        
                                            "Company_response_to_consumer"  :  Company_response_to_consumer,
                                            "Timely_response"               :  Timely_response,             
                                            "Consumer_disputed"             :  Consumer_disputed,           
                                            "Complaint_ID"                  :  Complaint_ID  
                                            })
        
                cart_cfpb_complaints_raw_df                = pd.DataFrame(complaint_data)
                cart_cfpb_complaints_raw_df['Loaded_By']   = employee_id
                cart_cfpb_complaints_raw_df['Cart_Log_Id'] = cart_log_id
            else:
                print("No hits found in the response")
        else:
            print(f"Error: {response.status_code}")
        return cart_cfpb_complaints_raw_df
    
# if __name__ == "__main__":
#     employee_id = 'c6400'
#     size = 10
#     date_received_min = "2023-01-01"
#     date_received_max = "2023-12-31"
#     company = "JPMORGAN CHASE & CO."
#     from_value = 0
#     fetch_compalints_class_obj = fetch_compalints_class()
#     cart_cfpb_complaints_raw_df = fetch_compalints_class_obj.get_cfpb_complaints(employee_id,date_received_min,date_received_max,company,size,from_value)
    
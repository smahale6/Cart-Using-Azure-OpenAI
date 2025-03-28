/****** Object:  StoredProcedure [dbo].[uspload_cart_cfpb_complaints_raw]    Script Date: 11/4/2024 11:25:59 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO


ALTER PROCEDURE [dbo].[uspload_cart_cfpb_complaints_raw]
As
BEGIN

--#########################################################Data Cleaning###############################################################
Drop Table If EXISTS #cart_cfpb_complaints_raw_stage
Select
       [Date_received]                 = Case when len(ltrim(rtrim([Date_received])))                > 0 Then cast([Date_received] as Date)                  Else null End                    
      ,[Product]                       = Case when len(ltrim(rtrim([Product])))                      > 0 Then ltrim(rtrim([Product]))                        Else null End  
      ,[Sub_product]                   = Case when len(ltrim(rtrim([Sub_product])))                  > 0 Then ltrim(rtrim([Sub_product]))                    Else null End  
      ,[Issue]                         = Case when len(ltrim(rtrim([Issue])))                        > 0 Then ltrim(rtrim([Issue]))                          Else null End
      ,[Sub_issue]                     = Case when len(ltrim(rtrim([Sub_issue])))                    > 0 Then ltrim(rtrim([Sub_issue]))                      Else null End
      ,[Consumer_complaint_narrative]  = [Consumer_complaint_narrative]
      ,[Company_public_response]       = Case when len(ltrim(rtrim([Company_public_response])))      > 0 Then ltrim(rtrim([Company_public_response]))        Else null End  
      ,[Company]                       = Case when len(ltrim(rtrim([Company])))                      > 0 Then ltrim(rtrim([Company]))                        Else null End  
      ,[State]                         = Case when len(ltrim(rtrim([State])))                        > 0 Then ltrim(rtrim([State]))                          Else null End
      ,[ZIP_code]                      = Case when len(ltrim(rtrim([ZIP_code])))                     > 0 Then ltrim(rtrim([ZIP_code]))                       Else null End
      ,[Tags]                          = Case when len(ltrim(rtrim([Tags])))                         > 0 Then ltrim(rtrim([Tags]))                           Else null End
      ,[Consumer_consent_provided]     = Case when len(ltrim(rtrim([Consumer_consent_provided])))    > 0 Then ltrim(rtrim([Consumer_consent_provided]))      Else null End
      ,[Submitted_via]                 = Case when len(ltrim(rtrim([Submitted_via])))                > 0 Then ltrim(rtrim([Submitted_via]))                  Else null End
      ,[Date_sent_to_company]          = Case when len(ltrim(rtrim([Date_sent_to_company])))         > 0 Then cast([Date_sent_to_company] as Date)           Else null End
      ,[Company_response_to_consumer]  = Case when len(ltrim(rtrim([Company_response_to_consumer]))) > 0 Then ltrim(rtrim([Company_response_to_consumer]))   Else null End
      ,[Timely_response]               = Case when len(ltrim(rtrim([Timely_response])))              > 0 Then ltrim(rtrim([Timely_response]))                Else null End
      ,[Consumer_disputed]             = Case when len(ltrim(rtrim([Consumer_disputed])))            > 0 Then ltrim(rtrim([Consumer_disputed]))              Else null End
      ,[Complaint_ID]                  = [Complaint_ID]
      ,[Loaded_By]                     = [Loaded_By]
	  ,[Cart_Log_Id]                   = [Cart_Log_Id]
Into #cart_cfpb_complaints_raw_stage
From dbo.cart_cfpb_complaints_raw_stage with (nolock)


--#########################################################Truncating Stage table and loading clean data###############################################################
Truncate table dbo.cart_cfpb_complaints_raw_stage
Insert Into    dbo.cart_cfpb_complaints_raw_stage
select * from  #cart_cfpb_complaints_raw_stage



--#########################################################Loading Data into Main table###############################################################
Declare @Load_Date Datetime = Getdate()

MERGE dbo.cart_cfpb_complaints_raw as cart
USING dbo.cart_cfpb_complaints_raw_stage AS stg
on cart.[Complaint_ID] = stg.[Complaint_ID]

WHEN NOT MATCHED BY Target THEN
Insert
(    
  [Complaint_ID]
 ,[Date_Received]
 ,[Product]
 ,[Sub_Product]
 ,[Issue]
 ,[Sub_Issue]
 ,[Complaint_Text]
 ,[Company_Public_Response]
 ,[Company]
 ,[State]
 ,[ZIP_Code]
 ,[Tags]
 ,[Consumer_Consent_Provided]
 ,[Submitted_Via]
 ,[Date_Sent_To_Company]
 ,[Company_Response_To_Consumer]
 ,[Timely_Response]
 ,[Consumer_Disputed]
 ,[Loaded_By]
 ,[Cart_Log_Id]
 ,[Load_Date]
)

Values
(
  stg.[Complaint_ID]
 ,stg.[Date_received]                  
 ,stg.[Product]
 ,stg.[Sub_product]
 ,stg.[Issue]
 ,stg.[Sub_issue]
 ,stg.[Consumer_complaint_narrative]
 ,stg.[Company_public_response]
 ,stg.[Company]
 ,stg.[State]
 ,stg.[ZIP_code]
 ,stg.[Tags]
 ,stg.[Consumer_consent_provided]
 ,stg.[Submitted_via]
 ,stg.[Date_sent_to_company]
 ,stg.[Company_response_to_consumer]
 ,stg.[Timely_response]
 ,stg.[Consumer_disputed]        
 ,stg.[Loaded_By]
 ,stg.[Cart_Log_Id]
 ,@Load_Date
)

WHEN  MATCHED THEN
UPDATE SET
   [Complaint_ID]                 =  stg.[Complaint_ID]
  ,[Date_Received]                =  stg.[Date_received]                  
  ,[Product]                      =  stg.[Product]
  ,[Sub_Product]                  =  stg.[Sub_product]
  ,[Issue]                        =  stg.[Issue]
  ,[Sub_Issue]                    =  stg.[Sub_issue]
  ,[Complaint_Text]               =  stg.[Consumer_complaint_narrative]
  ,[Company_Public_Response]      =  stg.[Company_public_response]
  ,[Company]                      =  stg.[Company]
  ,[State]                        =  stg.[State]
  ,[ZIP_Code]                     =  stg.[ZIP_code]
  ,[Tags]                         =  stg.[Tags]
  ,[Consumer_Consent_Provided]    =  stg.[Consumer_consent_provided]
  ,[Submitted_Via]                =  stg.[Submitted_via]
  ,[Date_Sent_To_Company]         =  stg.[Date_sent_to_company]
  ,[Company_Response_To_Consumer] =  stg.[Company_response_to_consumer]
  ,[Timely_Response]              =  stg.[Timely_response]
  ,[Consumer_Disputed]            =  stg.[Consumer_disputed]
  ,[Loaded_By]                    =  stg.[Loaded_By]    
  ,[Cart_Log_Id]                  =  stg.[Cart_Log_Id]
  ,[Update_Date]                  =  @Load_Date;

End
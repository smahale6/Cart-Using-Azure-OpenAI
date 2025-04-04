USE [CART]
GO
/****** Object:  StoredProcedure [dbo].[uspload_cart_cfpb_complaints_raw]    Script Date: 9/4/2024 10:42:40 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO


ALTER PROCEDURE [dbo].[uspload_cart_cfpb_complaints_reg]
As
BEGIN

Declare @Load_Date Datetime = Getdate()

MERGE dbo.cart_cfpb_complaints_reg as cart
USING dbo.cart_cfpb_complaints_reg_stage AS stg
on cart.[Complaint_ID] = stg.[Complaint_ID]

WHEN NOT MATCHED BY Target THEN
Insert
(
    [Complaint_ID]
   ,[Complaint_Text]
   ,[Reg_B]
   ,[Reg_B_Explanation]
   ,[Reg_C]
   ,[Reg_C_Explanation]
   ,[Reg_D]
   ,[Reg_D_Explanation]
   ,[Reg_E]
   ,[Reg_E_Explanation]
   ,[Reg_F]
   ,[Reg_F_Explanation]
   ,[Reg_G]
   ,[Reg_G_Explanation]
   ,[Reg_H]
   ,[Reg_H_Explanation]
   ,[Reg_I]
   ,[Reg_I_Explanation]
   ,[Reg_J]
   ,[Reg_J_Explanation]
   ,[Reg_K]
   ,[Reg_K_Explanation]
   ,[Reg_L]
   ,[Reg_L_Explanation]
   ,[Reg_M]
   ,[Reg_M_Explanation]
   ,[Reg_N]
   ,[Reg_N_Explanation]
   ,[Reg_O]
   ,[Reg_O_Explanation]
   ,[Reg_P]
   ,[Reg_P_Explanation]
   ,[Reg_V]
   ,[Reg_V_Explanation]
   ,[Reg_X]
   ,[Reg_X_Explanation]
   ,[Reg_Z]
   ,[Reg_Z_Explanation]
   ,[Reg_CC]
   ,[Reg_CC_Explanation]
   ,[Reg_DD]
   ,[Reg_DD_Explanation]
   ,[Reg_AA]
   ,[Reg_AA_Explanation]
   ,[Total_Tags]
   ,[Tagged_Regulations]
   ,[Loaded_By]
   ,[Cart_Log_Id]
   ,[Load_Date]
)

Values
(
    stg.[Complaint_ID]
   ,stg.[Complaint_Text]
   ,stg.[Reg_B]
   ,stg.[Reg_B_Explanation]
   ,stg.[Reg_C]
   ,stg.[Reg_C_Explanation]
   ,stg.[Reg_D]
   ,stg.[Reg_D_Explanation]
   ,stg.[Reg_E]
   ,stg.[Reg_E_Explanation]
   ,stg.[Reg_F]
   ,stg.[Reg_F_Explanation]
   ,stg.[Reg_G]
   ,stg.[Reg_G_Explanation]
   ,stg.[Reg_H]
   ,stg.[Reg_H_Explanation]
   ,stg.[Reg_I]
   ,stg.[Reg_I_Explanation]
   ,stg.[Reg_J]
   ,stg.[Reg_J_Explanation]
   ,stg.[Reg_K]
   ,stg.[Reg_K_Explanation]
   ,stg.[Reg_L]
   ,stg.[Reg_L_Explanation]
   ,stg.[Reg_M]
   ,stg.[Reg_M_Explanation]
   ,stg.[Reg_N]
   ,stg.[Reg_N_Explanation]
   ,stg.[Reg_O]
   ,stg.[Reg_O_Explanation]
   ,stg.[Reg_P]
   ,stg.[Reg_P_Explanation]
   ,stg.[Reg_V]
   ,stg.[Reg_V_Explanation]
   ,stg.[Reg_X]
   ,stg.[Reg_X_Explanation]
   ,stg.[Reg_Z]
   ,stg.[Reg_Z_Explanation]
   ,stg.[Reg_CC]
   ,stg.[Reg_CC_Explanation]
   ,stg.[Reg_DD]
   ,stg.[Reg_DD_Explanation]
   ,stg.[Reg_AA]
   ,stg.[Reg_AA_Explanation]
   ,stg.[Total_Tags]
   ,stg.[Tagged_Regulations]
   ,stg.[Loaded_By]
   ,stg.[Cart_Log_Id]
   ,@Load_Date
)

WHEN  MATCHED THEN
UPDATE SET
    [Complaint_ID]              =  stg.[Complaint_ID]          
   ,[Complaint_Text]			=  stg.[Complaint_Text]		
   ,[Reg_B]						=  stg.[Reg_B]					
   ,[Reg_B_Explanation]			=  stg.[Reg_B_Explanation]		
   ,[Reg_C]						=  stg.[Reg_C]					
   ,[Reg_C_Explanation]			=  stg.[Reg_C_Explanation]		
   ,[Reg_D]						=  stg.[Reg_D]					
   ,[Reg_D_Explanation]			=  stg.[Reg_D_Explanation]		
   ,[Reg_E]						=  stg.[Reg_E]					
   ,[Reg_E_Explanation]			=  stg.[Reg_E_Explanation]		
   ,[Reg_F]						=  stg.[Reg_F]					
   ,[Reg_F_Explanation]			=  stg.[Reg_F_Explanation]		
   ,[Reg_G]						=  stg.[Reg_G]					
   ,[Reg_G_Explanation]			=  stg.[Reg_G_Explanation]		
   ,[Reg_H]						=  stg.[Reg_H]					
   ,[Reg_H_Explanation]			=  stg.[Reg_H_Explanation]		
   ,[Reg_I]						=  stg.[Reg_I]					
   ,[Reg_I_Explanation]			=  stg.[Reg_I_Explanation]		
   ,[Reg_J]						=  stg.[Reg_J]					
   ,[Reg_J_Explanation]			=  stg.[Reg_J_Explanation]		
   ,[Reg_K]						=  stg.[Reg_K]					
   ,[Reg_K_Explanation]			=  stg.[Reg_K_Explanation]		
   ,[Reg_L]						=  stg.[Reg_L]					
   ,[Reg_L_Explanation]			=  stg.[Reg_L_Explanation]		
   ,[Reg_M]						=  stg.[Reg_M]					
   ,[Reg_M_Explanation]			=  stg.[Reg_M_Explanation]		
   ,[Reg_N]						=  stg.[Reg_N]					
   ,[Reg_N_Explanation]			=  stg.[Reg_N_Explanation]		
   ,[Reg_O]						=  stg.[Reg_O]					
   ,[Reg_O_Explanation]			=  stg.[Reg_O_Explanation]		
   ,[Reg_P]						=  stg.[Reg_P]					
   ,[Reg_P_Explanation]			=  stg.[Reg_P_Explanation]		
   ,[Reg_V]						=  stg.[Reg_V]					
   ,[Reg_V_Explanation]			=  stg.[Reg_V_Explanation]		
   ,[Reg_X]						=  stg.[Reg_X]					
   ,[Reg_X_Explanation]			=  stg.[Reg_X_Explanation]		
   ,[Reg_Z]						=  stg.[Reg_Z]					
   ,[Reg_Z_Explanation]			=  stg.[Reg_Z_Explanation]		
   ,[Reg_CC]					=  stg.[Reg_CC]				
   ,[Reg_CC_Explanation]		=  stg.[Reg_CC_Explanation]	
   ,[Reg_DD]					=  stg.[Reg_DD]				
   ,[Reg_DD_Explanation]		=  stg.[Reg_DD_Explanation]	
   ,[Reg_AA]					=  stg.[Reg_AA]				
   ,[Reg_AA_Explanation]		=  stg.[Reg_AA_Explanation]	
   ,[Total_Tags]				=  stg.[Total_Tags]			
   ,[Tagged_Regulations]		=  stg.[Tagged_Regulations]	
   ,[Loaded_By]					=  stg.[Loaded_By]		
   ,[Cart_Log_Id]				=  stg.[Cart_Log_Id]
   ,[Update_Date]				=  @Load_Date	;		


End
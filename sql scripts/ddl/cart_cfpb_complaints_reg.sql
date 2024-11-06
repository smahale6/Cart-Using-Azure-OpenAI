USE [CART]
GO

/****** Object:  Table [dbo].[cart_cfpb_complaints_reg]    Script Date: 8/24/2024 6:52:49 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO
DROP TABLE IF EXISTS [dbo].cart_cfpb_complaints_reg
CREATE TABLE [dbo].cart_cfpb_complaints_reg(
	[Complaint_ID]                  [int]  NOT NULL,
	[Complaint_Text]                [text] NULL,
    [Reg_B]						    [int]  NULL,
    [Reg_B_Explanation]             [text] NULL,
    [Reg_C]						    [int]  NULL,
    [Reg_C_Explanation]             [text] NULL,
    [Reg_D]						    [int]  NULL,
    [Reg_D_Explanation]             [text] NULL,
    [Reg_E]						    [int]  NULL,
    [Reg_E_Explanation]             [text] NULL,
    [Reg_F]						    [int]  NULL,
    [Reg_F_Explanation]             [text] NULL,
    [Reg_G]						    [int]  NULL,
    [Reg_G_Explanation]             [text] NULL,
    [Reg_H]							[int]  NULL,
    [Reg_H_Explanation]				[text] NULL,
    [Reg_I]							[int]  NULL,
    [Reg_I_Explanation]				[text] NULL,
    [Reg_J]							[int]  NULL,
    [Reg_J_Explanation]				[text] NULL,
    [Reg_K]							[int]  NULL,
    [Reg_K_Explanation]				[text] NULL,
    [Reg_L]							[int]  NULL,
    [Reg_L_Explanation]				[text] NULL,
    [Reg_M]							[int]  NULL,
    [Reg_M_Explanation]				[text] NULL,
    [Reg_N]							[int]  NULL,
    [Reg_N_Explanation]				[text] NULL,
    [Reg_O]							[int]  NULL,
    [Reg_O_Explanation]				[text] NULL,
    [Reg_P]							[int]  NULL,
    [Reg_P_Explanation]				[text] NULL,
    [Reg_V]							[int]  NULL,
    [Reg_V_Explanation] 			[text] NULL,
    [Reg_X]							[int]  NULL,
    [Reg_X_Explanation]				[text] NULL,
    [Reg_Z]							[int]  NULL,
    [Reg_Z_Explanation]				[text] NULL,
    [Reg_CC]						[int]  NULL,
    [Reg_CC_Explanation]			[text] NULL,
    [Reg_DD]						[int]  NULL,
    [Reg_DD_Explanation]			[text] NULL,
    [Reg_AA]						[int]  NULL,
    [Reg_AA_Explanation]			[text] NULL,
	[Total_Tags]					[int] NULL,
	[Tagged_Regulations]	        [Varchar](max) NULL,
	[Loaded_By]                     [varchar](100) Not NULL,
	[Cart_Log_Id]					[int] NULL,
	[Load_Date]                     [Datetime] not null,
	[Update_Date]                   [Datetime] null, 
 CONSTRAINT [PK_comp_reg] PRIMARY KEY CLUSTERED 
(
	[Complaint_ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO



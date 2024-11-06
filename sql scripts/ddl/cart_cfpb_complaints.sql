USE [CART]
GO

/****** Object:  Table [dbo].[cart_cfpb_complaints_raw]    Script Date: 8/24/2024 6:52:49 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO
DROP TABLE IF EXISTS [dbo].[cart_cfpb_complaints_raw]
CREATE TABLE [dbo].[cart_cfpb_complaints_raw](
	[Complaint_ID] [int] NOT NULL,
	[Date_Received] [date] NULL,
	[Product] [varchar](100) NULL,
	[Sub_Product] [varchar](100) NULL,
	[Issue] [varchar](512) NULL,
	[Sub_Issue] [varchar](512) NULL,
	[Complaint_Text] [text] NULL,
	[Company_Public_Response] [varchar](100) NULL,
	[Company] [varchar](100) NULL,
	[State] [varchar](50) NULL,
	[ZIP_Code] [varchar](15) NULL,
	[Tags] [varchar](100) NULL,
	[Consumer_Consent_Provided] [varchar](100)  NULL,
	[Submitted_Via] [varchar](100) NULL,
	[Date_Sent_To_Company] [date] NULL,
	[Company_Response_To_Consumer] [varchar](512)  NULL,
	[Timely_Response] [varchar](100) NULL,
	[Consumer_Disputed] [varchar](100) NULL,
	[Loaded_By] [varchar](100) Not NULL,
	Cart_Log_Id int not null,
	[Load_Date] [date] not null,
	[Update_Date] [date] null
 CONSTRAINT [PK_complaints] PRIMARY KEY CLUSTERED 
(
	[Complaint_ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO



USE [CART]
GO

/****** Object:  Table [dbo].[cart_log]    Script Date: 8/26/2024 2:59:56 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

DROP TABLE IF EXISTS [dbo].[cart_log]
CREATE TABLE [dbo].[cart_log](
	[Cart_Log_Id] [int] primary key identity(1000,1) NOT NULL ,
	[Version] [float]  NOT NULL,
	[Cart_Log_Status] varchar(100) Null,
	[Total_Complaints] [int] NOT NULL Default 0,
	[Reg_B_Count] [int] NOT NULL Default 0,
	[Reg_C_Count] [int] NOT NULL Default 0,
	[Reg_D_Count] [int] NOT NULL Default 0,
	[Reg_E_Count] [int] NOT NULL Default 0,
	[Reg_F_Count] [int] NOT NULL Default 0,
	[Reg_G_Count] [int] NOT NULL Default 0,
	[Reg_H_Count] [int] NOT NULL Default 0,
	[Reg_I_Count] [int] NOT NULL Default 0,
	[Reg_J_Count] [int] NOT NULL Default 0,
	[Reg_K_Count] [int] NOT NULL Default 0,
	[Reg_L_Count] [int] NOT NULL Default 0,
	[Reg_M_Count] [int] NOT NULL Default 0,
	[Reg_N_Count] [int] NOT NULL Default 0,
	[Reg_O_Count] [int] NOT NULL Default 0,
	[Reg_P_Count] [int] NOT NULL Default 0,
	[Reg_V_Count] [int] NOT NULL Default 0,
	[Reg_X_Count] [int] NOT NULL Default 0,
	[Reg_Z_Count] [int] NOT NULL Default 0,
	[Reg_CC_Count] [int] NOT NULL Default 0,
	[Reg_DD_Count] [int] NOT NULL Default 0,
	[Reg_AA_Count] [int] NOT NULL Default 0,
	[Tagged_By] [varchar](100) NOT NULL,
	[Log_Date] [date] NULL
)





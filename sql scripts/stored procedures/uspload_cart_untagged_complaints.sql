USE [CART]
GO
/****** Object:  StoredProcedure [dbo].[uspload_cart_cfpb_untagged_complaints]    Script Date: 8/26/2024 1:45:15 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO


CREATE PROCEDURE [dbo].[uspload_cart_untagged_complaints]
As
BEGIN

Drop Table If EXISTS #cart_untagged_complaints
Select
	raw.[Complaint_ID],
	raw.[Complaint_Text]
into #cart_untagged_complaints
From [dbo].[cart_cfpb_complaints_raw] raw
     left join [dbo].[cart_cfpb_complaints_reg] reg on raw.[Complaint_ID] = reg.[Complaint_ID]
Where reg.[Complaint_ID] is null

Truncate table [dbo].[cart_untagged_complaints]
Insert into [dbo].[cart_untagged_complaints]
Select * from #cart_untagged_complaints

END


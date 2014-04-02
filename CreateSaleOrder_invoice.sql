declare @serialNo int 
--get the serial number of the sale invoice.
Select @serialNo=JBillLastNo From TBillNumber Where JDeptID = 1 and JBillInfoID = 1302 and JMonthNO = 1  


--insert sale order
exec sp_executesql N'INSERT INTO [TOrderBill] ([JInputrID], [JChkrID], [JBillDate], [JBillCode], [JBillAmt], [JHandleID], [JDeptID], [JBillType], [JMemo], [JAskType], [JStockID], [JDeliveryDaten], [JSupClientID], [JDeliveryAdd], [JMaster], [JUseID], [JSecondDeptID], [JSupplyType], [JChkrID2], [JKeepID], [JUseBillType], [JMobile], [JClientDiscRate]) VALUES (@p1, @p2, @p3, @p4, @p5, @p6, @p7, @p8, @p9, @p10, @p11, @p12, @p13, @p14, @p15, @p16, @p17, @p18, @p19, @p20, @p21, @p22, @p23)',N'@p1 int,@p2 int,@p3 smalldatetime,@p4 nvarchar(16),@p5 decimal(18,6),@p6 int,@p7 int,@p8 int,@p9 nvarchar(4000),@p10 int,@p11 int,@p12 smalldatetime,@p13 int,@p14 nvarchar(4000),@p15 nvarchar(1),@p16 int,@p17 int,@p18 int,@p19 int,@p20 bit,@p21 int,@p22 int,@p23 decimal(18,4)',@p1=1,@p2=0,@p3='Jan 30 2014  9:55:00:000AM',@p4=N'SD0011401-000004',@p5=28200.000000,@p6=0,@p7=1,@p8=1302,@p9=N'',@p10=0,@p11=1,@p12=NULL,@p13=2,@p14=N'',@p15=N' ',@p16=0,@p17=0,@p18=0,@p19=0,@p20=0,@p21=0,@p22=0,@p23=1.0000


--update serialno 
exec sp_executesql N'UPDATE [TBillNumber] SET [JBillLastNO] = @p1 WHERE (([JDeptID] = @p2) AND ([JBillInfoID] = @p3) AND ((@p4 = 1 AND [JBillLastNO] IS NULL) OR ([JBillLastNO] = @p5)) AND ([JMonthNO] = @p6))',N'@p1 int,@p2 int,@p3 int,@p4 int,@p5 int,@p6 int',@p1=serialNo+1,@p2=1,@p3=1302,@p4=0,@p5=3,@p6=1
go

-- insert sale order detail
exec sp_executesql N'INSERT INTO [TOrderGrid] ([JBillID], [JGoodsID], [JGridQty], [JChkrQty], [JGridAmt], [JGridPrice], [JDiscRate], [JUseID], [JReceivingInform], [JOrderID], [JUseBillType], [JMultiUnitID], [JMultiUnitText], [JTransRate]) VALUES (@p1, @p2, @p3, @p4, @p5, @p6, @p7, @p8, @p9, @p10, @p11, @p12, @p13, @p14)',N'@p1 int,@p2 int,@p3 decimal(18,6),@p4 decimal(18,6),@p5 decimal(18,4),@p6 decimal(18,6),@p7 decimal(18,6),@p8 int,@p9 nvarchar(4000),@p10 int,@p11 int,@p12 int,@p13 nvarchar(2),@p14 decimal(18,6)',@p1=26,@p2=1747,@p3=12.000000,@p4=0.000000,@p5=28200.0000,@p6=2350.000000,@p7=1.000000,@p8=0,@p9=N'',@p10=1,@p11=0,@p12=0,@p13=N'12',@p14=0.000000
go
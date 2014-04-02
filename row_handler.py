import re
class row_parser:
    '''import eachrow to database'''
    
    def __init__(self, rowdata):
        self.rowdata = rowdata
        
    def parse(self):
        #print('----------RowData--')
        #print (self.rowdata)
        #print('----------RowData End-----')
        # header
        if self.rowdata[0] == 'Customer Product Sales Report':
            return ("row_daily_head",)
        
        # billdate
        m_bill_date = re.match(r'(\d{2}/\d{2}/\d{4})\s-\s(\d{2}/\d{2}/\d{4})', self.rowdata[0])
        if m_bill_date:
            bill_date_begin = m_bill_date.group(1)
            bill_date_end = m_bill_date.group(2)
            if bill_date_begin != bill_date_end:
                #print (bill_date_begin + '---------'+bill_date_end)
                raise "Bill_date_begin not equal to bill_date_end"
            return ('row_bill_date', bill_date_begin,)
        
        # customer
        m_customer = re.match(r'Cust\.\s:(\d{4}/\d{3}):(.+)', self.rowdata[0])
        if m_customer:
            return ("row_customer", m_customer.group(1), m_customer.group(2),)
        # grand total , ignore
        if str(self.rowdata[0])=='Grand Total':
            return None
        # bill total
        if str(self.rowdata[0]) == 'Grand Total':
            return ("row_bill_total", self.rowdata[2], self.rowdata[5],)
        
        # product item
        m_item_id = re.match(r"[a-zA-Z0-9_]", self.rowdata[0])
        if m_item_id and  self.rowdata[2]!='' and self.rowdata[7]!='':
            
            m_item_qty = re.match(r'\d+(\.0+)?', str(self.rowdata[2]))
            m_item_total = re.match(r'\d+(\.0+)?', str(self.rowdata[7]))
            if m_item_id and m_item_qty and m_item_total:
                return ('row_item', m_item_id, m_item_qty, m_item_total,)
        
        #bill end line
        #print(self.rowdata)
        if str(self.rowdata[0])=='' and str(self.rowdata[1])=='' and str(self.rowdata[3])!='' and \
         str(self.rowdata[3])!='' and str(self.rowdata[4])!='' and str(self.rowdata[5])!='' \
        and str(self.rowdata[6])!='' and str(self.rowdata[7])!='' and str(self.rowdata[8])!='' :
            '''print('------Should Be End-----------')
            print(self.rowdata[0])
            print(str(self.rowdata[0])=='')
            print(str(self.rowdata[1])=='')
            print(bool(re.match('\d+(\.0+)?',str(self.rowdata[2]))))
            print(bool(re.match('\d+(\.0+)?',str(self.rowdata[3])).group(0)))
            print(bool(re.match('\d+(\.0+)?',str(self.rowdata[4])).group(0)))
            print(bool(re.match('\d+(\.0+)?',str(self.rowdata[5])).group(0)))
            print(bool(re.match('\d+(\.0+)?',str(self.rowdata[6])).group(0)))
            print(bool(re.match('\d+(\.0+)?',str(self.rowdata[7])).group(0)))
            print(bool(re.match('\d+(\.0+)?',str(self.rowdata[8])).group(0)))
            '''
            if str(self.rowdata[0])=='' and str(self.rowdata[1])=='' and  re.match('\d+(\.0+)?',str(self.rowdata[2])) \
            and re.match('\d+(\.0+)?',str(self.rowdata[3])) and re.match('\d+(\.0+)?',str(self.rowdata[4])) \
            and re.match('\d+(\.0+)?',str(self.rowdata[5])) and re.match('\d+(\.0+)?',str(self.rowdata[6])) \
            and re.match('\d+(\.0+)?',str(self.rowdata[7]))  and re.match('\d+(\.0+)?',str(self.rowdata[8])):
                return ('row_bill_total',self.rowdata[5])
        
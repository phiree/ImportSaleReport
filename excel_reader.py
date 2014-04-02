import xlrd
import os
from datetime import datetime
from row_handler import row_parser
class excel_reader:
    def __init__(self,excel_file_path):
        self.excel_file_path=excel_file_path
        
    def read(self):
        workbook = xlrd.open_workbook(self.excel_file_path)
        #just want to part the first sheet
        worksheets=[workbook.sheet_by_index(1)]
        bookdata={}
        bookdata['filename']=self.excel_file_path
        bookdata['sheetsdata']=[]
        for sheet in worksheets:
            #fill merged cell with value of top left cell
            
            sheetdata={}
            sheetname=sheet.name
            sheetdata['sheetname']=sheetname
            sheetdata['rowlist']=[]
            current_row=0 # skip the title
            #print('sheet.nrows:'+str(sheet.nrows))
            #print('sheet.ncols:'+str(sheet.ncols))
            pool_bill={}
            pool_bill['items']=[]
            while current_row<sheet.nrows:
                rowdata=[]
                row=sheet.row(current_row)
                current_col=0
                #print('sheet.row_len():'+str(current_row)+','+str(sheet.row_len(current_row)))
                while current_col <sheet.ncols:
                    current_cell_value=sheet.cell_value(current_row,current_col)
                    current_cell_type=sheet.cell_type(current_row,current_col)
                    if current_cell_type== xlrd.XL_CELL_DATE:
                            dt_tuple = xlrd.xldate_as_tuple(current_cell_value, workbook.datemode)
                            # Create datetime object from this tuple.
                            get_col = datetime(
                            dt_tuple[0], dt_tuple[1], dt_tuple[2], 
                            dt_tuple[3], dt_tuple[4], dt_tuple[5]
                            )
                    
                    if current_cell_value=='':
                        current_cell_value=self.get_value_for_merged_cell(sheet, current_row,current_col)
                    #print ('current_row:'+str(current_row)+'current_col:'+str(current_col)+'value:'+str(current_cell_value))
                    rowdata.append(current_cell_value)
                    current_col+=1
                current_row+=1
                parser=row_parser(rowdata)
                row_data=parser.parse()
                
                if not row_data:
                    print(row_data)
                    continue
               
                if row_data[0]=='row_bill_total':
                    pool_bill["total"]=row_data
                    #import pdb;pdb.set_trace()
                    print('----------')
                    self.save_bill(pool_bill)
                    #flush the pool

                    pool_bill['items']=[]
                    
                    continue
                if row_data[0]=='row_bill_date':
                    pool_bill["date"]=row_data
                if row_data[0]=='row_customer':
                    pool_bill['customer']=row_data
                if row_data[0]=='row_item':
                    pool_bill['items'].append(row_data)
               
            bookdata['sheetsdata'].append(sheetdata)
        return bookdata
    def save_bill(self,bill):
        #import pdb;pdb.set_trace()
        print('--Create Bill---')
        print('Date:'+str(bill['date']))
        print('customer:'+str(bill['customer']))
        print('items:'+str(len(bill['items'])))
        print('total:'+str(bill['total']))

    def get_value_for_merged_cell(self,sheet,idxr,idxc):
        #import pdb;pdb.set_trace()
        
        #print('--------------------')
        for crange in sheet.merged_cells:
            #print(crange)
            #0,1,0,3 the hi index is based 1 but the low 0, confused, bug?
            rlo, rhi, clo, chi = crange
            if rlo<=idxr<=rhi-1 and clo<=idxc<=chi-1: 
                return sheet.cell_value(rlo,clo)
        return ''
            
if __name__=='__main__':
    reader=excel_reader('Test_January_Sale_Conso.xlsx')
    print(reader.read())
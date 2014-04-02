import pyodbc

def save(bill):
    conn=pyodbc.connect("driver={SQL Server};server=.\sqlexpress;database=TSNET1001;Trusted_Connection=yes")
    cursor=conn.cursor()
    cursor.execute("select * from tgoods")
    row=cursor.fetchone()
    if row:
        print(row)
if __name__=="__main__":
    save({"name":"bill_name"})
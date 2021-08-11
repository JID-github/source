import pymysql
from tkinter import *
from tkinter import messagebox


##함수 선언부
def insertData() :
    con, cur = None, None
    data1, data2, data3, data4 = "", ", ", ""
    sql=""

    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='memberDB', charset='utf8')
    cur = conn.cursor()

    data1 = edt1.get();     data2 = edt2.get();     data3 = edt3.get();     data4 = edt4.get()
    try :
        sql = "INSERT INTO usertable VALUES('" + data1 + "','" + data2 + "','" + data3 + "','" + data4 + "')"
        cur.execute(sql)
    except :
        messagebox.showerror('오류', '데잍 입력 오류가 발생함')
    else :
        messagebox.showinfo('성공', '데이터 입력 성공')
    
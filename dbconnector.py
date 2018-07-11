# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 09:31:40 2018

@author: xxiu
"""
import cx_Oracle

 

CONN_INFO = {
        'hots' : '54.72.155.85',
        'port': '1521',
        'user': 'quercus',
        'psw': 'quercus',
        'service': 'qdev '
        
        }

class dbconnector:
    
    def connect(self,query):
        
        conn_str = 'quercus/quercus@54.72.155.85:1521/qdev'
        conn = cx_Oracle.connect(conn_str)
        c = conn.cursor()
        c.execute(query)
        i = 0
        for row in c:
            print(row[:])
            i += 1
            print(i)
        conn.close()
        return c


with open('sqlquery.txt','r') as f:
    query = f.read().replace('\n',' ')


db = dbconnector()
db.connect(query)
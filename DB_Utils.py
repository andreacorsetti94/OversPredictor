#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3
from sqlite3 import Error
from contextlib import closing


# In[5]:


class SQLiteDB:
    
    def __init__(self,db_file):
        self.db_file = db_file
        
    def query(self, sql, data):
        with closing(sqlite3.connect(self.db_file)) as con, con, closing(con.cursor()) as cur:
            cur.execute(sql,data)
            return cur.fetchall()
        
    def write(self, sql, data):
        with closing(sqlite3.connect(self.db_file)) as con, con, closing(con.cursor()) as cur:
            cur.execute(sql,data)


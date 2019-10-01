import pandas as pd
import sqlite3

with sqlite3.connect('db.sqlite3') as conn:
    df=pd.read_sql_query("SELECT * from Users", conn)

df['first_and_last_name'] = df['first_name'] + df['last_name']
print(df)

export_excel = df.to_excel (r'C:\Users\student1\PycharmProjects\untitled\export_and.xlsx', index = None, header=True)
print("Media pe number of login", df['number_of_login'].mean())
print("Standard deviation pe number of login", df['number_of_login'].std())
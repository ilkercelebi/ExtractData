import pandas as pd
import pyodbc

# SQL Server bağlantısı
conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=GPTSERVER;'
    'DATABASE=GPTDATA;'
    'Trusted_Connection=yes;'
)

# Getirmek istediğimiz datalar için SQL sorgusu
query = "SELECT * FROM DB"

#SQL'den verileri alma
df = pd.read_sql(query, conn)

#CSV formatına dönüştürme
df.to_csv('data2.csv', index=False)

print("Veri CSV dosyasına başarıyla aktarıldı.")

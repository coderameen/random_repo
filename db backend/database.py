import sqlite3
conn = sqlite3.connect("hospitaldb.db", check_same_thread = False)


cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS doctors(d_id TEXT NOT NULL PRIMARY KEY, d_name TEXT, d_designation TEXT)""")
conn.commit()
print("table created successfully")
cursor.execute("""CREATE TABLE IF NOT EXISTS patient(p_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, p_name TEXT, symptom  TEXT, d_id)""")
conn.commit()
print("patient table created successfully")


#insert into tabnle
# cursor.execute("""INSERT INTO doctors(d_id, d_name, d_designation) VALUES(?,?,?)""",("d01","Alen","mbbs"))
# cursor.execute("""INSERT INTO doctors(d_id, d_name, d_designation) VALUES(?,?,?)""",("d02","Bob","Neurologist"))
conn.commit()
print("data inserted successfully")

# cursor.execute("""DROP TABLE patient""")
# print("table deleted successfully")
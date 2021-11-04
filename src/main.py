from db import getDb

db = getDb()

cursor = db.cursor()
cursor.execute("SELECT email, firstName FROM employees;")
result = cursor.fetchall()

for x in result:
  print(x[0])

import mysql.connector

mydb = mysql.connector.connect(
  host="https://mysql.transip.nl/",
  user="sulay_nl_sulaydb",
  passwd="Hatuluwaja",
  port="3307",
  database="sulay_nl_sulaydb"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM users")

myresult = mycursor.fetchone()

print(myresult)
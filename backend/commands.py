import sqlite3

con = sqlite3.connect("./database/ecommerce.db")
cursor = con.cursor()

# cursor.execute("drop table Cards")
# # cursor.execute("INSERT INTO pedidos (id, product, user, quant)SELECT id, product, user, quant FROM pedidos_old;")
# cursor.execute("""
#     CREATE TABLE Cards (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         user_id INTEGER NOT NULL,
#         CardType TEXT NOT NULL,
#         Num TEXT NOT NULL,
#         Mes INTEGER NOT NULL,
#         Ano INTEGER NOT NULL,
#         CVV TEXT NOT NULL,
#         Nome TEXT NOT NULL,
#         FOREIGN KEY (user_id) REFERENCES Users(id)
#     )

# """)
sql = "SELECT COUNT(*) FROM produtos WHERE LOWER(src) LIKE '%.jpg';"
cursor.execute(sql)          # Executa a query primeiro
result = cursor.fetchone()   # Pega a primeira linha do resultado
print(result[0])             # Imprime o valor do COUNT(*)


sql = "UPDATE produtos SET src = REPLACE(src, '.jpg', '.webp') WHERE LOWER(src) LIKE '%.jpg';"
cursor.execute(sql)
print(cursor.rowcount)  # Deve mostrar 22
con.commit()
# print(columns)
con.commit()

# Exibir os detalhes das colunas
# for column in columns:
#     print(column)
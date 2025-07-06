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

# # """)
# sql = "SELECT COUNT(*) FROM produtos WHERE LOWER(src) LIKE '%.jpg';"
# cursor.execute(sql)          # Executa a query primeiro
# result = cursor.fetchone()   # Pega a primeira linha do resultado
# print(result[0])             # Imprime o valor do COUNT(*)


sql = """UPDATE produtos SET `long_description` = '
<div class="product-description">
    <h2>Sensor de Gás MQ-2 - Detecção de Gases Inflamáveis</h2>
    <p>O <strong>Sensor MQ-2</strong> detecta uma variedade de gases inflamáveis e fumaça, com alta sensibilidade e resposta rápida.</p>
    
    <div class="gas-detection">
        <h3>Gases Detectados:</h3>
        <ul>
            <li>GLP (gás de cozinha)</li>
            <li>Metano (CH4)</li>
            <li>Propano (C3H8)</li>
            <li>Butano (C4H10)</li>
            <li>Fumaça</li>
            <li>Álcool</li>
        </ul>
    </div>
    
    <div class="technical-data">
        <h3>Dados Técnicos:</h3>
        <table>
            <tr><td>Tensão de operação</td><td>5V DC</td></tr>
            <tr><td>Consumo</td><td>~150mA</td></tr>
            <tr><td>Tempo de aquecimento</td><td>>24 horas (ótimo desempenho)</td></tr>
            <tr><td>Saída</td><td>Analógica (0-5V) e Digital (TTL)</td></tr>
        </table>
    </div>
    
    <div class="safety-features">
        <h3>Recursos para Aplicações Críticas:</h3>
        <ul>
            <li>Sinalizador de pré-aquecimento</li>
            <li>Compensação de temperatura/humidade</li>
            <li>Saída digital com limiar ajustável</li>
            <li>Design robusto para uso contínuo</li>
        </ul>
    </div>
</div>
' WHERE id = 22;
"""
cursor.executescript(sql)
# print(cursor.rowcount)  # Deve mostrar 22
con.commit()
# print(columns)
con.commit()

# Exibir os detalhes das colunas
# for column in columns:
#     print(column)
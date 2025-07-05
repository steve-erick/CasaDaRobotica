import sqlite3  

class DB:
    def __init__(self):
        # Conexão persistente (fora do 'with', senão fecha ao sair do bloco)
        self.con = sqlite3.connect("./database/ecommerce.db")
        self.cur = self.con.cursor()
        self.cur.execute("PRAGMA foreign_keys = ON")

class Products(DB):  # Herda de DB
    def __init__(self):
        super().__init__()

    def select_all_products(self):
        try:
            self.cur.execute('SELECT * FROM produtos')
            data = self.cur.fetchall()
        except sqlite3.Error as e:
            return(f"SQLite error occurred: {e}")   
        finally:
            self.con.close()
            return data

    def select_product(self, id):
        try:
            self.cur.execute('SELECT * FROM produtos WHERE id = ?', (id,))
            data = self.cur.fetchone()
        except sqlite3.Error as e:
            return(f"SQLite error occurred: {e}")   
        finally:
            self.con.close()
            return data

    def search(self,searchdata):
        try:
            terms = searchdata.split()

# Criar a SQL com OR para as duas colunas
            sql = "SELECT * FROM produtos WHERE " + " OR ".join(
            ["name LIKE ?"] * len(terms) + ["description LIKE ?"] * len(terms)
            )

# Criar os parâmetros para a consulta
            params = ['%' + term + '%' for term in terms] * 2  # Multiplicando por 2 para cada termo ser aplicado nas duas colunas

# Executar a consulta
            self.cur.execute(sql, params)
            searchresult = self.cur.fetchall()

        except sqlite3.Error as e:
            return(f"SQLite error occurred: {e}")   
        finally:
            self.con.close()
            return searchresult
 
class Users(DB):  # Faltou ":" e ajuste na herança
    def __init__(self):
        super().__init__()

    def new_user(self, name, phone,email,password,adrres):
        try:
            self.cur.execute('INSERT INTO Users (name, phone, email, password, adrres) VALUES (?, ?, ?, ?, ?)', (name, phone, email, password, adrres))       
        
            if self.cur.rowcount > 0:
                self.con.commit()
                return self.cur.lastrowid  # Confirmação de sucesso
            else:
                return "Falha na inserção do usuário."
        except sqlite3.Error as e:
            self.con.rollback()  # Desfaz qualquer alteração em caso de erro
            return f"Erro no banco de dados: {e}"
        finally:
            self.con.close()

    def checkuser(self,Email,password):
        try:
            self.cur.execute("SELECT * FROM users where Email == ? and password == ?;",(Email,password))
            data = self.cur.fetchone()
        except sqlite3.Error as e:
            self.con.rollback()  # Desfaz qualquer alteração em caso de erro
            return(f"SQLite error occurred: {e}")   
        finally:
            self.con.close()
            if(data):
                return(data)
            else: 
                return(False)
            # print(data)
    def datafromuser(self,id):
        try:
            self.cur.execute("SELECT * FROM users where id == ? ;",(id,))
            data = self.cur.fetchone()
            return data
        except sqlite3.Error as e:
            self.con.rollback()  # Desfaz qualquer alteração em caso de erro
            return(f"SQLite error occurred: {e}")   
        finally:
            self.con.close()
    
class Pedidos(DB):  # Faltou ":" e ajuste na herança
    def __init__(self):
        super().__init__()

    def listar_pedidos(self,id):
            try:
                self.cur.execute("SELECT * FROM pedidos where user == ? ;",(id,))
                data = self.cur.fetchall()
                return data
            except sqlite3.Error as e:
                self.con.rollback()  # Desfaz qualquer alteração em caso de erro
                return(f"SQLite error occurred: {e}")   
            finally:
                self.con.close()
    def AttAmount(self,id,amount):
        try:
                self.cur.execute("UPDATE pedidos SET quant = ? where id == ? ;",(amount,id,))
                self.con.commit()
                self.cur.execute("SELECT quant FROM pedidos where id == ? ;",(id,))
                data = self.cur.fetchone()
                return data
        except sqlite3.Error as e:
                self.con.rollback()  # Desfaz qualquer alteração em caso de erro
                return(f"SQLite error occurred: {e}")   
        finally:
                self.con.close()
    def removerPedido(self,id):
        try:
                print(id)
                self.cur.execute("DELETE from pedidos WHERE id == ? ;",(id,))
                self.con.commit()
                return 'Pedido removido com sucesso'
        except sqlite3.Error as e:
                self.con.rollback()  # Desfaz qualquer alteração em caso de erro
                return(f"SQLite error occurred: {e}") 
    def newpedido(self,product,user,quant):
        try:
            self.cur.execute("SELECT id, quant FROM pedidos WHERE product = ? AND user = ?", (product, user))
            existing = self.cur.fetchone()

            if existing:
                pedido_id, quantidade_atual = existing
                nova_quantidade = quantidade_atual + quant
                self.cur.execute("UPDATE pedidos SET quant = ? WHERE id = ?", (nova_quantidade, pedido_id))
                self.con.commit()
                return "Quantidade atualizada com sucesso"
            else:
                self.cur.execute("INSERT INTO pedidos (product, user, quant, status) VALUES (?, ?, ?, 'Pending');", (product, user, quant))
                self.con.commit()
                return "Pedido inserido com sucesso"
        except sqlite3.Error as e:
                self.con.rollback()  # Desfaz qualquer alteração em caso de erro
                return(f"SQLite error occurred: {e}") 
        
class Cards(DB):
     def __init__(self):
        super().__init__()

     def ShowCards(self,id):
        try:
            self.cur.execute("SELECT * FROM cards Where user_id = ?",(id,))
            result = self.cur.fetchall()
            return result
        except sqlite3.Error as e:
                self.con.rollback()  # Desfaz qualquer alteração em caso de erro
                return(f"SQLite error occurred: {e}") 
        finally:
            self.con.close()
     def removerCard(self,id):
        try:
                # print(id)
                self.cur.execute("DELETE from cards WHERE id == ? ;",(id,))
                self.con.commit()
                return 'Pedido removido com sucesso'
        except sqlite3.Error as e:
                self.con.rollback()  # Desfaz qualquer alteração em caso de erro
                return(f"SQLite error occurred: {e}") 
        
     def newcard(self,user_id,CardType,Num,Mes,Ano,CVV,Nome):
          try:
               self.cur.execute("INSERT into cards (user_id,CardType,Num,Mes,Ano,CVV,Nome) VALUES (?,?,?,?,?,?,?)", (user_id,CardType,Num,Mes,Ano,CVV,Nome))
          except sqlite3.Error as e:
                self.con.rollback()  # Desfaz qualquer alteração em caso de erro
                return(f"SQLite error occurred: {e}") 
               
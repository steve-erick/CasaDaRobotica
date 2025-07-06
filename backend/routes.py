from flask import Flask, Blueprint, jsonify, send_from_directory, url_for, request
from flask_hashing import Hashing
from flask_cors import CORS
import logging
from datetime import timedelta, datetime
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from db import Pedidos 
from db import Products as produtos
from db import Users
from db import Cards


app = Flask(__name__)
hashing = Hashing(app)

from datetime import datetime

agora = datetime.now()
print("Data e hora atuais do servidor:", agora)

# Configuração do CORS para aceitar o header Authorization
CORS(app, resources={r"/*": {"origins": "*"}}, expose_headers=["Authorization"])

# Configuração da chave secreta do JWT
logging.basicConfig(level=logging.DEBUG)
# Blueprints
productsroutes = Blueprint('products', __name__, url_prefix='/products')
pedidosroutes = Blueprint('Pedidos',__name__, url_prefix='/pedidos')
usersroute = Blueprint('users', __name__, url_prefix='/users')
cardsroutes = Blueprint('cards', __name__, url_prefix='/Cards')
   
#jwt config 
app.config['JWT_SECRET_KEY'] = 'a-string-secret-at-least-256-bits-long'  # Troque isso em produção
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=7)
app.config["JWT_COOKIE_CSRF_PROTECT"] = False
jwt = JWTManager(app)

@jwt.unauthorized_loader
def custom_unauthorized_response(callback):
    return jsonify({"error": "Token de acesso ausente ou inválido"}), 401

@jwt.invalid_token_loader
def custom_invalid_token_response(error):
    return jsonify({"error": "Token inválido"}), 422

@jwt.expired_token_loader
def custom_expired_token_response(jwt_header, jwt_payload):
    return jsonify({"error": "Token expirado"}), 401

# Rotas
@app.route('/images/<filename>')
def serve_image(filename):
    return send_from_directory('static/images', filename)

@app.route('/rota-protegida', methods=['GET'])
@jwt_required()
def rota_protegida():    
        usuario = get_jwt_identity()
        return jsonify(mensagem=f"Token válido! Bem-vindo, {usuario}"), 200

@usersroute.route('/cadastro', methods=['POST'])
def cadastro():
    user_data = request.get_json()
    new_user = user_data.get("newUser", [])[0]
    name = new_user.get("name")
    phone = new_user.get("phone")
    email = new_user.get("email")
    password = new_user.get("password")
    address = new_user.get("address")
    senha_hash = hashing.hash_value(password, salt='bcrypt')

    user = Users()
    iduser = user.new_user(name, phone, email, senha_hash, address)
    if(iduser):
        print(iduser)
        access_token = create_access_token(identity=str(iduser))
        return jsonify(access_token=access_token), 200

@usersroute.route('/login', methods=['POST'])
def login():
    user_data = request.get_json()
    login = user_data['login'][0]
    senha_hash = hashing.hash_value(login['password'], salt='bcrypt')
    user = Users()
    checked = user.checkuser (login['email'], senha_hash)
    # print(type(checked))
    if checked:
        access_token = create_access_token(identity=str(checked[0]))
        # print(app.config['JWT_SECRET_KEY'])
        return jsonify(access_token=access_token), 200

def get_user_data(id):
    user = Users()
    datauser = user.datafromuser(id)
    if datauser:
        return {
            "id": datauser[0],
            "name": datauser[1],
            "phone": datauser[2],
            "email": datauser[3],
            "address": datauser[4]
        }
    else:
        return None


@usersroute.route('/get-user/<int:id>', methods=['GET'])
# @jwt_required()
def datafromuser_route(id):
    user_data = get_user_data(id)
    if user_data:
        return jsonify(user_data)
    else:
        return jsonify({"error": "Usuário não encontrado"}), 404

    
def get_image_url(filename):
    return url_for('serve_image', filename=filename, _external=True)


def get_product_data(id):
    newprodutos = produtos()
    produto = newprodutos.select_product(id)
    if produto:
        return {
            "id": produto[0],
            "name": produto[1],
            "description": produto[2],
            "price": produto[3],
            "src": get_image_url(produto[4]),
            "special": produto[5],
            "long_description": produto[6]
        }
    else:
        return None

@productsroutes.route("/listar-produtos", methods=['GET'])
def listar_produtos():
    newprodutos = produtos()
    lista_produtos = newprodutos.select_all_products()
    return {
        "products": [
            {
                "id": p[0],
                "name": p[1],
                "description": p[2],
                "price": p[3],
                "src": get_image_url(p[4]),
                "special": p[5],
                "long_description": p[6]
            } for p in lista_produtos
        ]
    }

@productsroutes.route("/listar-produtos/<int:id>", methods=['GET'])
def listarproduto_unico(id):
    product_data = get_product_data(id)
    if product_data:
        return jsonify(product_data)
    else:
        return jsonify({"error": "Usuário não encontrado"}), 404

@productsroutes.route('/search' ,  methods=['GET'])
def searchproduct():
    produto_data = request.args.get('search')

    searchdata = produtos()
    result = searchdata.search(produto_data)
    return {
        "products": [
            {
                "id": p[0],
                "name": p[1],
                "description": p[2],
                "price": p[3],
                "src": get_image_url(p[4]),
                "special": p[5]
            } for p in result
        ]
    }
@pedidosroutes.route("/listar-pedidos/<int:id>", methods=['GET'])
def listar_pedididos(id):
    # print(userid)
    pedidos = Pedidos()
    Listarpedidos = pedidos.listar_pedidos(id)
    print(Listarpedidos)
    return {
        "pedidos": [
            {
                "pedido_id": item[0],
                "User": get_user_data(item[2]),
                "Product": get_product_data(item[1]),
                "Amount": item[3],
                "Status": item[4]
            }
            for item in Listarpedidos
        ]
    }

@pedidosroutes.route("/<int:id>/Amount", methods=['GET'])
def AttAmount(id):
    pedido = Pedidos()    
    Amount = request.headers.get('Amount')
    return jsonify(pedido.AttAmount(id,Amount))

@pedidosroutes.route("/<int:id>/remover", methods=['DELETE'])
def removepedido(id):
    pedido = Pedidos()    
    return jsonify(pedido.removerPedido(id))


@pedidosroutes.route("/newpedido", methods=['POST'])
def newpedido():
    pedido = Pedidos()    
    pedido_data = request.get_json()
    new_pedido = pedido_data.get("pedido", [])[0]
    Product = new_pedido.get("Product")
    User = new_pedido.get("User")
    Quant = new_pedido.get("Quant")

    return jsonify(pedido.newpedido(Product,User,Quant))

@cardsroutes.route('/<int:id>',methods=["GET"])
def ShowCards(id):
    cards = Cards()
    result = cards.ShowCards(id)

    return {
        "Cards": [
            {
                "CardId": c[0],
                "CardType": c[2],
                "Num": c[3],
                "Mes": c[4],
                "Ano": c[5],
                "CVV": c[6]
            } for c in result
        ]
    } 

@cardsroutes.route('/<int:id>',methods=["DELETE"])
def removecard(id):
    card = Cards()    
    return jsonify(card.removerCard(id))

@cardsroutes.route('/', methods=["POST"])
def newcard():
    card = Cards()    
    card_data = request.get_json()
    new_card = card_data.get("card", [])[0]
    User_id = new_card.get("User_id")
    CardType = new_card.get("CardType")
    Num = new_card.get("Num")
    Mes = new_card.get("Mes")
    Ano = new_card.get("Ano")
    CVV = new_card.get("CVV")
    Nome = new_card.get("Nome")
# user_id,CardType,Num,Mes,Ano,CVV,Nome
    return jsonify(card.newcard(User_id,CardType,Num,Mes,Ano,CVV,Nome))
# Registro dos Blueprints
app.register_blueprint(productsroutes)
app.register_blueprint(pedidosroutes)
app.register_blueprint(usersroute)
app.register_blueprint(cardsroutes)

if __name__ == "__main__":
    app.run(debug=True, port=5000)

from flask import Flask
from flask_restful import Api
from envs import env
from dotenv import load_dotenv

from resources.clube import Clubes, Clube, ClubeAdd


load_dotenv()

app = Flask(__name__)
# Configuração do banco caminho e nome do banco e é aqui que se eu quiser mudar o banco trocamos essa conf apenas
app.config["SECRET_KEY"] = env('SECRET_KEY')
app.config["SQLALCHEMY_DATABASE_URI"] = env('SQLALCHEMY_DATABASE_URI')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

api = Api(app)

# Aqui eu crio uma função para que ele crie o banco de dados antes da primeira requisição


@app.before_first_request
def cria_banco():
    banco.create_all()


# Registrando a biblioteca e criando as rotas da aplicação
api.add_resource(Clubes, '/clubes')
api.add_resource(ClubeAdd, '/clube-add')
api.add_resource(Clube, '/clube/<string:clube_id>')
# api.add_resource(Clube, '/clube/<string:clube_id>')

if __name__ == '__main__':
    # ===Importa o sql Alchemy aqui
    from sql_alchemy import banco
    banco.init_app(app)
    # ===============================
    app.run(debug=True)

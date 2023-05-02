from flask_restful import Resource, reqparse
from flasgger import swag_from

from models.clube import ClubeModel


class Clubes(Resource):
    # Retorna a lista complera de Clubes cadastrados
    @swag_from('clubes.yml')
    def get(self):
        return {'clubes': [clube.json() for clube in ClubeModel.query.all()]}

# CRUD


class Clube(Resource):
    args = reqparse.RequestParser()
    # args.add_argument('clube_id', type=int, required=True, help="Field 'clube_id' is required")
    args.add_argument('name', type=str, required=True,
                      help="Field 'Name' is required.")
    args.add_argument('city', type=str, required=True,
                      help="Field 'City' is required.")
    args.add_argument('state', type=str, required=True,
                      help="Field 'State' is required.")
    args.add_argument('logo', type=str, required=True,
                      help="Field 'Logo' is required.")

    # Recupera um Clube pelo seu ID
    def get(self, clube_id):
        if clube_id:
            clube = ClubeModel.find_clube(clube_id)
            if clube:
                return clube.json()
            return {'message': 'Clube not found'}, 404  # Status code not found

    def put(self, clube_id):
        dados = Clube.args.parse_args()
        clube_encontrado = ClubeModel.find_clube(clube_id)
        if clube_encontrado:
            clube_encontrado.update_clube(**dados)
            clube_encontrado.save_clube()
            return clube_encontrado.json(), 200  # Ok atualizado
        clube = ClubeModel(clube_id, **dados)
        # Senão cria
        try:
            clube.save_clube()
        except:
            # Internal server error
            return {'message': 'An internal error ocurred trying to save clube'}, 500
        return clube.json(), 201  # Status code 201 criado

    def delete(self, clube_id):
        clube = ClubeModel.find_clube(clube_id)
        if clube:
            try:
                clube.delete_clube()
            except:
                # Internal server error
                return {'message': 'An internal error ocurred trying to save clube'}, 500
            return {'message': 'Clube deleted successfully'}
        return {'message': "Clube '{}' not found".format(clube_id)}, 404

# CRUD INSERT


class ClubeAdd(Resource):
    args = reqparse.RequestParser()
    args.add_argument('name', type=str, required=True,
                      help="Field 'Name' is required.")
    args.add_argument('city', type=str, required=True,
                      help="Field 'City' is required.")
    args.add_argument('state', type=str, required=True,
                      help="Field 'State' is required.")
    args.add_argument('logo', type=str, required=True,
                      help="Field 'Logo' is required.")

    # Cria um novo Clube no Banco de dados
    def post(self):
        dados = Clube.args.parse_args()
        clube = ClubeModel(None, dados.name, dados.city,
                           dados.state, dados.logo)
        try:
            clube.save_clube()
        except:
            # internal error
            return {'message': 'An internal error occurred while saving'}, 500
        return clube.json()

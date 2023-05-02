from sql_alchemy import banco
# from ..utils.utils import Img_path

# Pegar o caminho do diretório de imagens
# img_path = Img_path()
# path_img = img_path.img()
# path_img = './src/img/'

# Model de Clubes de futebol de botão
class ClubeModel(banco.Model):
    # Nome da Tabela
    __tablename__ = 'clubes'
    
    # Colunas da Tabela para o mapeamento objeto relacional
    clube_id = banco.Column(banco.Integer, primary_key=True)
    name = banco.Column(banco.String(256))
    city = banco.Column(banco.String(256))
    state = banco.Column(banco.String(2))
    logo = banco.Column(banco.String(256))
    
    def __init__(self, clube_id, name, city, state, logo):
        self.clube_id = clube_id
        self.name = name
        self.city = city
        self.state = state
        self.logo = logo
    
    # Serializando os dados do banco de dados
    def json(self):
        return {
            'clube_id': self.clube_id,
            'name': self.name,
            'city': self.city,
            'state': self.state,
            'logo': self.logo
        }
    
    # Metodos para o CRUD
    @classmethod
    def find_clube(cls, clube_id):
        clube = cls.query.filter_by(clube_id=clube_id).first()
        if clube:
            return clube
        return None
    
    # Método para Salvar
    def save_clube(self):
        banco.session.add(self)
        banco.session.commit()
    
    # Método para update do clube no banco de dados
    def update_clube(self, name, city, state, logo):
        self.name = name
        self.city = city
        self.state = state
        self.logo = logo
    
    # Método que deleta o clube por id no banco de dados
    def delete_clube(self):
        banco.session.delete(self)
        banco.session.commit()
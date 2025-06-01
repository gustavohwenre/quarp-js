from .base import BaseModel

class Produto(BaseModel):
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

    def salvar(self):
        # Aqui viria lógica para salvar no banco
        print(f"Salvando produto: {self.nome}")

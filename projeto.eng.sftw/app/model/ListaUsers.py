class Usuario:
    def __init__(self, nome, email, cpf, telefone):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.telefone = telefone

    def mostrar_informacoes(self):
        return f"{self.nome} - {self.email} (CPF: {self.cpf})"

class UserRepo:
    def __init__(self):
        self.list_users = []

    def add_user(self, user: Usuario): 
        self.list_users.insert(0, user)

    def delete_user(self, index: int):
        if 0 <= index < len(self.list_users):
            self.list_users.pop(index)

    def get_users(self):
        return self.list_users

repo = UserRepo()
class Usuario():
    def __init__(self, name, credential, password):
        self._name = name
        self._credential = credential
        self._password = password
    
    def get_name(self):
        return self._name
    
    def get_credential(self):
        return self._credential
    
    def get_password(self):
        return self._password

class Registros():
    def __init__(self, Usuario):
        self.credenciais = []
    
    def cadastrar_usuarios(self, Usuario):
        self.credenciais.append(Usuario)
        print('Usuário Cadastrado!')
    
    def logar(self, login, senha):
        for dado in self.credenciais:
            if dado.get_credential() == login and dado.get_password() == senha:
                return True
            else:
                return False
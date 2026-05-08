import os
import time

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
    def __init__(self):
        self.credenciais = []
    
    def cadastrar_usuarios(self, Usuario):
        self.credenciais.append(Usuario)
        print('Usuário Cadastrado!')
    
    def logar(self, login, senha):
        for dado in self.credenciais:
            if dado.get_credential() == login and dado.get_password() == senha:
                return True
            else:
                continue

        return False

def menu():
    print('[1] - Login')
    print('[2] - Registre-se')
    pass

registros = Registros()
while(True):
    os.system('clear || cls')
    print('Faça o Login para acessar ou Registre-se!')
    menu()
    opcao = input('Digite a opção desejada: ')
    if not opcao.isdigit():
        print('Digite uma opção numérica válida!')
        time.sleep(1)
        continue

    if opcao == '1':
        credencial = input('Digite seu email ou usuário: ')
        senha = input('Digite sua senha: ')
        response = registros.logar(credencial, senha)

        if response:
            print('Acesso permitido. Bem vindo!')
            break
        else:
            print('Acesso Negado! Tente novamente ou cadastre-se.')
            time.sleep(1)
            

    elif opcao == '2':
        nome = input('Digite seu nome: ')
        credencial = input('Digite seu email ou usuário: ')
        senha = input('Digite sua senha: ')

        usuario = Usuario(
            name=nome,
            credential=credencial,
            password=senha
        )
        registros.cadastrar_usuarios(usuario)
        time.sleep(1)
        

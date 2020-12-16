from os import system, name
from time import sleep
import random


def cls():
    # para Windows
    if name == 'nt':
        _ = system('cls')


cls()

print("BEM VINDO AO SISTEMA DE CADASTRO\n")
cadastro = input("Digite [1] para se cadastrar: ")
if cadastro == '1':
    arquivo_nome = "C:/Users/COMPUTADOR/Desktop/FACULDADE/PROGRAMAÇÃO ESTRUTURADA/Login.txt"
    programa_nome = open(arquivo_nome, "r+")
    nome_usuario = []
    usuario = input("\nDigite seu nome de usuário: ").upper()
    if usuario in nome_usuario:
        nome_usuario = False
    else:
        nome_usuario.append(usuario)
        programa_nome.write(usuario)

    arquivo_senha = "C:/Users/COMPUTADOR/Desktop/FACULDADE/PROGRAMAÇÃO ESTRUTURADA/Senha.txt"
    programa_senha = open(arquivo_senha, "r+")
    senha_usuario = []
    senha = input("\nAgora crie sua senha: ").upper()
    if senha in senha_usuario:
        senha_usuario = False
    else:
        senha_usuario.append(senha)
        programa_senha.write(senha)

cls()

print("Salvando seus dados...")
sleep(2)

cls()

print("\n SEU CADASTRO FOI REALIZADO!\n")


login = input("\nDigite [0] para realizar seu login: ")
if login == '0':
    while True:
        usuario1 = input("\nDigite seu usuário de login: ").upper()
        while True:
            if usuario1 == usuario:
                senha1 = input("\nDigite sua senha: ").upper()
                if senha1 == senha:
                    sleep(2)
                    print("\nLogin efetuado com sucesso!")
                    exit(0)
                else:
                    novamente = str(input('\nSua senha está incorreta, deseja tentar novamente [S/N]? ')).upper()
                    if novamente != 'S':
                        exit(0)
            else:
                novamente1 = str(input('\nSeu usuário está incorreto, deseja tentar novamente [S/N]? ')).upper()
                if novamente1 != 'S':
                    exit(0)
                break
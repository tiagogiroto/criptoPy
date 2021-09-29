from cryptography.fernet import Fernet
import os, os.path
import sys

def funcao_criar_key():
    print("** A CHAVE SERA SALVA NO MESMO LOCAL DA APLICACAO **")

    # geração de chave   
    key = Fernet.generate_key()
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)

def funcao_descriptografar():
    #especificando caminho
    
    entrada_de_dados = input(" ** Digite o caminho da pasta de arquivos criptografados ** : \n")
    directory_files = (entrada_de_dados)

    files_and_directories = os.listdir(directory_files)

    # codigo para descripptografia
    for i in files_and_directories:
        with open('filekey.key', 'rb') as filekey:
            key = filekey.read()
            # usando a chave gerada
            fernet = Fernet(key)
            final_string_directory = directory_files + i;

            #decriptando arquivos
            with open(final_string_directory.replace('\\','/'), 'rb') as enc_file:
                encrypted = enc_file.read()
            decrypted = fernet.decrypt(encrypted)
            with open(final_string_directory.replace('\\','/'), 'wb') as dec_file:
                dec_file.write(decrypted)

def funcao_criptografar():
    # código ppara criptografia 
    entrada_de_dados = input(" ** Digite o caminho da pasta para criptografia ** : \n")

    # directory_files = entrada_de_dados
    files_and_directories = os.listdir(entrada_de_dados)

    for i in (files_and_directories) :

        # leitura da chave
        with open('filekey.key', 'rb') as filekey:
            key = filekey.read()
        fernet = Fernet(key)
        final_string_directory = entrada_de_dados + i;

        #selecionar arquivos
        with open(final_string_directory.replace('\\','/'), 'rb') as file:
            original = file.read()
            encrypted = fernet.encrypt(original)

        with open(final_string_directory.replace('\\','/'), 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

def sair():
    exit()

def main():

    print('-- DIGITE A OPÇÃO DESEJADA --')
    print(' 1 - Criar Chave criptografica ')
    print(' 2 - Descriptografar ')
    print(' 3 - Criptografar ')
    print(' 4 - Sair')

    entrada_de_dados = input("Digite o número da oppção desejada : \n")

    if entrada_de_dados == '1':
        funcao_criar_key()
    elif entrada_de_dados == '2':
        funcao_descriptografar()
    elif entrada_de_dados == '3':
        funcao_criptografar()
    else:
        sair()

if __name__ == "__main__":
    main()

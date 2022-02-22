from os.path import isfile, isdir, join
from time import sleep
import requests
import json
import os
import sys

# github.com/euMts
version = "1 - beta"

# escreve texto informado no arquivo filename.txt
# write some text in filename.txt
# Ex. textToFile("ola mundo!", "meuArquivo.txt")
def textToFile(text, filename):
    try:
        file = open(f"{filename}", "w")
        file.write(text)
        file.close()
        return {"status":"200"}
    except Exception as e:
        print(f"Error in textToFile\n{e}")
        return {"status":"error"}

# envia request contendo arquivo como parametro
# send the request w archive to the url
# Ex sendRequest("https://minhaApi.com/receber", "meuArquivo.pdf")
def sendRequest(url, filename):
    try:
        file = {"file": open(filename, "rb")}
        req = requests.post(url, files=file)
        return {
            "status":req.status_code,
            "response":req.json()
        }
    except Exception as e:
        print(f"Error in sendRequest\n{e}")
        return{
            "status":"error",
            "response":""
        }

# retorna quantidade e nomes de arquivos dentro de uma pasta
# returns the count and name of archives inside a folder
# Ex. getFiles("./")
def getFiles(myPath):
    try:
        onlyFiles = [file for file in os.listdir(myPath) if isfile(join(myPath, file))]
        return{
            "status":"200",
            "response":{
                "files_count":len(onlyFiles),
                "files":onlyFiles
            }
        }
    except Exception as e:
        print(f"Error in getFiles\n{e}")
        return{
            "status":"error",
            "response":""
        }

def main():
    print("Digite o número da operação desejada:")
    print("1 - Enviar arquivo único\n2 - Enviar todos os arquivos de uma pasta")
    option = input(">>> ")
    if option == "1":
        print("Opção selecionada: 1\nDigite o nome do arquivo a ser enviado para a API:\nEx. ./documento.pdf")
        file = input(">>> ")
        if isfile(file) == False:
            print("Arquivo não encontrado")
            input("Pressione ENTER para sair.")
            sys.exit()
        # url = ""
        url = input("Digite a url da api: ")
        print("Digite o nome do arquivo para armazenar a response:\nEx. responseDocumento.txt")
        fileName = input(">>> ")
        folderName = "RESPONSES"
        if isdir(folderName) == False:
            print(f"Pasta {folderName} não encontrada, criando..")
            os.system(f"mkdir {folderName}")
        responseFile = f"./{folderName}/response_{fileName}.txt"
        ###
        print(f"Enviando arquivo {file}")
        response = sendRequest(url, file)
        if response["response"] != "":
            print(f"Retorno recebido, armazenando response na pasta {folderName}")
            if isdir(folderName) == False:
                print(f"Pasta {folderName} não encontrada, criando..")
                os.system(f"mkdir {folderName}")
            textToFile(json.dumps(response["response"]["entities"], indent=4), responseFile) # response["response"] = response inteira
            print(f"Response armazenada como {responseFile}")   
            print("Finalizado")
        else:
            print("Timeout.")

    elif option == "2":
        success_count = 0
        print("Opção selecionada: 2\nDigite o nome da pasta que contém os arquivos a serem enviados para a API:\nEx. ./minhapasta")
        dir = input(">>> ")
        if isdir(dir) == False:
            print("Pasta não encontrada")
            input("Pressione ENTER para sair.")
            sys.exit()
        # url = ""
        url = input("Digite a url da api: ")
        folderName = "RESPONSES"
        print("As responses serão armazenadas na pasta RESPONSES")
        if isdir(folderName) == False:
            print(f"Pasta {folderName} não encontrada, criando..")
            os.system(f"mkdir {folderName}")
        ###
        files = getFiles(f"./{dir}")["response"]["files"]
        for x in range(len(files)):
            responseFile = f"./{folderName}/response_{files[x].split('.')[0]}.txt"
            if isfile(responseFile) == True:
                print(f"O arquivo '{responseFile}' já existe!")
                pass
            else:
                print(f"Enviando arquivo {files[x]}")
                response = sendRequest(url, f"{dir}/{files[x]}")
                if response["response"] != "":
                    print(f"Retorno recebido, armazenando response na pasta {folderName}")
                    textToFile(json.dumps(response["response"]["entities"], indent=4), responseFile) # response["response"] = response inteira
                    print(f"Response armazenada como {responseFile}")   
                    print(" ")
                    success_count += 1
                    sleep(2)
                else:
                    print(f"Timeout em {files[x]}")
            print(f"\nO retorno de {success_count} arquivos foi armazenado.\n")
    else:
        print(f"O número informado ({option}) não corresponde a uma alternativa.")
    input("Pressione ENTER para sair.")

if __name__ == "__main__":
    print(f"Rodando versão {version}\n")
    main()
import re
import pandas as pd
import os
import sys


def ler_nm_arq_entrada ():
    with open('@parametro.txt', 'r') as file:
     return (file.read().strip())


def stream_p1_quebra_texto_main():
    
    #### deleta o arquivo de origem ##########################
    path_deletar = os.path.join("dados")

    for arquivo in os.listdir(path_deletar):
        caminho_arquivo = os.path.join(path_deletar, arquivo)
        if os.path.isfile(caminho_arquivo):
            os.remove(caminho_arquivo)

    
    ## ler o arquivo txt e quebra em partes lógicas ####################
    arq_origem=ler_nm_arq_entrada()
    arq_origem=os.path.join('uploaded_files',arq_origem)
    with open(arq_origem, 'r') as file:
        relatorio = file.read()
        file.seek(0)
        relatorio_lista = file.readlines()


    w_count=0

    # #pattern = re.compile(r'BRASIL(.*?)BRASIL', re.DOTALL)
    # pattern = re.compile(r"BANCO CENTRAL DO BRASIL(.*?)BANCO CENTRAL DO BRASIL", re.DOTALL)
    # matches = re.findall(pattern, relatorio)

    # for match in matches:
    #     w_count=w_count+1
    # # start, end = match.span()
    #     filename = f'linha_{w_count}.txt'
    #     path = os.path.join("dados", filename)
    
    #     with open(path, 'w') as file:
    #         file.write(match)

    chunks = relatorio.split('\f')
    for i, chunk in enumerate(chunks):
        filename = f'linha_{i}.txt'
        path = os.path.join("dados", filename)
    
        with open(path, 'w') as file:
             file.write(chunk)

    
   # print(f'Chunk {i+1} foi salvo como {new_filename}')





    # #### extrai a parte final do arquivo pois não obedece ao padrao de quebra anterior
    # lines=[]
    # for line in reversed(relatorio_lista):
        
    #         if 'BANCO CENTRAL DO BRASIL' in line:
    #             lines.append(line)
    #             break
    #         else:
    #             lines.append(line)
    # path = os.path.join("dados", 'linha_final.txt')
    # with open(path, 'w') as arquivo:
    #     for linha in lines[::-1]:
    #         arquivo.write(linha)



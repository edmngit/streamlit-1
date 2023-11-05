import json
import pandas as pd

import sys

import os


def ler_nm_arq_entrada ():
    with open('@parametro.txt', 'r') as file:
     return (file.read().strip())


def read_json (lista_json,extension="json"):
    if extension=="json":   
        w_file_name=lista_json+".json"
    else:
        w_file_name=lista_json+"."+extension
        
    myfile = open(w_file_name, encoding='utf-8')     # Reading a UTF-8 file; 'r' is omitted
    result=json.load(myfile )
    return result

def save_json (lista_json,file_name_json,extension="json"):
   # https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/
    if extension=="json":   
        w_file_name=file_name_json+".json"
    else:
        w_file_name=file_name_json+"."+extension
    
    with open(w_file_name, 'w',encoding='utf-8') as f:
     result=json.dumps(lista_json,indent=4,ensure_ascii=False)
     #json.dump(lista_json,f)//
     f.write(result)


def stream_p3_gera_json():
    ## ler o arquivo json
    filename = ler_nm_arq_entrada ()
    filename_without_extension = os.path.splitext(filename)[0]

    dados_originais = read_json (filename_without_extension)

    #sys.exit()

    # Passo 2: Criar a nova lista de dados
    novos_dados = []
    for dado in dados_originais:
        for detalhe in dado["detalhe"]:
            novo_objeto = {
                "nm_arq": dado["nm_arq"],
                "cod_bem": dado["cod_bem"],
                "descr_geral": dado["descr_geral"],
                "setor": dado["setor"],
                "cod_item": detalhe["cod_item"],
                "descr_curta": detalhe["descr_curta"],
                "matricula": detalhe["matricula"]
            }
            novos_dados.append(novo_objeto)

    # Passo 3: Escrever os novos dados no formato do arquivo_2
    #arquivo_2 = json.dumps(novos_dados, indent=4)  # 'indent=4' adiciona uma indentação para facilitar a leitura.

    save_json(novos_dados,'resultado3')


    nm_plan=filename_without_extension+'.xlsx'
    df = pd.DataFrame(data=novos_dados)

    df.to_excel(nm_plan, index=False)




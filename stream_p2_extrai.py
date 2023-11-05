import os
import re
import pandas as pd
import json


def ler_nm_arq_entrada ():
    with open('@parametro.txt', 'r') as file:
     return (file.read().strip())
    
 

def save_json(lista_json,file_name_json,extension="json"):
   # https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/
    if extension=="json":   
        w_file_name=file_name_json+".json"
    else:
        w_file_name=file_name_json+"."+extension
    
    with open(w_file_name, 'w',encoding='utf-8') as f:
     result=json.dumps(lista_json,indent=4,ensure_ascii=False)
     #json.dump(lista_json,f)//
     f.write(result)


def captura_cod_bem (conteudo):

   pattern = re.compile(r'\d{4}\.\d\.\d{2}\.\d{2}\.\d')
   match = pattern.search(conteudo)
   if match:
     #print("Primeira ocorrência encontrada:")
     return (match.group(0))
   else:
     return ("indefinido")

   
def captura_descr_geral (conteudo):

   pattern = re.compile(r'\d{4}\.\d\.\d{2}\.\d{2}\.\d\s+(.+)')
   match = pattern.search(conteudo)
   if match:
     #print("Primeira ocorrência encontrada:")
     return (match.group(1).strip())
   else:
     return ("indefinido")


def captura_setor (conteudo):

  #pattern = r'\s+-+\s*([a-zA-Z0-9]+/[a-zA-Z0-9]+/[a-zA-Z0-9]+)\s*-+'
  pattern = r'-+\s*(.*/.*/[a-zA-Z0-9__\-\.]+)\s*-+' 
  match = re.search(pattern, conteudo)
  if match:
    return(match.group(1))
  


def captura_matricula (linha):

  pattern = r'\d{1,2}\.\d{3}\.\d{3}-\w' 
  match = re.search(pattern, linha)
  if match:
      return match.group(0)



def captura_descr_curta (linha):

        pattern = r'\d{3}\.\d{3}-\d'
        match = re.search(pattern, linha)
        if match:
          return (linha[10:90].strip())  



def captura_detalhes (conteudo):

   lista_detalhe=[]
   
   for linha in conteudo.splitlines():
        pattern = r'\d{3}\.\d{3}-\d'
        match = re.search(pattern, linha)
        if match:
          #print("Primeira ocorrência encontrada:")
          cod_item=  match.group(0).strip()

          dict_detalhe=dict(
                      # cod_bem= cod_bem,
                      # descr_geral=descr_geral,
                      # setor=setor,
                       cod_item=cod_item ,
                       descr_curta=captura_descr_curta(linha),
                       matricula=captura_matricula (linha)
                      )   

          lista_detalhe.append(dict_detalhe)
   
   return lista_detalhe
   
##########################################################
############# Inicio do Programa #########################   
##########################################################
def stream_p2_extrai_main():

  diretorio = './dados'
  w_count=0

  lista=[]

  ####### Realiza loop de leitura dos pedaços dos arquivos #######################

  for nome_arquivo in os.listdir(diretorio):
      if nome_arquivo.endswith('.txt'):
          caminho_arquivo = os.path.join(diretorio, nome_arquivo)
          
          with open(caminho_arquivo, 'r') as arquivo:
              conteudo = arquivo.read()
              print (caminho_arquivo)

              # captura cabeçalho e linha de detalhe
              dict_parte=dict(
                      texto=conteudo,   # texto objeto da análise
                      nm_arq = nome_arquivo,
                      cod_bem= captura_cod_bem(conteudo),  #campo de cabeçalho
                      descr_geral=captura_descr_geral(conteudo),  #campo de cabeçalho
                      setor=captura_setor(conteudo), #campo de cabeçalho
                      detalhe=captura_detalhes (conteudo) #captura linha detalhe (retorna lista de dicionário)
                      )
              
              lista.append(dict_parte)

  
  #   w_count = w_count +1    



  filename = ler_nm_arq_entrada ()
  filename_without_extension = os.path.splitext(filename)[0]

  save_json(lista_json=lista,file_name_json=filename_without_extension)
      

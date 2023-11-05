import streamlit as st
import re
import io
import os


# def save_json(lista_json,file_name_json,extension="json"):
#    # https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/
#     if extension=="json":   
#         w_file_name=file_name_json+".json"
#     else:
#         w_file_name=file_name_json+"."+extension
    
#     with open(w_file_name, 'w',encoding='utf-8') as f:
#      result=json.dumps(lista_json,indent=4,ensure_ascii=False)
#      #json.dump(lista_json,f)//
#      f.write(result)





# def process_quebra_file(file):
# ## ler o arquivo txt e quebra em partes lógicas ####################
#     file_content = file.read().decode('ISO-8859-1')
#     pattern = re.compile(r"BANCO CENTRAL DO BRASIL(.*?)BANCO CENTRAL DO BRASIL", re.DOTALL)
#     matches = re.findall(pattern, file_content)
    
#     #st.write(type(file))
#     file.seek(0)
#     relatorio_lista = file.readlines()
#     st.write(type(relatorio_lista))

#     w_count = 0

#     for match in matches:
#         w_count=w_count+1
   
#         filename = f'linha_{w_count}.txt'
#         path = os.path.join("dados", filename)
    
#         with open(path, 'w') as file:
#             file.write(match)

#     #### extrai a parte final do arquivo pois não obedece ao padrao de quebra anterior
#     lines=[]
#     for line in reversed(relatorio_lista):
        
#             if 'BANCO CENTRAL DO BRASIL' in line:
#                 lines.append(line)
#                 break
#             else:
#                 lines.append(line)
#     path = os.path.join("dados", 'linha_final.txt')
#     with open(path, 'w') as arquivo:
#         for linha in lines[::-1]:
#             arquivo.write(linha)



import stream_p1_quebra_texto as p1
import stream_p2_extrai as p2
import stream_p3_gera_json as p3

def download_planilha():
    
    with open('@parametro.txt', 'r') as file:
      #file.read().strip()
      #file_name_without_extension = os.path.splitext(file_name_with_extension)[0]
      file_name_plan = os.path.splitext(file.read().strip())[0] +'.xlsx'
    
   
    st.title('Download de Arquivo no Streamlit')

    # Caminho para o arquivo .xlsx
    #file_path = os.path.join ()

    # Verificar se o arquivo existe
    if os.path.exists(file_name_plan):
        
        # Botão de download para o arquivo .xlsx
        with open(file_name_plan, "rb") as file:
            btn = st.download_button(
                label="Download .xlsx file",
                data=file,
                file_name=file_name_plan,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )
            save_path = 'download'
           # st.success(f"Arquivo {file_name_plan} salvo em {save_path}!")

            if btn:
                st.success('Iniciando download...')
    else:
        st.warning("O arquivo não foi encontrado.")





def upload_arquivo():
    # Criando um diretório para salvar os arquivos, se ele não existir
    save_path = 'uploaded_files'
    if not os.path.isdir(save_path):
        os.makedirs(save_path)

    # Título da aplicação na página web
    st.title('Upload de Arquivo no Streamlit')

    # File uploader permite ao usuário fazer upload de um arquivo
    uploaded_file = st.file_uploader("Por favor, faça upload de um arquivo .txt", type="txt")

    # Verificar se um arquivo foi carregado
    if uploaded_file is not None:
        # Lendo o conteúdo do arquivo
        file_content = uploaded_file.read().decode('ISO-8859-1')
     
        
        # Exibir as primeiras linhas do arquivo na tela
        st.write("Preview do Conteúdo do Arquivo:")
        st.write(file_content[:100])  # Assumindo que você quer ver os primeiros 100 caracteres
        
        # Salvando o arquivo
        with open(os.path.join(save_path, uploaded_file.name), "w") as f:
            f.write(file_content)
        
        st.success(f"Arquivo {uploaded_file.name} salvo em {save_path}!")


        #salva nome do arquivo no arquivo de parametro
        
        with open('@parametro.txt', 'w') as file:
          file.write(uploaded_file.name)


        #processa o arquivo
        p1.stream_p1_quebra_texto_main()
        p2.stream_p2_extrai_main()
        p3.stream_p3_gera_json()

        download_planilha()


w_streamlit = True

if w_streamlit == True:
 upload_arquivo()

else:
    #execute o codigo abaixo para processar a geração da planilha de padrões por fora do streamlit
    p1.stream_p1_quebra_texto_main()
    p2.stream_p2_extrai_main()
    p3.stream_p3_gera_json()


















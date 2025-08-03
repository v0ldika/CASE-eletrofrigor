from os.path import exists
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

# ler os arquivos separadamente
pd.set_option('display.max_columns', None)
df1 = pd.read_csv("D:\Projeto\.venv\documentos\Empresa A - Copia.csv", sep = ";")
df2 = pd.read_csv("D:\Projeto\.venv\documentos\Empresa B.csv", sep = ";")
df3 = pd.read_csv("D:\Projeto\.venv\documentos\Empresa C.csv", sep = ";")

#tratamento de dados

# tranformar em data

df1['Data venda'] = pd.to_datetime(df1['Data venda'], errors='coerce')
df2['Data venda'] = pd.to_datetime(df2['Data venda'], errors='coerce')
df3['Data venda'] = pd.to_datetime(df3['Data venda'], errors='coerce')

#transformar em float valor

df1['Valor'] = df1['Valor'].str.replace(',', '.').astype(float)
df2['Valor'] = df2['Valor'].str.replace(',', '.').astype(float)
df3['Valor'] = df3['Valor'].str.replace(',', '.').astype(float)


# verificar valores se tem nan ou 0

total_nulos1 = (df1["Valor"].fillna(0) == 0).sum()
total_nulos2 = (df2["Valor"].fillna(0) == 0).sum()
total_nulos3 = (df3["Valor"].fillna(0) == 0).sum()


print("Total de nulos na A :", total_nulos1)
print("Total de nulos na B :", total_nulos2)
print("Total de nulos na C :", total_nulos3)

# configurar as informações de conexão com o banco de dados
user = 'root'
password = 'Vini2001'
host = "localhost"
database = 'case_eletrofrigor'

# criar conexão
engine_string = f'mysql+mysqlconnector://{user}:{password}@{host}/{database}'
engine = create_engine(engine_string)
print(f"String de conexão a ser usada: {engine_string}")
try:
    # enviar o df da Empresa A
    with engine.connect() as conn:
        df1.to_sql('vendas_empresa_a', con=conn, if_exists='replace', index=False)
        print("df da Empresa A enviado com sucesso para o MySQL.")

    # enviar o df da Empresa B
    with engine.connect() as conn:
        df2.to_sql('vendas_empresa_b', con=conn, if_exists='replace', index=False)
        print("df da Empresa B enviado com sucesso para o MySQL.")

    # enviar o df da Empresa C
    with engine.connect() as conn:
        df3.to_sql('vendas_empresa_c', con=conn, if_exists='replace', index=False)
        print("df da Empresa C enviado com sucesso para o MySQL.")



except Exception as e:
    print(f"Ocorreu um erro: {e}")


# a tabela com todas as informacoes juntas concatenadas vai ser criada em sql por se tratar de uma grande volume de dados
Projeto de Análise de Dados: EletroFrigor
Este projeto tem como objetivo principal unificar e analisar dados de vendas de três empresas (Empresa A, Empresa B e Empresa C), consolidando-os em um banco de dados MySQL para facilitar análises futuras.

Visão Geral do Projeto
O script em Python realiza o seguinte fluxo de trabalho:

Extração de Dados: Lê os arquivos CSV das três empresas.

Tratamento e Limpeza:

Converte as colunas de data (Data venda) para o formato de data correto.

Transforma os valores de venda (Valor) em formato numérico (float), substituindo vírgulas por pontos.

Verifica a quantidade de valores nulos ou zero na coluna Valor de cada DataFrame.

Carregamento de Dados (ELT): Conecta-se a um banco de dados MySQL (case_eletrofrigor) e insere os dados de cada empresa em suas respectivas tabelas (vendas_empresa_a, vendas_empresa_b, vendas_empresa_c).

A consolidação final dos dados em uma única tabela será realizada diretamente no SQL, otimizando o processamento para um grande volume de informações.
###################
Tecnologias Utilizadas
Python: Linguagem principal do projeto.

pandas: Biblioteca utilizada para manipulação e tratamento de dados.

SQLAlchemy: Toolkit de SQL para interagir com o banco de dados.

mysql-connector-python: Driver para conexão com MySQL.

MySQL: Sistema de gerenciamento de banco de dados relacional.
###################
Como Executar o Projeto
Para rodar este script localmente, siga os passos abaixo:

Bash

pip install pandas sqlalchemy mysql-connector-python
Configuração do Banco de Dados:

Criei um banco de dados chamado case_eletrofrigor no seu servidor MySQL.

No script Python, ajuste as variáveis de conexão com o banco de dados (user, password, host, database) para corresponder às suas credenciais.

Estrutura de Arquivos:

Coloque os arquivos CSV (Empresa A - Copia.csv, Empresa B.csv, Empresa C.csv) no caminho especificado pelo script. Certifique-se de que o caminho D:\Projeto\.venv\documentos\ está correto, ou ajuste-o conforme a sua estrutura de diretórios.

Execute o script:

Bash

python main.py


Contribuição
Sinta-se à vontade para abrir issues ou enviar pull requests para melhorias. Contribuições são sempre bem-vindas!

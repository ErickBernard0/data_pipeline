
#### PACOTES
import pandas as pd
import os

#### FUNCAO LEITURA
def leitura_dados(dados):
    if dados.endswith('.json'):
        return pd.read_json(dados)
    else:
        return pd.read_csv(dados)

#### NORMALIZANDO DADOS
def normalizar_dados(df1, df2):
    if df1.shape[1] >= df2.shape[1]:
        df_maior = df1
        df_menor = df2
    else:
        df_maior = df2
        df_menor = df1    
    # Renomear as colunas do DataFrame menor para corresponder ao DataFrame maior
    df_menor.columns = df_maior.columns[:df_menor.shape[1]]    
    # Juntando df's
    df_empresas = pd.concat([df_maior, df_menor], ignore_index=True, sort=False)
    # Retornando df normalizado
    return df_empresas

#### SALVANDO ARQUIVO
def salvando_arquivo(df_final):
    try:
        df_final.to_csv('data/context/dados_empresas.csv', index=False)
        print("Arquivo salvo com sucesso")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

#### LOCAL DO ARQUIVO
path_data_empresa_a = 'data/raw/dados_empresaA.json'
path_data_empresa_b = 'data/raw/dados_empresaB.csv'    

#### CARREGANDO DADOS
try:
    df_empresa_a = leitura_dados(path_data_empresa_a)
    df_empresa_b = leitura_dados(path_data_empresa_b)
    
    # NORMALIZANDO DADOS
    df_empresas = normalizar_dados(df_empresa_a, df_empresa_b)
    
    # SALVANDO ARQUIVO
    salvando_arquivo(df_empresas)

except Exception as e:
    print(f"Erro durante o processamento dos dados: {e}")
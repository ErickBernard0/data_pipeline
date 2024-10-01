import pandas as pd

class DataProcessor:
    def __init__(self, path_a, path_b, output_path):
        self.path_data_empresa_a = path_a
        self.path_data_empresa_b = path_b
        self.output_path = output_path
        self.df_empresa_a = None
        self.df_empresa_b = None

    def leitura_dados(self, dados):
        if dados.endswith('.json'):
            return pd.read_json(dados)
        else:
            return pd.read_csv(dados)

    def carregar_dados(self):
        try:
            self.df_empresa_a = self.leitura_dados(self.path_data_empresa_a)
            self.df_empresa_b = self.leitura_dados(self.path_data_empresa_b)
        except Exception as e:
            print(f"Erro durante o carregamento dos dados: {e}")

    def normalizar_dados(self):
        try:
            if self.df_empresa_a.shape[1] >= self.df_empresa_b.shape[1]:
                df_maior = self.df_empresa_a
                df_menor = self.df_empresa_b
            else:
                df_maior = self.df_empresa_b
                df_menor = self.df_empresa_a    
            
            # Renomear as colunas do DataFrame menor
            df_menor.columns = df_maior.columns[:df_menor.shape[1]]    
            # Juntando os DataFrames
            df_empresas = pd.concat([df_maior, df_menor], ignore_index=True, sort=False)
            return df_empresas
        except Exception as e:
            print(f"Erro durante a normalização dos dados: {e}")
            return None

    def salvando_arquivo(self, df_final):
        try:
            df_final.to_csv(self.output_path, index=False)
            print("Arquivo salvo com sucesso")
        except Exception as e:
            print(f"Erro ao salvar o arquivo: {e}")

    def processar_dados(self):
        self.carregar_dados()
        df_empresas = self.normalizar_dados()
        if df_empresas is not None:
            self.salvando_arquivo(df_empresas)


# Definindo os caminhos dos arquivos
path_data_empresa_a = 'data/raw/dados_empresaA.json'
path_data_empresa_b = 'data/raw/dados_empresaB.csv'    
output_path = 'data/context/dados_empresas.csv'

# Criando uma instância da classe e processando os dados
data_processor = DataProcessor(path_data_empresa_a, path_data_empresa_b, output_path)
data_processor.processar_dados()

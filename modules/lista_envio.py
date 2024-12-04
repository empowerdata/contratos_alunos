import pandas as pd

def cria_lista_envio(nome_arquivo):
    colunas = ['nome contato', 'email contato', 
               'nome produto', 'valor venda', 
               'pagamento', 'parcelas',
               'data aprovacao']
    df = pd.read_excel(nome_arquivo)
    df['nome produto'] = df['nome produto'].str.replace('00 - ', '')
    df = df[colunas]
    return df.drop_duplicates()
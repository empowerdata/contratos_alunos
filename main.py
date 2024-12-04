from modules.postmark import postmark_send_email
from datetime import datetime
from modules.lista_envio import cria_lista_envio

# configure o nome do arquivo da lista de contatos
nome_lista_envio = "alunos-24-12-04.xlsx"

data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

if __name__ == '__main__':
    lista = cria_lista_envio(f"listas_envio/{nome_lista_envio}")

    for _, row in lista.iterrows():
        
        # realiza o envio do e-mail
        postmark_send_email(row['nome contato'], 
                            row['email contato'],
                            row['nome produto'],
                            row['valor venda'],
                            row['pagamento'],
                            row['data aprovacao'][:10],
                            data_hora) 
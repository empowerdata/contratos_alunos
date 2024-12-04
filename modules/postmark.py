from postmarker.core import PostmarkClient
from modules.database import insert_db

postmark = PostmarkClient(server_token="5a48b95a-c91e-4249-a3ed-3b3424a3b649")

def postmark_send_email(nome, email_aluno, produto, valor, pagamento, data_compra, data_hora):
    try:
        email = postmark.emails.Email(
            From="plataforma@empowerdata.com.br",
            To=email_aluno,
            Cc="assinaturas@empowerdata.com.br",
            Subject=f"Contrato Empowerdata - {nome}",
            HtmlBody=f"""<p>Olá <strong>{nome}</strong>,</p>
            <p>Estamos entrando em contato para enviar o contrato de compra de acesso à nossa plataforma.<br/> 
            O contrato encontra-se anexo e abaixo estão os detalhes da sua inscrição: </p>
            
            <p>
                <strong>Nome: </strong>{nome}<br/>
                <strong>Produto: </strong>{produto}<br/>
                <strong>Valor: </strong>R$ {valor}<br/>
                <strong>Forma de Pagamento: </strong>{pagamento}<br/>
                <strong>Data da Compra: </strong> {data_compra}<br/>
                <strong>Prazo de Acesso: </strong> 1 ano<br/><br/>
           
                É um prazer ter você junto com a gente nessa jornada. Bons estudos!<br/>                
                Qualquer dúvida, entre em contato pelo WhatsApp com o nosso time de CS: <strong>(22) 99802-3538</strong>
                ou através do e-mail <strong>suporte@empowerdata.com.br</strong><br/><br/>
                
                Atenciosamente,<br/>Time Empowerdata
            """
        )
        email.attach('contrato.pdf')
        # email.attach_binary(content=b'content', filename='contrato.pdf')
        email.send()

        # insere os dados no banco de dados
        insert_db(nome, email_aluno, "Acesso completo", data_hora, 'sucesso')

    except Exception as e:
        # insere os dados no banco de dados
        insert_db(nome, email_aluno, "Acesso completo", data_hora, 'erro no envio')
        
        with open('logs/log_postmark.txt', 'a') as file:
            file.write(f"Erro ao tentar enviar contrato para {email}: {e}.\n\n")
            

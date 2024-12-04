from sqlalchemy import create_engine, text

usuario = "empowerbot"
senha = "Empower#2023"
host = "147.182.244.229"
porta = 3306
banco_de_dados = "empowerbot"

def insert_db(nome_aluno, email_aluno, produto, dt_envio, status):
    try:
        engine = create_engine(f"mysql+pymysql://{usuario}:{senha}@{host}:{porta}/{banco_de_dados}")
        with engine.connect() as conn:
            conn.execute(
                text(f"INSERT INTO contrato_alunos VALUES ('{nome_aluno}', '{email_aluno}', '{produto}', '{dt_envio}', '{status}')")
            )
            conn.commit()

    except Exception as e:
        with open('logs/log_bd.txt', 'a') as file:
            file.write(f"Erro ao tentar inserir {email_aluno} no BD: {e}.\n\n")
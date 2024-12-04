Use o TMUX para rodar o script:

- crie um novo terminal: `tmux new -s contratos`
- execute o comando: `poetry run python main.py`
- saia do terminal e deixe o comando executando: `CTRL B e depois D`
- para voltar ao terminal: `tmux attach -t contratos`
- para elimiar o terminal tmux: `tmux kill-session -t contratos`

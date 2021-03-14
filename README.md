# Dólar Canadense Bipolar

Um bot que de vez em quando tweeta a cotação do Dólar Canadense para o Real

## Instalando o Repositório

1. Abra a linha de comando, entre na pasta raiz desse projeto e crie um ambiente virtual com `python -m venv venv`
2. Instale as bibliotecas das dependências usando `pip install -r requirements.txt`
3. Crie um arquivo `auth_tokens.py` na pasta `utils` e coloque suas credenciais de API do Twitter dessa maneira:

```python
TWITTER_API_KEY = "sua_chave_da_api"
TWITTER_API_KEY_SECRET = "sua_chave_secreta_da_api"

TWITTER_ACCESS_TOKEN = "seu_token_de_acesso"
TWITTER_ACCESS_TOKEN_SECRET = "seu_token_de_acesso_secreto"
```
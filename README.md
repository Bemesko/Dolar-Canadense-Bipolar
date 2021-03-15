# Dólar Canadense Bipolar v.1.0.0

Um bot open-source que de vez em quando tweeta a cotação do Dólar Canadense para o Real!

Me veja em ação em [@dolarCA_bipolar](https://twitter.com/dolarCA_bipolar)

<blockquote class="twitter-tweet"><p lang="pt" dir="ltr">🇨🇦 Subiu! 😯 - R$ 4.46 às 22:20 <br> <br>Triste<br><br>variação 📈 + 0.12% (R$ 0.54)</p>&mdash; Dólar Canadense Bipolar 🇨🇦 (@dolarCA_bipolar) <a href="https://twitter.com/dolarCA_bipolar/status/1371270326412263425?ref_src=twsrc%5Etfw">March 15, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

## Instalando o Repositório

1. Abra a linha de comando, entre na pasta raiz desse projeto e crie um ambiente virtual com `python -m venv venv`
2. Instale as bibliotecas das dependências usando `pip install -r requirements.txt`
3. Crie um arquivo `auth_tokens.py` na pasta `utils` e coloque suas credenciais de API do Twitter dessa maneira (se você não sabe como fazer isso pode dar uma olhada [aqui](https://realpython.com/twitter-bot-python-tweepy/#creating-twitter-api-authentication-credentials)):

```python
TWITTER_API_KEY = "sua_chave_da_api"
TWITTER_API_KEY_SECRET = "sua_chave_secreta_da_api"

TWITTER_ACCESS_TOKEN = "seu_token_de_acesso"
TWITTER_ACCESS_TOKEN_SECRET = "seu_token_de_acesso_secreto"
```
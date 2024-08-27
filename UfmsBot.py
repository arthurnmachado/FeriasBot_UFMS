import tweepy
import datetime
import os
import dotenv

dotenv.load_dotenv()  # Carrega as variáveis de ambiente

access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']
bearer_token = os.environ['BEARER_TOKEN']
api_key = os.environ['API_KEY']
api_secret = os.environ['API_SECRET']

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuthHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Dicionário com as datas de férias (chave: instituição, valor: data)
ferias_dict = {
    "UFMS": datetime.date(2024, 12, 8),
    "UCDB": datetime.date(2024, 12, 17),
    "UNIDERP": datetime.date(2024, 12, 7),
}

agora = datetime.date.today()  # Computa o dia de hoje

for instituicao, ferias in ferias_dict.items():
    fdias_horas = ferias - agora  # Diferença entre os dias colocados anteriormente (Tempo para as ferias)
    fdias = fdias_horas.days  # Agora pegamos somente os dias

    # Verifica se a data já passou
    if agora > ferias:
        continue

    # Mensagem base
    if fdias == 0:
        message = f"ATENÇÃO: COMEÇARAM AS FÉRIAS DA {instituicao}!!!"
    elif fdias == 1:
        message = f"Falta 1 dia para as férias da {instituicao}!!!"
    else:
        # Mensagem para múltiplos de 10 ou outros dias
        if (fdias % 10) == 0:
            message = f"Faltam {fdias} dias para as férias da {instituicao}!!!"
        else:
            message = f"Faltam {fdias} dias para as férias da {instituicao}"

    client.create_tweet(text=message)  # Cria o tweet
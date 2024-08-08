### Bot versão 2.0 (atualizada para o novo twitter (X))

import tweepy
import datetime
import os
import dotenv

dotenv.load_dotenv() # Carrega as variáveis de ambiente

access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']
bearer_token = os.environ['BEARER_TOKEN']
api_key = os.environ['API_KEY']
api_secret = os.environ['API_SECRET']

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuthHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

ferias = datetime.date(2024,12,8) # Coloque aqui a data do início das férias no modelo (ANO,MES,DIA)
agora = datetime.date.today() # Computa o dia de hoje

fdias_horas = ferias - agora # Diferença entre os dias colocados anteriormente (Tempo para as ferias)
fdias = fdias_horas.days  # Agora pegamos somente os dias

# Temos que separar o caso em que falta apenas 1 dia, para poder mudar "dias" para "dia" no tweet

inicio = datetime.date(2023,8,7)

if agora >= inicio:

    if fdias > 1:

        if fdias % 10 == 0: #Testando para ver se o dia é um multiplo de 10
            client.create_tweet(text = ("Faltam " + str(fdias) + " dias para as férias da UFMS!!!") )

        if fdias % 10 != 0: #Testando para ver se o dia é um multiplo de 10
            client.create_tweet(text = ("Faltam " + str(fdias) + " dias para as férias da UFMS") )


    if fdias == 1:
        client.create_tweet(text = ("Falta " + str(fdias) + " dia para as férias da UFMS!!!") )


    if fdias == 0:
        client.creat_tweet(text = ("ATENÇÃO: COMEÇARAM AS FÉRIAS DA UFMS!!!") )
        
else:
    quit()
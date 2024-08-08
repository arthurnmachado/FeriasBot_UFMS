# FeriasBot_UFMS

:snake: Esse é um bot escrito em Python 3.8 com o obejetivo de twittar todo dia dizendo quantos dias faltam para as férias na USP. 

O código que utilizei pode se encontrado aqui, e é muito simples pois utiliza a biblioteca (datetime) do Python, que tem uma função para calcular o dia atual e uma função em que eu coloco manualmente a data de término das aulas. Consequentemente os dias que faltam para as férias são definidos como a diferença entre estes dois.


O perfil do Bot no twitter pode ser achado por [@ufms_ferias](https://twitter.com/ufms_ferias) e está hospedado no site [pythonanywhere](https://www.pythonanywhere.com), em que é programado para rodar o mesmo código todos os dias às 11:00 da manhã.

Aproveitem :)

## Instalação e configuração

Caso você queira rodar o bot em sua máquina, basta:

- Criar um ambiente virtual rodando o comando:

```bash
python -m venv /caminho/para/novo/ambiente/virtual
```

- Ativar o ambiente com o comando:

```bash
source .venv/bin/activate
```

- Instalar as bibliotecas necessárias com:

```bash
pip install -r requirements.txt
```

Para definir as variáveis de ambiente, basta:

- Copiar o `.env.example` em `.env`:

```bash
cp .env.example .env
```

- E, por fim, definir os valores dentro do arquivo `.env`:

```
ACCESS_TOKEN = 'XXXXXXXXXXXXXXX'
ACCESS_TOKEN_SECRET = 'YYYYYYYYYYYYYY'
BEARER_TOKEN = 'ZZZZZZZZZZZZ'
API_KEY = 'WWWWWWWWWWWWWWW'
API_SECRET = 'BBBBBBBBBBBBBBB'
```
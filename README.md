# API de Tradução com Flask e Redis

Esta é uma API de tradução simples criada com o framework Flask que utiliza um serviço de tradução externo (Rapid Translate, neste exemplo) e cache com Redis para armazenar traduções previamente solicitadas. Os endpoints disponíveis são:

- `/translate`: Traduz um texto de um idioma para outro.
- `/translate_cache`: Utiliza o cache do Redis para retornar traduções

## Pré-requisitos

Antes de começar, certifique-se de ter o seguinte instalado em sua máquina:

- Python 3.x
- Flask
- Redis
- Bibliotecas Python: requests, redis

## Instalação

1. Clone este repositório para sua máquina local:

   ```bash
   git clone https://github.com/seu-usuario/api-traducao-flask-redis.git


## Execução

Para iniciar o serviço Redis com o Docker Compose, siga estas etapas:

Certifique-se de ter o Docker e o Docker Compose instalados em seu sistema.

No terminal, execute o seguinte comando:
`docker-compose up -d`

O Docker Compose irá criar e iniciar um contêiner Redis local usando as configurações definidas no arquivo docker-compose.yml. 
O Redis estará disponível em localhost:6379.


Para iniciar o aplicativo, execute o seguinte comando:
`make api`

Isso iniciará o servidor Flask e tornará os endpoints /translate e /translate_cache acessíveis em http://localhost:5000.

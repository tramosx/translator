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
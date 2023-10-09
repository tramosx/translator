import os

# Configurações da API de Tradução
RAPIDAPI_API_KEY = os.environ.get('RAPIDAPI_API_KEY', 'SUA-CHAVE-AQUI')
TRANSLATION_API_URL = 'https://rapid-translate.p.rapidapi.com/TranslateText'

# Configurações do Redis
REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
REDIS_PORT = os.environ.get('REDIS_PORT', '6379')
REDIS_DB = os.environ.get('REDIS_DB', '0')

# Tempo de cache em segundos (1 hora)
CACHE_EXPIRATION = 3600
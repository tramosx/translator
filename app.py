from flask import Flask, request, jsonify
import requests
import redis

from config import RAPIDAPI_API_KEY, TRANSLATION_API_URL, REDIS_HOST, REDIS_PORT, REDIS_DB, CACHE_EXPIRATION


app = Flask(__name__)
redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)


@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    language_from = data.get('language_from')
    language_to = data.get('language_to')
    text = data.get('text')
    
    
    headers = {
        'content-type': 'application/json',
        'X-RapidAPI-Host': 'rapid-translate.p.rapidapi.com',
        'X-RapidAPI-Key': RAPIDAPI_API_KEY,
    }
    payload = {
        'from': language_from,
        'text': text,
        'to': language_to,
    }

    response = requests.post(TRANSLATION_API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        translation = response.json()

        translation_key = f'{language_from}:{language_to}:{text}'
        redis_client.set(translation_key, translation.get('result'), ex=CACHE_EXPIRATION)  # Cache por 1 hora

        return jsonify({
            'language_from': translation.get('from'),
            'language_to': translation.get('to'),
            'text': text,
            'text_translated': translation.get('result')
        })
    else:
        return jsonify({'error': 'Erro na tradução'}), 500


@app.route('/translate_cache', methods=['POST'])
def translate_cache():
    data = request.get_json()
    language_from = data.get('language_from')
    language_to = data.get('language_to')
    text = data.get('text')

    
    translation_key = f'{language_from}:{language_to}:{text}'
    
    cached_translation = redis_client.get(translation_key)
    if cached_translation:
        return jsonify({
            'language_from': language_from,
            'language_to': language_to,
            'text': text,
            'text_translated': cached_translation.decode('utf-8')
        })


    return jsonify({'msg': 'Não encontrado no cache'}), 404


if __name__ == '__main__':
    app.run(debug=True)
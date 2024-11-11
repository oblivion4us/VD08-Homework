from flask import Flask, render_template
import requests
from googletrans import Translator

app = Flask(__name__)

API_KEY = '/UHpzZen0n1NCOoXbB7SsQ==YAYK376econUC2yi'

# Инициализация переводчика
translator = Translator()


@app.route('/')
def index():
    # Запрос к API для получения случайной цитаты
    response = requests.get(
        'https://api.api-ninjas.com/v1/quotes',
        headers={'X-Api-Key': API_KEY}
    )

    if response.status_code == 200:
        quote_data = response.json()
        if quote_data:
            quote = quote_data[0]['quote']
            author = quote_data[0]['author']

            # Перевод цитаты с английского на русский
            try:
                translated_quote = translator.translate(quote, src='en', dest='ru').text
                translated_author = translator.translate(author, src='en', dest='ru').text
            except Exception as e:
                translated_quote = "Ошибка при переводе"
                translated_author = "Ошибка при переводе"
        else:
            quote, author, translated_quote, translated_author = "No quote found", "Unknown", "No translation available", "Unknown"
    else:
        quote, author, translated_quote, translated_author = "Error fetching quote", "Unknown", "No translation available", "Unknown"

    return render_template('index.html', quote=quote, author=author, translated_quote=translated_quote, translated_author=translated_author)

if __name__ == '__main__':
    app.run(debug=True)
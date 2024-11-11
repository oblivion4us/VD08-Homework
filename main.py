from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = '/UHpzZen0n1NCOoXbB7SsQ==YAYK376econUC2yi'

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
        else:
            quote, author = "No quote found", "Unknown"
    else:
        quote, author = "Error fetching quote", "Unknown"

    return render_template_string('index.html', quote=quote, author=author)

if __name__ == '__main__':
    app.run(debug=True)

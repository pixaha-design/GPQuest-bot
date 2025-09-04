from flask import Flask, render_template
import urllib.parse

app = Flask(__name__)

# Настройки квеста
quest = {
    "name": "Квест Цикада",
    "difficulty": "4/10",
    "price": "0.01 $GOVNO",
    "participants": 5,
    "prize_pool": "0.04 $GOVNO"
}

# Ссылка шаблон (замени на реальный Govno Payment Bot URL)
GOVNO_BASE_URL = "https://govnopaymentbot.com/pay"

# Ссылка обратного вызова после оплаты (можно заменить на рабочий webhook)
CALLBACK_URL = "https://yourserver.com/webhook"

@app.route("/")
def index():
    # Генерируем ссылку оплаты
    params = {
        "amount": 0.01,
        "currency": "GOVNO",
        "callback": CALLBACK_URL
    }
    pay_link = f"{GOVNO_BASE_URL}?{urllib.parse.urlencode(params)}"
    return render_template("index.html", quest=quest, pay_link=pay_link)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # Render подставит свой порт
    app.run(host="0.0.0.0", port=port, debug=True)


from flask import Flask, request, render_template, redirect, url_for
import requests, urllib.parse

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

# Ссылка обратного вызова после оплаты (можно пустая для теста)
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

# 🔑 Вставь сюда токен своего бота из @BotFather
TELEGRAM_TOKEN = "8473743934:AAF5GSF_epqwhzUUIm1cPr7t5-xD0D9gVrw"

# Функция отправки сообщения пользователю
def send_access_key(user_id):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    message = "✅ Оплата получена! Вот твой ключ доступа: ABC123"
    requests.post(url, json={"chat_id": user_id, "text": message})

# Webhook для платежей
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Получены данные:", data)  # для отладки

    # Проверяем статус платежа
    if data.get("status") == "success":
        user_id = data.get("telegram_id")  # этот параметр зависит от Govno Payment Bot
        if user_id:
            send_access_key(user_id)

    return {"ok": True}

if __name__ == "__main__":
    app.run(debug=True)
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)


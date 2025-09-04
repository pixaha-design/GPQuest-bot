from flask import Flask, request
import requests

app = Flask(__name__)

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
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

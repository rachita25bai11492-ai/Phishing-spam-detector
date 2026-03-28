def detect_fraud(message):
    message = message.lower()
    keywords = ["win", "free", "prize", "click", "urgent",
        "password", "otp", "bank", "offer", "money"]
    score = 0
    for word in keywords:
        if word in message:
            score += 1
    if score >= 2:
        return "⚠️ Fraud/Spam Message"
    else:
        return "✅ Safe Message"
while True:
    msg = input("Enter message (or 'exit'): ")
    if msg == "exit":
        break
    print(detect_fraud(msg))
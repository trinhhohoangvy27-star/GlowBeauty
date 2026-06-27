from flask import Flask, render_template, request
from datetime import datetime
import requests

app = Flask(__name__)

# ============================
# Trang chủ
# ============================

@app.route("/")
def home():
    return render_template("index.html")


# ============================
# Xử lý đặt lịch
# ============================

@app.route("/submit", methods=["POST"])
def submit():

    # Lấy dữ liệu từ form
    name = request.form.get("name")
    age = request.form.get("age")
    phone = request.form.get("phone")
    service = request.form.get("service")
    date = request.form.get("date")

    time = datetime.now().strftime("%d/%m/%Y %H:%M")

    # Dữ liệu gửi sang Google Apps Script
    data = {
        "name": name,
        "age": age,
        "phone": phone,
        "service": service,
        "date": date,
        "time": time
    }

    # ===== DEBUG =====
    print("========== DỮ LIỆU NHẬN ĐƯỢC ==========")
    print(data)

    try:

        url = "https://script.google.com/macros/s/AKfycbyzyVlqaoWKVvdpw-QBKm4goBZL9Cqkpd7Dht9QK7-Xx2-A3W4agXvCqE1i6H2x4SqV3A/exec"

        response = requests.post(
            url,
            json=data,
            timeout=10
        )

        print("Status:", response.status_code)
        print("Response:", response.text)

    except Exception as e:
        print("Lỗi gửi Google Sheet:", e)

    return """
<!DOCTYPE html>
<html lang="vi">

<head>

<meta charset="UTF-8">

<title>Glow & Beauty</title>

<style>

body{

font-family:Arial;

background:#fff5f8;

display:flex;

justify-content:center;

align-items:center;

height:100vh;

margin:0;

}

.box{

width:500px;

background:white;

padding:40px;

border-radius:20px;

box-shadow:0 10px 25px rgba(0,0,0,.15);

text-align:center;

}

h2{

color:#ff4f8b;

}

p{

font-size:18px;

color:#555;

}

button{

margin-top:20px;

padding:12px 25px;

border:none;

background:#ff4f8b;

color:white;

border-radius:10px;

cursor:pointer;

font-size:16px;

}

button:hover{

background:#e64079;

}

</style>

</head>

<body>

<div class="box">

<h2>🌸 Đặt lịch thành công!</h2>

<p>Cảm ơn bạn đã đăng ký dịch vụ tại <b>Glow & Beauty Spa</b>.</p>

<p>Chúng tôi sẽ liên hệ với bạn trong thời gian sớm nhất.</p>

<button onclick="window.location='/'">
Quay lại
</button>

</div>

</body>

</html>
"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
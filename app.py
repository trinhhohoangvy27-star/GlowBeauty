from flask import Flask, render_template, request
from datetime import datetime
import requests

app = Flask(__name__)

# ============================
# TRANG CHỦ
# ============================

@app.route("/")
def home():
    return render_template("index.html")


# ============================
# NHẬN DỮ LIỆU TỪ FORM
# ============================

@app.route("/submit", methods=["POST"])
def submit():

    name = request.form.get("name")
    phone = request.form.get("phone")
    service = request.form.get("service")
    date = request.form.get("date")

    time = datetime.now().strftime("%d/%m/%Y %H:%M")

    data = {
        "name": name,
        "phone": phone,
        "service": service,
        "date": date,
        "time": time
    }

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
text-align:center;
padding-top:100px;
}

.box{

width:500px;
margin:auto;
background:white;
padding:40px;
border-radius:20px;
box-shadow:0 5px 15px rgba(0,0,0,.15);

}

h2{

color:#ff4f8b;

}

p{

font-size:18px;

}

button{

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

<p>

Cảm ơn bạn đã đăng ký dịch vụ tại <b>Glow & Beauty</b>.

</p>

<p>

Chúng tôi sẽ liên hệ với bạn trong thời gian sớm nhất.

</p>

<br>

<button onclick="window.location='/'">

Quay lại

</button>

</div>

</body>

</html>

"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
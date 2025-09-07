from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

absensi = []

@app.route('/')
def index():
    return render_template('index.html', absensi=absensi)

@app.route('/absen', methods=['POST'])
def absen():
    nama = request.form['nama']
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    absensi.append({'nama': nama, 'waktu': waktu})
    return render_template('index.html', absensi=absensi)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

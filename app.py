from flask import Flask, request, redirect, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/track')
def track():
    target = request.args.get('to', 'https://default.com')
    user_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    timestamp = datetime.datetime.now()

    log_entry = f"{timestamp} | IP: {user_ip} | UA: {user_agent} | Redirect to: {target}\n"
    with open('logs.txt', 'a') as f:
        f.write(log_entry)

    return redirect(target)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template
from dashboard.analytics import get_system_status

app = Flask(__name__)

@app.route('/')
def dashboard():
    status = get_system_status()
    return render_template('dashboard.html', status=status)

if __name__ == '__main__':
    app.run(debug=True)

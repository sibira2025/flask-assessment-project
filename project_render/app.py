from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary in-memory storage (will reset if app restarts)
items = []

@app.route('/')
def index():
    return render_template('index.html', items=items)

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        title = request.form.get('title')
        if title:
            items.append(title)
        return redirect(url_for('index'))
    return render_template('add_item.html')

if __name__ == '__main__':
    # For local/dev use. On Render, gunicorn will start the app via: gunicorn app:app
    app.run(host='0.0.0.0', port=5000, debug=True)

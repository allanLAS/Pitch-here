from flask import render_template
from app import app


# views
@app.route('/')
def index():
    """"""

    title = 'Home - You have 60 secs. Pitch away!'
    return render_template('index.html', title=title)

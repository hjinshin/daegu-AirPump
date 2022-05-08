from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

import sys
sys.path.append("/Namgu")
sys.path.append("/Seogu")
import Namgu as Ng
import Seogu as Sg

@app.route('/')
def index():
    return render_template('Map.html', Namgu=Ng.body, Seogu=Sg.body)


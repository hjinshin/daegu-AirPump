from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

import sys
sys.path.append("/ScrapeAirPump")
import ScrapeAirPump as ad


@app.route('/')
def index():
    return render_template('Map.html', value=ad.addresses)


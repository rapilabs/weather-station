import requests
from flask import Flask, render_template
from bs4 import BeautifulSoup


app = Flask(__name__)


BAYWX_URL = 'http://www.baywx.com.au/'
BAYWX_TEMP_URL = BAYWX_URL + 'melbtemp2.html'

#max_temp_re = re.compile('Max to now:.*(\d+\.\d+)&deg')
#min_temp_re = re.compile('Min to now:.*(\d+\.\d+)&deg')


def retrieve_temp():
    response = requests.get(BAYWX_TEMP_URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    # the alt tag is actually wrong
    graph_relative_url = soup.find(alt="Melbourne CBD Temperature Graph")['src']
    return BAYWX_URL + graph_relative_url


@app.route('/')
def index():
    graph_url = retrieve_temp()
    return render_template('index.html', temp_url=BAYWX_URL, temp_graph_url=graph_url)

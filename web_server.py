from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
import logging

from rnm.interface import Interface
from rnm.wireless import WiFi

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html',
                           page_id='index',
                           eth_ip='TBD',
                           wlan_ip='TBD',
                           )

if __name__ == '__main__':
    # This will provide info to stout
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    # FileHandler will provide a way to print log info to file
    # todo: grab log file name from application config file?
    handler = logging.FileHandler('web_server.log')
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    eth = Interface(iface='eth0', logger=logger)
    wlan = Interface(iface='wlan0', logger=logger)
    wifi = WiFi()
    #wifi.scan()
    #index()
    app.run(debug=True, host='0.0.0.0')

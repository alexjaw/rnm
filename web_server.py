from flask import Flask
import logging

from rnm.interface import Interface
from rnm.wireless import WiFi

app = Flask(__name__)

@app.route('/')
def index():
    html_elements = []
    html_elements.append('<h1>Raspberry network manager</h1>')
    html_elements.append('<p>My eth0 IP: ' + str(eth.get_ip()) + '</p>')
    html_elements.append('<p>My wlan0 IP: ' + str(wlan.get_ip()) + '</p>')
    html_elements.append('<p>Active hotspot(s) list:</p>')
    html_elements.append('<ul>')
    for hotspot in wifi.get_hotspots_info():
        html_elements.append('<li>ssid/encrypted/quality : '
                             + hotspot.get('ssid') + '/'
                             + str(hotspot.get('encrypted')) + '/'
                             + hotspot.get('quality') + '</li>')
    html_elements.append('</ul>')
    html_page = '\n'.join(html_elements)
    return html_page


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
    wifi.scan()
    #index()
    app.run(host='0.0.0.0')

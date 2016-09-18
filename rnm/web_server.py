from flask import Flask
import logging

from rnm import Interface

app = Flask(__name__)

@app.route('/')
def index():
    html_elements = []
    html_elements.append('<h1>Hello</h1>')
    html_elements.append('<p>My IP: ' + str(rnm.get_ip()) + '</p>')
    html_elements.append('<p>Can see these hotspots: ' + 'TBD' + '</p>')
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

    rnm = Interface(logger=logger)
    app.run(host='0.0.0.0')

from flask import Flask, request
from netaddr import valid_ipv6
app = Flask(__name__)


@app.route('/')
def index():
    if valid_ipv6(request.remote_addr):
        return "<img src='https://www.hillspet.com/" \
               "content/dam/cp-sites/hills/hills-pet/" \
               "en_us/exported/cat-care/images/russian-blue-cat-on-cat-bed.jpg'/>"
    return "<img src='http://www.clker.com/cliparts/D/G/V/D/V/u/sad-smiley-md.png'/>"


if __name__ == '__main__':
    app.run()

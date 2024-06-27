from flask import Flask
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

@app.route('/')
def hello_world_new():
    for _ in range(100):
        app.logger.info('Hello World !!!')
    return 'Hello World !!!'

@app.route('/helloworld')
def hello_world():
    for _ in range(100):
        app.logger.info('Hello World !!! This is API endpoint: helloworld')
    return 'Hello World !!! This is API endpoint: helloworld'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

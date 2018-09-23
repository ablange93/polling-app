from flask import Flask

votr = Flask(__name__)

@votr.route('/')
def home():
    return 'hello world'

if __name__ == '__main__':
    votr.run()
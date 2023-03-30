from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/hello/', methods=['GET', 'POST'])
def welcome():

   return jsonify("Hello"), 200

if __name__ == '__main__':
    app.run(host='localhost', port=3333)
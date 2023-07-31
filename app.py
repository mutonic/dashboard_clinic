from flask import Flask

app = Flask(__name__)

@app.route("/")

def give_me_this():
  return 'Hello G'

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
from flask import Flask, request
app = Flask(__name__)

# app.route below will result in :
# the webserver page being served at http:<IP Address>:<port>/menu

@app.route('/menu')

def menu():
    return app.send_static_file('index.html')

if __name__ == '__main__':
  app.run(debug=True,host='0.0.0.0', port=5500)


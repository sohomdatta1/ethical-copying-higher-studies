from flask import *
 
app = Flask(__name__)
 
@app.route('/flutter_infra_release/flutter/fonts/bd151aa3c2f7231344411a01dba4ef61b3cd56b2/fonts.zip')
def hello_world():
    return send_file('./fonts.zip')

if __name__ == '__main__':
    app.run()
"""
Nathaniel Mason's Flask API.
"""

from flask import Flask, abort, send_from_directory

app = Flask(__name__)

@app.route("/<string:dir_path>/<string:file_name>")
def hello(dir_path, file_name):
    return "UOCIS docker demo!\n dir path is: {dir_path}\n file name is {file_name}"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

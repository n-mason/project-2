"""
Nathaniel Mason's Flask API.
"""

from flask import Flask, abort, send_from_directory
import os

app = Flask(__name__)

@app.route("/<string:web>/<string:pages>/<string:file_name>")
def hello(web, pages, file_name):
    full_path = "./" + web + "/" + pages + "/" + file_name
    #str_ans = (f"full path is: {full_path} \n")

    #check for ~ and .. in path
    if ("~" in full_path) or (".." in full_path):
        abort(403)
    # Else if file exists in pages/ directory, transmit STATUS_OK followed by file
    elif os.path.isfile(full_path):
        send_from_directory('pages/', file_name), 200
    #else case, so file is not found
    else:
        abort(404)
    
    #return "UOCIS docker demo!\n"
    #return str_ans

@app.errorhandler(403)
def forbidden(e):
    return send_from_directory('pages/', '403.html'), 403

@app.errorhandler(404)
def forbidden(e):
    return send_from_directory('pages/', '404.html'), 404

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

"""
Nathaniel Mason's Flask API.
"""

from flask import Flask, abort, send_from_directory
import os

app = Flask(__name__)

@app.route("/<string:request>")
def hello(request):
    # full input will look like localhost:5001/trivia.html, 
    # so request will contain the stuff after the slash: "trivia.html"
    path_to_check = "pages/" + request

    # check for ~ and .. in path
    if ("~" in request) or (".." in request):
        abort(403)
    # else if file exists in pages/ directory, transmit STATUS_OK followed by file
    elif os.path.isfile(path_to_check):
        return send_from_directory('pages/', request), 200
    # else case, so file is not found
    else:
        abort(404)

@app.errorhandler(403)
def forbidden(e):
    return send_from_directory('pages/', '403.html'), 403

@app.errorhandler(404)
def forbidden(e):
    return send_from_directory('pages/', '404.html'), 404

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

"""
Nathaniel Mason's Flask API.
"""

from flask import Flask, abort, send_from_directory
import os
import configparser

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
        file_found()
    # else case, so file is not found
    else:
        abort(404)

@app.errorhandler(403)
def forbidden(e):
    return send_from_directory('pages/', '403.html'), 403

@app.errorhandler(404)
def file_not_found(e):
    return send_from_directory('pages/', '404.html'), 404

def file_found(f):
    return send_from_directory('pages/', request), 200


def parse_config(config_paths):
    config_path = None
    for f in config_paths:
        if os.path.isfile(f):
            config_path = f
            break

    if config_path is None:
        raise RuntimeError("Configuration file not found!")

    config = configparser.ConfigParser()
    config.read(config_path)
    return config

config = parse_config(["credentials.ini", "default.ini"])

port = config["SERVER"]["PORT"]
debug = config["SERVER"]["DEBUG"]

if __name__ == "__main__":
    app.run(debug=debug, host='0.0.0.0', port=port)

"""
Nathaniel Mason's Flask API.
"""

from flask import Flask, abort, send_from_directory
import os
import configparser

app = Flask(__name__)

@app.route("/<string:request>")
def hello(request):
    # If the request contains no illegal characters, will need to see if the request exists in the pages/ directory
    # So, define the path variable that will be checked on the next line
    path_to_check = "pages/" + request

    # Check for illegal characters "~" and ".." in the request the user entered
    if ("~" in request) or (".." in request):
        abort(403)
    # Else if file requested exists in pages/ directory, call file_found function
    elif os.path.isfile(path_to_check):
        return file_found(request)
    # Last case is when the file requested is not found
    else:
        abort(404)

# Handle the case where the request is forbidden
@app.errorhandler(403)
def forbidden(e):
    return send_from_directory('pages/', '403.html'), 403

# Handle the case where the request is not found
@app.errorhandler(404)
def file_not_found(e):
    return send_from_directory('pages/', '404.html'), 404

# Handle the case where the request is found in the pages/ directory
def file_found(request):
    return send_from_directory('pages/', request), 200

# Config parser code to determine the port and debug mode that was defined
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

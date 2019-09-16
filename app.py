#!/usr/bin/env python

"""
Basic Flask API for password generation
"""

from datetime import datetime as dt
from flask import Flask, make_response, render_template, request
from password_generator import generate_password
#from random import choice

app = Flask(__name__)
THEMES = [
    "mirage", "nimvelo", "sea-blue", "celestial", "orca", "love-and-liberty",
    "the-blue-lagoon", "under-the-lake", "cosmic-fusion", "love-couple",
    "frost", "mauve", "deep-sea-space", "solid-vault", "deep-space", "purplin",
    "little-leaf", "purple-bliss", "amethyst", "namn", "kashmir"
    ]
RELEASE = "1.0.0"

@app.route("/", methods=["POST", "GET"])
def index():
    options = {"debug": None, "language": "en", "spaces": "0", "symbol":"1",
               "uppercase":"1"}
    if request.method == "POST":
        resp = make_response("")
        for k in options:
            # Ensure invalid POST variables are not left unhandled
            try:
                resp.set_cookie(
                    f"fp_{k}", request.form.get(k),
                    max_age=60*60*24*7)
            except KeyError:
                pass
        resp.headers["location"] = "./"
        return resp, 302
    else:
        # Prioritize GET values over cookies
        for k in options:
            try:
                # Set default to ensure existing options are not overridden
                # if HTML query strings or POST variables are not defined
                if request.args.get(k, default=None) is not None:
                    options[k] = request.args.get(k, '')
                elif request.cookies.get(f"fp_{k}", default=None) is not None:
                    options[k] = request.cookies.get(f"fp_{k}")
            except KeyError:
                pass
        password = generate_password(
            language=options["language"], spaces=options["spaces"],
            symbol=options["symbol"], uppercase=options["uppercase"])
        return render_template(
            "index.html", debug=options["debug"], debug_data=options,
            language=options["language"], release=RELEASE,
            spaces=options["spaces"], symbol=options["symbol"],
            uppercase=options["uppercase"], theme="sea-blue",
            title="Password Generator", password=password, year=dt.now().year,
            )

if __name__ == "__main__":
    app.run(debug=True)

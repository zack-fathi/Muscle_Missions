"""Your previous workouts page."""

import os
import uuid
import hashlib
import pathlib
import flask
from openai import OpenAI
import muscle
import requests
import json
from .. import utils


client = OpenAI()

@muscle.app.route("/liftbot/")
def show_liftbot():
    """Show the liftbot screen."""

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
    )

    print(completion.choices[0].message)

    return flask.render_template("liftbot.html")

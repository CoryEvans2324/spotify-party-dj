#!/bin/bash

source ./venv/bin/activate

export FLASK_APP=app.server:app
export FLASK_ENV=development

flask run --host 0.0.0.0 --port 5000 --cert=cert.pem --key=key.pem

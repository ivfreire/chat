#!/bin/bash
export FLASK_ENV=development
export FLASK_APP=chat.py
flask run --host=0.0.0.0 --port=3000

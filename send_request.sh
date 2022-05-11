#!/bin/sh

curl -d '{"name": "Alfred", "id": 10}' -H 'Content-Type: application/json' localhost:8000/predict/

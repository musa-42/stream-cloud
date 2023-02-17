#!/bin/sh
gunicorn main:main --bind 0.0.0.0:8000 --timeout 86400 --worker-class aiohttp.GunicornWebWorker & python -m bot

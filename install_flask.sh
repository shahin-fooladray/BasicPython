#!/bin/bash
cd /home/fooladra/public_html/apps/BasicPython
source /home/fooladra/virtualenv/public_html/apps/BasicPython/3.9/bin/activate
python -m pip install --upgrade pip
python -m pip install Flask==3.0.2 --no-cache-dir 
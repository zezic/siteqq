# Site QQ

## Clone and install dependencies

    git clone https://github.com/zezic/siteqq.git
    cd siteqq
    python3 -m venv .venv
    source .venv/bin/activate
    pip install flask flask-restful flask-mongoengine marshmallow-mongoengine

## Configure

    cp config.py.example instance/config.py

## Run

    python run.py

[Docs](API.md)

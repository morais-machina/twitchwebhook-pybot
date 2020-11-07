# twitchwebhook-pybot

A simple twitch bot built in Python using the twitchAPI.webhook example here: <https://pytwitchapi.readthedocs.io/en/latest/modules/twitchAPI.webhook.html>

## Install

```bash
git clone git@github.com:morais-machina/twitchwebhook-pybot.git
cd twitchwebhook-pybot
pip install --upgrade pip
pip install virtualenv
virtualenv pybot
./pybot/Scripts/activate
pip install -r requirements.in
```

## Run

If running locally, be sure to uncomment the `app.run` line

```bash
python app.py
```

## Deploy

### Create your deployment environment with a cloud service

Many options...

### Create environment variables in your deployment environment to populate Secrets

This is usually found in the cloud project's settings

They will end up exposed to your application via these environment variables

```Python
username = os.environ.get("username", "")
channel = os.environ.get("channel", "")
client_id = os.environ.get("client_id", "")
client_secret = os.environ.get("client_secret", "")
callback_url = os.environ.get("callback_url", "http://localhost:5000")
```

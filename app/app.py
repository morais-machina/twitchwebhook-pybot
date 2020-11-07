import os
from twitchAPI.twitch import Twitch
from twitchAPI.webhook import TwitchWebHook
from pprint import pprint

from flask import Flask

app = Flask(__name__)


@app.route("/health")
def health():
    return "Hey, we have Flask in a Docker container!"


def callback_stream_changed(uuid, data):
    print("Callback for UUID " + str(uuid))
    pprint(data)


if __name__ == "__main__":
    # Grab secrets from the env
    username = os.environ.get("username", "")
    channel = os.environ.get("channel", "")
    client_id = os.environ.get("client_id", "")
    client_secret = os.environ.get("client_secret", "")
    callback_url = os.environ.get("callback_url", "http://localhost:5000")
    debug = os.environ.get("debug", False)

    twitch = Twitch(client_id, client_secret)
    twitch.authenticate_app([])

    user_info = twitch.get_users(logins=[username])
    user_id = user_info["data"][0]["id"]
    
    # basic setup
    hook = TwitchWebHook(callback_url, client_id, 5000)
    hook.authenticate(twitch)
    hook.start()

    print("subscribing to hook:")
    success, uuid = hook.subscribe_stream_changed(user_id, callback_stream_changed)
    pprint(success)

    # Only uncomment this if running locally
    # app.run(debug=debug, host="0.0.0.0", port=5000)

<b>Steps for testing Locust</b>
* Setup pyenv `python3 -m venv .venv`
* Activate pyenv `source .venv/bin/activate`
* Install requirements `pip3 install -r requirements.txt`

<b>After it, we're ready to start test!</b>

* Start Locust `locust -f locust.py`

Then we're going to `localhost:8089` and can run test!

In this case, we'll test my instance with preinstalled Rocket Chat.
Also, I added credentials for connecting to chat in .env file. I do this, because <b>I don't store any personal data</b> on this instance and it will be destroyed after <u>several</u> days after meetup:)


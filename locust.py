from locust import HttpLocust, TaskSet
from requests import sessions

from rocketchat_API.rocketchat import RocketChat
from dotenv import load_dotenv
import os
import time

load_dotenv()

user_rocket = os.getenv("USER_ROCKET")
password_rocket = os.getenv("PASS_ROCKET")

with sessions.Session() as session:
    rocket = RocketChat(user_rocket, password_rocket, server_url='https://performance.semistrok-devops.xyz', session=session)
    userData = rocket.login(user_rocket, password_rocket).json()
    authToken = userData["data"]["authToken"]
    userId = userData["data"]["userId"]

headers = {"X-Auth-Token": authToken, "X-User-Id": userId, "Content-type": "application/json" }
roomId = "HfFzxN862YjKmnCsF"

def statistics(l):
    l.client.get("/api/v1/statistics", headers=headers)

def rooms(l):
    l.client.get("/api/v1/rooms.get", headers=headers)

def channel_history(l):
    l.client.get("/api/v1/channels.history\?roomId\=" + roomId, headers=headers)

def discussions(l):
    l.client.get("/api/v1/rooms.getDiscussions?roomId=GENERAL", headers=headers)

def permissions(l):
    l.client.get("/api/v1/permissions.listAll?updatedSince=2017-11-25T15:08:17.248Z", headers=headers)

def something(l):
    payload = { "channel": "#test_channel", "text": "This is a test!" + str(time.time()) }
    l.client.post("/api/v1/chat.postMessage", json=payload, headers=headers )

class UserBehavior(TaskSet):
    tasks = { statistics: 1, rooms: 1, channel_history: 1, discussions: 1, permissions: 1, something: 1 }

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
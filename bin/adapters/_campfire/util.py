import os
import pyfire
import sys

def get_campfire_room():
    subdomain = os.environ.get("HUBOT_CAMPFIRE_SUBDOMAIN", None)
    username = os.environ.get("HUBOT_CAMPFIRE_USERNAME", None)
    password = os.environ.get("HUBOT_CAMPFIRE_PASSWORD", None)
    room_name = os.environ.get("HUBOT_CAMPFIRE_ROOM", None)

    if not all([subdomain, username, password, room_name]):
        sys.stderr.write("You must set HUBOT_CAMPFIRE_SUBDOMAIN "
                         "HUBOT_CAMPFIRE_USERNAME, HUBOT_CAMPFIRE_PASSWORD "
                         "and HUBOT_CAMPFIRE_ROOM\n")
        sys.exit(1)

    campfire = pyfire.Campfire(subdomain, username, password, ssl=True)
    room = campfire.get_room_by_name(room_name)
    room.join()
    return room

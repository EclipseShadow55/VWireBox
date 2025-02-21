import json
from twitchAPI.type import AuthScope as AS

def get_static():
    with open("Data/static.json", "r") as file:
        return json.load(file)

def get_user():
    with open("Data/user.json", "r") as file:
        return json.load(file)

def save_static(data):
    with open("Data/static.json", "w") as file:
        json.dump(data, file, indent=4)

def save_user(data):
    with open("Data/user.json", "w") as file:
        json.dump(data, file, indent=4)

def convert_auths(authlist):
    output = []
    for a in range(len(authlist)):
        auth = authlist[a].lower().split(":")
        if auth[0] == "user":
            if len(auth) < 2:
                raise ValueError("Invalid auth scope " + authlist[a] + " at position " + str(a) + ", too few terms for scope user")
            if auth[1] == "read":
                if len(auth) < 3:
                    raise ValueError("Invalid auth scope " + authlist[a] + " at position " + str(a) + ", too few terms for scope user:read")
                elif len(auth) > 3:
                    raise ValueError("Invalid auth scope " + authlist[a] + " at position " + str(a) + ", too many terms for scope user:read")
                if auth[2] == "broadcast":
                    output.append(AS.USER_READ_BROADCAST)
                elif auth[2] == "email":
                    output.append(AS.USER_READ_EMAIL)
                elif auth[2] == "blocked_users":
                    output.append(AS.USER_READ_BLOCKED_USERS)
                elif auth[2] == "subscriptions":
                    output.append(AS.USER_READ_SUBSCRIPTIONS)
                elif auth[2] == "follows":
                    output.append(AS.USER_READ_FOLLOWS)
                elif auth[2] == "whispers":
                    output.append(AS.USER_READ_WHISPERS)
                elif auth[2] == "chat":
                    output.append(AS.USER_READ_CHAT)
                elif auth[2] == "moderated_channels":
                    output.append(AS.USER_READ_MODERATED_CHANNELS)
                elif auth[2] == "emotes":
                    output.append(AS.USER_READ_EMOTES)
                else:
                    raise ValueError("Invalid auth scope: " + authlist[a] + " at position " + str(a) + ", no matching scope found for scope user:read")
            elif auth[1] == "edit":
                if len(auth) < 3:
                    output.append(AS.USER_EDIT)
                elif len(auth) > 3:
                    raise ValueError("Invalid auth scope " + authlist[a] + " at position " + str(a) + ", too many terms for scope user:edit")
                elif auth[2] == "broadcast":
                    output.append(AS.USER_EDIT_BROADCAST)
                elif auth[2] == "follows":
                    output.append(AS.USER_EDIT_FOLLOWS)
                else:
                    raise ValueError("Invalid auth scope: " + authlist[a] + " at position " + str(a) + ", no matching scope found for scope user:edit")
            elif auth[1] == "manage":
                if len(auth) < 3:
                    raise ValueError("Invalid auth scope " + authlist[a] + " at position " + str(a) + ", too few terms for scope user:manage")
                elif len(auth) > 3:
                    raise ValueError("Invalid auth scope " + authlist[a] + " at position " + str(a) + ", too many terms for scope user:manage")
                elif auth[2] == "bloacked_users":
                    output.append(AS.USER_MANAGE_BLOCKED_USERS)
                elif auth[2] == "chat_color":
                    output.append(AS.USER_MANAGE_CHAT_COLOR)
                elif auth[2] == "whispers":
                    output.append(AS.USER_MANAGE_WHISPERS)
                else:
                    raise ValueError("Invalid auth scope: " + authlist[a] + " at position " + str(a) + ", no matching scope found for scope user:manage")
            elif auth[1] == "bot":
                if len(auth) < 3:
                    output.append(AS.USER_BOT)
                else:
                    raise ValueError("Invalid auth scope " + authlist[a] + " at position " + str(a) + ", too many terms for scope user:bot")
            elif auth[1] == "write":
                if len(auth) < 3:
                    raise ValueError("Invalid auth scope " + authlist[a] + " at position " + str(a) + ", too few terms for scope user:write")
                elif len(auth) > 3:
                    raise ValueError("Invalid auth scope " + authlist[a] + " at position " + str(a) + ", too many terms for scope user:write")
                elif auth[2] == "chat":
                    output.append(AS.USER_WRITE_CHAT)
                else:
                    raise ValueError("Invalid auth scope: " + authlist[a] + " at position " + str(a) + ", no matching scope found for scope user:write")
            else:
                raise ValueError("Invalid auth scope: " + authlist[a] + " at position " + str(a) + ", no matching scope found for scope user")
        elif auth[0] == "channel":
            if len(auth) < 2:
                raise ValueError("Invalid auth scope " + authlist[a] + " at position " + str(a) + ", too few terms for scope channel")
            if auth[1] == "read":
                if len(auth) < 3:
                    raise ValueError("Invalid auth scope " + authlist[a] + " at position " + str(a) + ", too few terms for scope channel:read")
                elif len(auth) > 3:
                    raise ValueError("Invalid auth scope " + authlist[a] + " at position " + str(a) + ", too many terms for scope channel:read")
                elif auth[2] == "subscriptions":
                    output.append(AS.CHANNEL_READ_SUBSCRIPTIONS)
                elif auth[2] == "stream_key":
                    output.append(AS.CHANNEL_READ_STREAM_KEY)
                elif auth[2] == "hype_train":
                    output.append(AS.CHANNEL_READ_HYPE_TRAIN)
                elif auth[2] == "redemptions":
                    output.append(AS.CHANNEL_READ_REDEMPTIONS)
                elif auth[2] == "charity":
                    output.append(AS.CHANNEL_READ_CHARITY)
                elif auth[2] == "editors":
                    output.append(AS.CHANNEL_READ_EDITORS)
                elif auth[2] == "goals":
                    output.append(AS.CHANNEL_READ_GOALS)
                elif auth[2] == "polls":
                    output.append(AS.CHANNEL_READ_POLLS)
                elif auth[2] == "predictions":
                    output.append(AS.CHANNEL_READ_PREDICTIONS)
                elif auth[2] == "vips":
                    output.append(AS.CHANNEL_READ_VIPS)
                elif auth[2] == "ads":
                    output.append(AS.CHANNEL_READ_ADS)
                else:
                    raise ValueError("Invalid auth scope: " + authlist[a] + " at position " + str(a) + ", no matching scope found for scope channel:read")
            elif auth[1] == "moderate":
                if len(auth) < 3:
                    output.append(AS.CHANNEL_MODERATE)
                else:
                    raise ValueError("Invalid auth scope " + authlist[a] + " at position " + str(a) + ", too many terms for scope channel:moderator")
            elif auth[1] == "manage":
                if len(auth) < 3:
                    raise ValueError("Invalid auth scope " + authlist[a] + " at position " + str(a) + ", too few terms for scope channel:manage")
                elif len(auth) > 3:
                    raise ValueError("Invalid auth scope " + authlist[a] + " at position " + str(a) + ", too many terms for scope channel:manage")
                elif auth[2] == "broadcast":
                    output.append(AS.CHANNEL_MANAGE_BROADCAST)
                elif auth[2] == "redemptions":
                    output.append(AS.CHANNEL_MANAGE_REDEMPTIONS)
                elif auth[2] == "videos":
                    output.append(AS.CHANNEL_MANAGE_VIDEOS)
                elif auth[2] == "polls":
                    output.append(AS.CHANNEL_MANAGE_POLLS)
                elif auth[2] == "predictions":
                    output.append(AS.CHANNEL_MANAGE_PREDICTIONS)
                elif auth[2] == "schedule":
                    output.append(AS.CHANNEL_MANAGE_SCHEDULE)
                elif auth[2] == "raids":
                    output.append(AS.CHANNEL_MANAGE_RAIDS)
                elif auth[2] == "moderators":
                    output.append(AS.CHANNEL_MANAGE_MODERATORS)
                elif auth[2] == "vips":
                    output.append(AS.CHANNEL_MANAGE_VIPS)
                elif auth[2] == "ads":
                    output.append(AS.CHANNEL_MANAGE_ADS)
                else:
                    raise ValueError("Invalid auth scope: " + authlist[a] + " at position " + str(a) + ", no matching scope found for scope channel:manage")
            elif auth[1] == "bot":
                if len(auth) < 3:
                    output.append(AS.CHANNEL_BOT)
                else:
                    raise ValueError("Invalid auth scope " + authlist[a] + " at position " + str(a) + ", too many terms for scope channel:bot")
            elif auth[1] == "subscriptions":
                if len(auth) < 3:
                    output.append(AS.CHANNEL_SUBSCRIPTIONS)
                else:
                    raise ValueError("Invalid auth scope " + authlist[a] + " at position " + str(a) + ", too many terms for scope channel:subscriptions")
            elif auth[1] == "edit":
                if len(auth) < 3:
                    raise ValueError("Invalid auth scope " + authlist[a] + " at position " + str(a) + ", too few terms for scope channel:edit")
                elif len(auth) > 3:
                    raise ValueError("Invalid auth scope " + authlist[a] + " at position " + str(a) + ", too many terms for scope channel:edit")
                elif auth[2] == "comercial":
                    output.append(AS.CHANNEL_EDIT_COMMERCIAL)
                else:
                    raise ValueError("Invalid auth scope: " + authlist[a] + " at position " + str(a) + ", no matching scope found for scope channel:edit")
            else:
                raise ValueError("Invalid auth scope: " + authlist[a] + " at position " + str(a) + ", no matching scope found for scope channel")
        elif auth[0] == "chat":
            if len(auth) < 2:
                raise ValueError("Invalid auth scope " + authlist[a] + " at position " + str(a) + ", too few terms for scope chat")
            elif len(auth) > 2:
                raise ValueError("Invalid auth scope " + authlist[a] + " at position " + str(a) + ", too many terms for scope chat")
            elif auth[1] == "edit":
                output.append(AS.CHAT_EDIT)
            elif auth[1] == "read":
                output.append(AS.CHAT_READ)
            else:
                raise ValueError("Invalid auth scope: " + authlist[a] + " at position " + str(a) + ", no matching scope found for scope chat")
        elif auth[0] == "analytics":
            if len(auth) < 3:
                raise ValueError("Invalid auth scope " + authlist[a] + " at position " + str(a) + ", too few terms for scope analytics")
            elif len(auth) > 3:
                raise ValueError("Invalid auth scope " + authlist[a] + " at position " + str(a) + ", too many terms for scope analytics")
            elif auth[1] == "read":
                if auth[2] == "extensions":
                    output.append(AS.ANALYTICS_READ_EXTENSIONS)
                elif auth[2] == "games":
                    output.append(AS.ANALYTICS_READ_GAMES)
                else:
                    raise ValueError("Invalid auth scope: " + authlist[a] + " at position " + str(a) + ", no matching scope found for scope analytics:read")
            else:
                raise ValueError("Invalid auth scope: " + authlist[a] + " at position " + str(a) + ", no matching scope found for scope analytics")
        elif auth[0] == "bits":
            if len(auth) < 2:
                raise ValueError("Invalid auth scope " + authlist[a] + " at position " + str(a) + ", too few terms for scope bits")
            elif len(auth) > 2:
                raise ValueError("Invalid auth scope " + authlist[a] + " at position " + str(a) + ", too many terms for scope bits")
            elif auth[1] == "read":
                output.append(AS.BITS_READ)
            else:
                raise ValueError("Invalid auth scope: " + authlist[a] + " at position " + str(a) + ", no matching scope found for scope bits")
        elif auth[0] == "clips":
            if len(auth) < 2:
                raise ValueError("Invalid auth scope " + authlist[a] + " at position " + str(a) + ", too few terms for scope clips")
            elif len(auth) > 2:
                raise ValueError("Invalid auth scope " + authlist[a] + " at position " + str(a) + ", too many terms for scope clips")
            elif auth[1] == "edit":
                output.append(AS.CLIPS_EDIT)
            else:
                raise ValueError("Invalid auth scope: " + authlist[a] + " at position " + str(a) + ", no matching scope found for scope clips")
        elif auth[0] == "whispers":
            if len(auth) < 2:
                raise ValueError("Invalid auth scope " + authlist[a] + " at position " + str(a) + ", too few terms for scope whispers")
            elif len(auth) > 2:
                raise ValueError("Invalid auth scope " + authlist[a] + " at position " + str(a) + ", too many terms for scope whispers")
            elif auth[1] == "read":
                output.append(AS.WHISPERS_READ)
            elif auth[1] == "edit":
                output.append(AS.WHISPERS_EDIT)
            else:
                raise ValueError("Invalid auth scope: " + authlist[a] + " at position " + str(a) + ", no matching scope found for scope whispers")
        elif auth[0] == "moderation":
            if len(auth) < 2:
                raise ValueError("Invalid auth scope " + authlist[a] + " at position " + str(a) + ", too few terms for scope moderation")
            elif len(auth) > 2:
                raise ValueError("Invalid auth scope " + authlist[a] + " at position " + str(a) + ", too many terms for scope moderation")
            elif auth[1] == "read":
                output.append(AS.MODERATION_READ)
            else:
                raise ValueError("Invalid auth scope: " + authlist[a] + " at position " + str(a) + ", no matching scope found for scope moderation")
        elif auth[0] == "moderator":
            if len(auth) < 3:
                raise ValueError("Invalid auth scope " + authlist[a] + " at position " + str(a) + ", too few terms for scope moderator")
            elif len(auth) > 3:
                raise ValueError("Invalid auth scope " + authlist[a] + " at position " + str(a) + ", too many terms for scope moderator")
            elif auth[1] == "manage":
                if auth[2] == "automod":
                    output.append(AS.MODERATOR_MANAGE_AUTOMOD)
                elif auth[2] == "chat_settings":
                    output.append(AS.MODERATOR_MANAGE_CHAT_SETTINGS)
                elif auth[2] == "banned_users":
                    output.append(AS.MODERATOR_MANAGE_BANNED_USERS)
                elif auth[2] == "blocked_terms":
                    output.append(AS.MODERATOR_MANAGE_BLOCKED_TERMS)
                elif auth[2] == "announcements":
                    output.append(AS.MODERATOR_MANAGE_ANNOUNCEMENTS)
                elif auth[2] == "chat_messages":
                    output.append(AS.MODERATOR_MANAGE_CHAT_MESSAGES)
                elif auth[2] == "warnings":
                    output.append(AS.MODERATOR_MANAGE_WARNINGS)
                elif auth[2] == "shield_mode":
                    output.append(AS.MODERATOR_MANAGE_SHIELD_MODE)
                elif auth[2] == "automod_settings":
                    output.append(AS.MODERATOR_MANAGE_AUTOMOD_SETTINGS)
                elif auth[2] == "shoutouts":
                    output.append(AS.MODERATOR_MANAGE_SHOUTOUTS)
                elif auth[2] == "unban_requests":
                    output.append(AS.MODERATOR_MANAGE_UNBAN_REQUESTS)
                else:
                    raise ValueError("Invalid auth scope: " + authlist[a] + " at position " + str(a) + ", no matching scope found for scope moderator:manage")
            elif auth[1] == "read":
                if auth[2] == "chat_settings":
                    output.append(AS.MODERATOR_READ_CHAT_SETTINGS)
                elif auth[2] == "banned_users":
                    output.append(AS.MODERATOR_READ_BANNED_USERS)
                elif auth[2] == "blocked_terms":
                    output.append(AS.MODERATOR_READ_BLOCKED_TERMS)
                elif auth[2] == "chat_messages":
                    output.append(AS.MODERATOR_READ_CHAT_MESSAGES)
                elif auth[2] == "warnings":
                    output.append(AS.MODERATOR_READ_WARNINGS)
                elif auth[2] == "moderators":
                    output.append(AS.MODERATOR_READ_MODERATORS)
                elif auth[2] == "vips":
                    output.append(AS.MODERATOR_READ_VIPS)
                elif auth[2] == "chatters":
                    output.append(AS.MODERATOR_READ_CHATTERS)
                elif auth[2] == "shield_mode":
                    output.append(AS.MODERATOR_READ_SHIELD_MODE)
                elif auth[2] == "automod_settings":
                    output.append(AS.MODERATOR_READ_AUTOMOD_SETTINGS)
                elif auth[2] == "followers":
                    output.append(AS.MODERATOR_READ_FOLLOWERS)
                elif auth[2] == "shoutouts":
                    output.append(AS.MODERATOR_READ_SHOUTOUTS)
                elif auth[2] == "unban_requests":
                    output.append(AS.MODERATOR_READ_UNBAN_REQUESTS)
                elif auth[2] == "suspicious_users":
                    output.append(AS.MODERATOR_READ_SUSPICIOUS_USERS)
                else:
                    raise ValueError("Invalid auth scope: " + authlist[a] + " at position " + str(a) + ", no matching scope found for scope moderator:read")
            else:
                raise ValueError("Invalid auth scope: " + authlist[a] + " at position " + str(a) + ", no matching scope found for scope moderator")

def get_optimized_auths(authlist):
    output = []
    for auth in authlist:
        if auth not in output:
            output.append(auth)
    for item in output:
        sitem = item.split(":")
        if sitem[1] == "read":
            if len(sitem) == 3:
                if ":".join([sitem[0], "manage", sitem[2]]) in output:
                    output.remove(item)
                elif ":".join([sitem[0], "edit", sitem[2]]) in output:
                    output.remove(item)
            elif len(sitem) == 2:
                if ":".join([sitem[0], "manage"]) in output:
                    output.remove(item)
                elif ":".join([sitem[0], "edit"]) in output:
                    output.remove(item)
    return output

def calc_necessary_auth(sublist):
    static = get_static()
    auths = []
    for sub in sublist:
        for auth in static[sub][2]:
            auths.append(auth)
    return get_optimized_auths(auths)

def add_sub(sublist):
    static = get_static()
    user = get_user()
    for s in sublist:
        sub = s.lower()
        if sub not in static:
            raise ValueError(f"Sub {sub} not found in static data.")
        elif sub in user["subs"]:
            raise ValueError(f"Sub {sub} already in user data.")
        user["subs"].append(sub)
    save_user(user)

def rem_sub(sublist):
    user = get_user()
    for s in sublist:
        sub = s.lower()
        if sub not in user["subs"]:
            raise ValueError(f"Sub {sub} not found in user data.")
        user["subs"].remove(sub)
    save_user(user)
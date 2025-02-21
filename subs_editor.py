import misc


def process(command):
    static = misc.get_static()
    user = misc.get_user()
    output = {"data": {}, "state": ""}
    if command[0] == "list":
        if len(command) > 1:
            if command[1] == "-a":
                if len(command) > 2:
                    if command[2] == "-n":
                        output["data"] = static.keys()
                    elif command[2] == "-p":
                        output["data"] = {key: value[0] for key, value in static.items()}
                    elif command[2] == "-d":
                        output["data"] = {key: value[1] for key, value in static.items()}
                    else:
                        output["data"] = static
                output["state"] = "list"
                output["data"]["list"] = f"Subs listed with modifiers \"{','.join(command[1:])}\""
                output["data"] = static
            elif command[1] == "-c":
                if len(command) > 2:
                    if command[2] == "-n":
                        output["data"] = user["subs"]
                    elif command[2] == "-p":
                        output["data"] = {user["subs"][i]: static[user["subs"][i]][0] for i in range(len(user["subs"]))}
                    elif command[2] == "-d":
                        output["data"] = {user["subs"][i]: static[user["subs"][i]][1] for i in range(len(user["subs"]))}
                    else:
                        output["data"] = {user["subs"][i]: static[user["subs"][i]] for i in range(len(user["subs"]))}
                output["state"] = "list"
                output["data"]["list"] = f"Subs listed with modifiers \"{','.join(command[1:])}\""
                output["data"] = static
            else:
                output["state"] = "error"
                output["data"] = {"error": "Invalid option"}
        else:
            output["state"] = "error"
            output["data"] = {"error": "No option specified"}
    elif command[0] == "add":
        if len(command) > 1:
            if command[1] in user["subs"]:
                output["data"]["error"] = "Sub already in list of current subs"
            elif command[1] in static.keys():
                user["subs"].append(command[1])
                output["data"]["success"] = f"Sub \"{command[1]}\" added"
            else:
                output["state"] = "error"
                output["data"]["error"] = "Sub not found"
        else:
            output["data"] = {"error": "No name specified"}
    elif command[0] == "remove":
        if len(command) > 1:
            if command[1] in user["subs"]:
                user["subs"].remove(command[1])
                output["state"] = "success"
                output["data"]["success"] = f"Sub \"{command[1]}\" removed"
            else:
                output["state"] = "error"
                output["data"]["error"] = "Sub not in list of current subs"
        else:
            output["state"] = "error"
            output["data"] = {"error": "No name specified"}
    else:
        output["state"] = "error"
        output["data"] = {"error": "Invalid command"}
    user["perms"] = misc.calc_necessary_auth(user["subs"])
    misc.save_static(static)
    misc.save_user(user)
    return output
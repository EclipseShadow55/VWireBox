import twitchAPI
import misc
import requests
import os
from datetime import datetime
from importlib import import_module
import updater


if __name__ == "__main__":
    # Create new log file
    os.environ["LOG_FILE"] = log_file = f"Logs/{datetime.now().strftime('%d+%m+%Y&%H+%M+%S+%f')}.txt"
    with open(log_file, "x") as f:
        f.write("")
    # Find and initialize plugins
    plugins = []
    for direct in misc.get_subdirs("Plugins"):
        if os.path.isfile(f"Plugins/{direct}/main.py") and updater.exists("EclipseShadow55", "Twitch-Connector", f"Plugins/{direct}/main.py"):
            updater.update_file("EclipseShadow55", "Twitch-Connector", f"Plugins/{direct}/main.py")
            plugins.append({
                "name": direct,
                "on_alert": import_module(f"Plugins.{direct}.main.on_alert",
                                          package=os.path.dirname(os.path.abspath(__file__)))
            })
        else:
            with open(log_file, "a") as f:
                f.write(f"Plugin {direct} does not have a main.py file, so can not be used.\n")
            raise Warning(f"Plugin {direct} does not have a main.py file, so can not be used.")
    # Check for updates
    # TODO: UNCOMMENT THIS NEXT LINE
    #
    # Get user data
    user = misc.get_user()
    # Main loop


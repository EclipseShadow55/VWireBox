from updater import update_file, FILES, compare_files

if __name__ == "__main__":
    print("Searching for updates...")
    needs_to_update = []
    for file in FILES:
        if not compare_files("EclipseShadow55", "Twitch-Connector", file):
            needs_to_update.append(file)
            print("Update needed for", file)
    if len(needs_to_update) and input("Would you like to update all programs (y/n): ").lower()[0] == "y":
        for file in needs_to_update:
            update_file("EclipseShadow55", "Twitch-Connector", file)

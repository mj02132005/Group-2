command = input("Command: ").lower()
match command:
    case "start": print("Starting...")
    case "stop": print("Stopping...")
    case "pause": print("Paused")
    case "help": print("Available: start, stop, pause, help")
    case _: print("Unknown command")

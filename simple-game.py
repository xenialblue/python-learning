command = ""
started = False

while True:
    command = input("> ").lower()
    if command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif command == "start":
        if started:
            print("The car is already started!")
        else:
            started = True
            print("Car started... Ready to go!")
    elif command == "stop":
        if started:
            started = False
            print("The car is stopped!")
        else:
            print("The car is already stopped!")
    elif command == "quit":
        break
    else:
        print("I don't understand this...")
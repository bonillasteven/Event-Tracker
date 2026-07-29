from datetime import datetime 
import json
events = []

def save_events():
    with open("events.json", "w") as file:
        json.dump(events, file, indent=4)

def load_events():
    global events

    try:
        with open("events.json", "r") as file:
            events = json.load(file)
    except FileNotFoundError:
        events = []


def show_main_menu():
    """Display the calendar menu."""

    print("\033[1;36m\n===== EVENT CALENDAR =====\033[0m")
    print("1. Add Event")
    print("2. Remove Event")
    print("3. Edit Event")
    print("4. View Event")
    print("5. Search Event")
    print("6. Exit")

def add_event():
    """Collect information and add one event to the list"""

    print("\033[1;36m\n --- Add Event ---\033[0m")

    title = input("Enter the event title: ").strip()
    date = input("Enter the date (MM/DD/YYYY): ").strip()
    time = input("Enter the time (HH:MM): ").strip()
    location = input("Enter the location: ").strip()
    description = input("Enter a description: ").strip()

    event = {
        "title": title,
        "date": date,
        "time": time,
        "location": location,
        "description": description
    }

    events.append(event)
    save_events()

    print(f"\033[1;32m\n '{title}' was added successfully\033[0m")

def remove_event():
    """ Remove information for the list """

    print("\033[1;36m\n --- Remove Event ---\033[0m")

    # Check if there are any events 
    if len(events) == 0:
        print("\033[1;31mThere are no events to remove.\033[0m")
        return 

    # Diaplay all events
    print("\033[1;36m\n----- Current Evnets -----\033[0m")
    for index, event in enumerate(events, start=1):
        print(f"{index}. {event['title']}")

    # Ask the user while event to remove 
    choice = int(input("\nEnter the event number to remove: "))

    # Remove the selected event
    remove_event = events.pop(choice - 1)
    save_events()

    print(f"\033[1;32m'\n{remove_event['title']}' has been remove.\033[0m")




def edit_event():

    """ Edit Event """

    print("\033[1;36m\n --- Update Event ---\033[0m")

    if len(events) == 0:
        print("\033[1;31mThere are no events to edit.\033[0m")
        return 
    

    update_event = input("Enter the Title of the event you which to update: ")

    found = False

    for event in events:

        if event["title"].lower() == update_event.lower():
        
                found = True
                print("\nCurrent Event Infomartion")
                print(f"\033[1;33mTitle:\033[0m {event['title']}")
                print(f"\033[1;33mDate:\033[0m {event['date']}")
                print(f"\033[1;33mTime:\033[0m {event['time']}")
                print(f"\033[1;33mLocation:\033[0m {event['location']}")
                print(f"\033[1;33mDescription:\033[0m {event['description']}")

                print("\n----- Update Menu -----")
                print("1. Title")
                print("2. Date")
                print("3. Time")
                print("4. Location")
                print("5. Description")
                print("6. All")

                user_choice = input("Press from the selection: ")

                if user_choice == "1":
                    event["title"] = input("New Title: ").strip()

                elif user_choice == "2":
                    event["date"] = input("New Date (MM/DD/YYYY): ").strip()

                elif user_choice == "3":
                    event["time"] = input("New Time (HH:MM): ").strip()
                    
                elif user_choice == "4":
                    event["location"] = input("New Location: ").strip()
                
        
                elif user_choice == "5":
                    event["description"] = input("New Description: ").strip()

                elif user_choice == "6":
                    event["title"] = input("New Title: ").strip()
                    event["date"] = input("New Date (MM/DD/YYYY): ").strip()
                    event["time"] = input("New Time (HH:MM): ").strip()
                    event["location"] = input("New Location: ").strip()
                    event["description"] = input("New Description: ").strip()

                else:
                    print("\033[1;31mInvalid choice.\033[0m")
                    return 

                print("\033[1;32m\nEvent updated successfully\033[0m")
                save_events()
                break
        
    if found == False:
        print("\033[1;31mThere is no event with that title.\033[0m") 

def view_event():
    """Display all events currently stored"""

    if len(events) ==0:
        print("\033[1;31mThere are no events saved.\033[0m")
        return 

    sorted_events = sorted(
        events,
        key=lambda event: datetime.strptime(event["date"], "%m/%d/%Y")
    )

    print("\033[1;36m\n----- Events by Date -----\033[0m")
    for number, event in enumerate(sorted_events, start=1):
        print(f"\033[1;36m\nEvent #{number}\033[0m")
        print("\033[1;36m-\033[0m" * 30)
        print(f"\033[1;33mTitle:\033[0m {event['title']}")
        print(f"\033[1;33mDate:\033[0m {event['date']}")
        print(f"\033[1;33mTime:\033[0m {event['time']}")
        print(f"\033[1;33mLocation:\033[0m {event['location']}")
        print(f"\033[1;33mDescription:\033[0m {event['description']}")

    
def search_event():
    """Display information based on the search"""

    print("\033[1;36m\n----- Search Event -----\033[0m")

    searched_event = input("Enter the title of the event: ")

    found = False 

    for event in events:
        if event['title'].lower() == searched_event.lower():

            found = True
            print(f"\033[1;33mTitle:\033[0m {event['title']}")
            print(f"\033[1;33mDate:\033[0m {event['date']}")
            print(f"\033[1;33mTime:\033[0m {event['time']}")
            print(f"\033[1;33mLocation:\033[0m {event['location']}")
            print(f"\033[1;33mDescription:\033[0m {event['description']}")


    if not found:
        print("\033[1;31mThere is no event with that title\033[0m")

def exit():
    print("\033[1;34m\nThank You!\033[0m")
    print("\033[1;34mGoodBye!\033[0m")







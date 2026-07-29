from datetime import datetime
import json

# List that stores all calendar events
events = []

# Save all events to a JSON file
def save_events():
    with open("events.json", "w") as file:
        json.dump(events, file, indent=4)

# Load events from the JSON file when the program starts
def load_events():
    global events

    try:
        with open("events.json", "r") as file:
            events = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        events = []

# Display the main menu options
def show_main_menu():
    """Display the calendar menu."""

    print("\033[1;36m\n===== EVENT CALENDAR =====\033[0m")
    print("1. Add Event")
    print("2. Remove Event")
    print("3. Edit Event")
    print("4. View Event")
    print("5. Search Event")
    print("6. Exit")

# Add a new event to the calendar
def add_event():
    """Collect information and add one event to the list."""

    print("\033[1;36m\n --- Add Event ---\033[0m")

    # Gather information from the user
    title = input("Enter the event title: ").strip()
    date = input("Enter the date (MM/DD/YYYY): ").strip()
    time = input("Enter the time (HH:MM): ").strip()
    location = input("Enter the location: ").strip()
    description = input("Enter a description: ").strip()

    # Create a dictionary for the event
    event = {
        "title": title,
        "date": date,
        "time": time,
        "location": location,
        "description": description
    }

    # Add the event to the list and save it
    events.append(event)
    save_events()

    print(f"\033[1;32m\n'{title}' was added successfully.\033[0m")

# Remove an event from the calendar
def remove_event():
    """Allow the user to select and remove an event."""

    print("\033[1;36m\n--- Remove Event ---\033[0m")

    # Stop if there are no saved events
    if len(events) == 0:
        print("\033[1;31mThere are no events to remove.\033[0m")
        return

    # Display current events
    print("\033[1;36m\n----- Current Events -----\033[0m")

    for index, event in enumerate(events, start=1):
        print(
            f"{index}. {event['title']} | "
            f"{event['date']} | {event['time']}"
        )

    # Ask for an event number and validate the input
    try:
        choice = int(
            input("\nEnter the event number to remove: ").strip()
        )
    except ValueError:
        print("\033[1;31mPlease enter a number only.\033[0m")
        return

    # Check whether the selected number exists
    if choice < 1 or choice > len(events):
        print("\033[1;31mThat event number does not exist.\033[0m")
        return

    # Get the selected event
    selected_event = events[choice - 1]

    # Display the selected event
    print("\033[1;36m\n----- Selected Event -----\033[0m")
    print(f"\033[1;33mTitle:\033[0m {selected_event['title']}")
    print(f"\033[1;33mDate:\033[0m {selected_event['date']}")
    print(f"\033[1;33mTime:\033[0m {selected_event['time']}")
    print(
        f"\033[1;33mLocation:\033[0m "
        f"{selected_event['location']}"
    )
    print(
        f"\033[1;33mDescription:\033[0m "
        f"{selected_event['description']}"
    )

    # Confirm deletion
    confirm = input(
        "\nRemove this event? Enter Y for yes or N for no: "
    ).strip().lower()

    if confirm == "y":
        removed_event = events.pop(choice - 1)
        save_events()

        print(
            f"\033[1;32m\n'{removed_event['title']}' "
            f"was removed successfully.\033[0m"
        )

    elif confirm == "n":
        print("\033[1;33m\nRemoval canceled.\033[0m")

    else:
        print(
            "\033[1;31m\nInvalid response. "
            "Removal canceled.\033[0m"
        )
# Edit an existing event
def edit_event():
    """Edit information for an existing event."""

    print("\033[1;36m\n--- Edit Event ---\033[0m")

    # Make sure events exist
    if len(events) == 0:
        print("\033[1;31mThere are no events to edit.\033[0m")
        return

    # Display all current events
    print("\033[1;36m\n----- Current Events -----\033[0m")
    for index, event in enumerate(events, start=1):
        print(f"{index}. {event['title']}")

    # Ask the user which event to edit
    try:
        choice = int(input("\nEnter the event number to edit: "))

        if choice < 1 or choice > len(events):
            print("\033[1;31mInvalid event number.\033[0m")
            return

    except ValueError:
        print("\033[1;31mPlease enter a valid number.\033[0m")
        return

    # Get the selected event
    event = events[choice - 1]

    # Display current event information
    print("\033[1;36m\n----- Current Event Information -----\033[0m")
    print(f"\033[1;33mTitle:\033[0m {event['title']}")
    print(f"\033[1;33mDate:\033[0m {event['date']}")
    print(f"\033[1;33mTime:\033[0m {event['time']}")
    print(f"\033[1;33mLocation:\033[0m {event['location']}")
    print(f"\033[1;33mDescription:\033[0m {event['description']}")

    # Display update menu
    print("\n----- Update Menu -----")
    print("1. Title")
    print("2. Date")
    print("3. Time")
    print("4. Location")
    print("5. Description")
    print("6. All")

    user_choice = input("Choose what you want to edit: ")

    # Update selected field
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
        print("\nEnter the new event information:")
        event["title"] = input("New Title: ").strip()
        event["date"] = input("New Date (MM/DD/YYYY): ").strip()
        event["time"] = input("New Time (HH:MM): ").strip()
        event["location"] = input("New Location: ").strip()
        event["description"] = input("New Description: ").strip()

    else:
        print("\033[1;31mInvalid choice.\033[0m")
        return

    # Save the changes
    save_events()

    print("\033[1;32m\nEvent updated successfully!\033[0m")

# Display all events sorted by date
def view_event():
    """Display all events currently stored."""

    # Check whether any events exist
    if len(events) == 0:
        print("\033[1;31mThere are no events saved.\033[0m")
        return

    # Sort events by date
    sorted_events = sorted(
        events,
        key=lambda event: datetime.strptime(event["date"], "%m/%d/%Y")
    )

    # Display all events
    print("\033[1;36m\n----- Events by Date -----\033[0m")
    for number, event in enumerate(sorted_events, start=1):
        print(f"\033[1;36m\nEvent #{number}\033[0m")
        print("\033[1;36m-\033[0m" * 30)
        print(f"\033[1;33mTitle:\033[0m {event['title']}")
        print(f"\033[1;33mDate:\033[0m {event['date']}")
        print(f"\033[1;33mTime:\033[0m {event['time']}")
        print(f"\033[1;33mLocation:\033[0m {event['location']}")
        print(f"\033[1;33mDescription:\033[0m {event['description']}")

# Search for an event by title
def search_event():
    """Display information based on the search."""

    print("\033[1;36m\n----- Search Event -----\033[0m")

    searched_event = input("Enter the title of the event: ")

    found = False

    # Search through every event
    for event in events:
        if event['title'].lower() == searched_event.lower():

            found = True

            # Display the matching event
            print(f"\033[1;33mTitle:\033[0m {event['title']}")
            print(f"\033[1;33mDate:\033[0m {event['date']}")
            print(f"\033[1;33mTime:\033[0m {event['time']}")
            print(f"\033[1;33mLocation:\033[0m {event['location']}")
            print(f"\033[1;33mDescription:\033[0m {event['description']}")

    # Display an error if no event was found
    if not found:
        print("\033[1;31mThere is no event with that title.\033[0m")

# Exit message
def exit():
    """Display a goodbye message."""

    print("\033[1;34m\nThank You!\033[0m")
    print("\033[1;34mGoodbye!\033[0m")





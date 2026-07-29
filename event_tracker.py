# ======================================================
# Event Tracker
# Author: Steven Bonilla
# Description:
# Main program for the Event Tracker application.
# This file displays the menu and calls functions
# from events_define_module.py.
# ======================================================

# Import the event module
import events_define_module as event

# Load saved events from events.json
event.load_events()

# Welcome message
print("\033[1;36m========================================\033[0m")
print("\033[1;36m      Welcome to Steven's Event Tracker\033[0m")
print("\033[1;36m========================================\033[0m")

# Keep the program running until the user exits
while True:

    # Display the main menu
    event.show_main_menu()

    # Ask the user for a menu option
    user_choice = input("\nWhat would you like to do? ").strip()

    if user_choice == "1":
        event.add_event()

    elif user_choice == "2":
        event.remove_event()

    elif user_choice == "3":
        event.edit_event()

    elif user_choice == "4":
        event.view_event()

    elif user_choice == "5":
        event.search_event()

    elif user_choice == "6":
        event.exit()
        break

    else:
        print("\033[1;31m\nInvalid choice. Please try again.\033[0m")

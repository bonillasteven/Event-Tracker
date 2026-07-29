
import Calendar_Define_Module
Calendar_Define_Module.load_events()


print("Welcome to Steven Event Tracker")

while True:
    Calendar_Define_Module.show_main_menu()
    user_choice = input(f"What would like to do? ")

    if user_choice == "1":
        Calendar_Define_Module.add_event()
        
    elif user_choice == "2":
        Calendar_Define_Module.remove_event()
    
    elif user_choice == "3":
        Calendar_Define_Module.edit_event()
        
    elif user_choice == "4":
        Calendar_Define_Module.view_event()
        
    elif user_choice == "5":
        Calendar_Define_Module.search_event()

    elif user_choice == "6":
        Calendar_Define_Module.exit()
        break
    else:
        print("\nInvalid Choice. Please try again.")






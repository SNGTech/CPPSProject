# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:21:27 2022

@author: couts
"""

import menus
import option_functions as options
import os

# Initialise main menu dictionary (INDEX 1: Description, INDEX 2: Function to Call)
main_menu_dict = {
'A': (
"""Based on selected year,
   Show number of dentists by sectors in that year""",
   menus.submenu_A),
'B': (
"""Based on selected sector and year range, 
   Show average number of dentists in that year range
   and minimum number of dentists in that year range and the year it occurred in""", 
   menus.submenu_B),
'C': (
"""Based on selected sector,
   Show highest percentage change year on year and the year it occurred in""",
   menus.submenu_C),
'D': (
"""Based on selected dentist roles for line and bar plots,
   Show line plot of total active dentists for selected role vs Year 
   and bar chart of private and public active dentists for selected role vs Year""",
   menus.submenu_D),
#'E': ("Enter admin mode (display and/or edit data)",
#       data.debug), # MAY ADD IF GOT TIME
'Q': (
"Quit the Portal",
   options.quit_program)
}

def disp_main_menu():
    menus.disp_header("SINGAPORE ACTIVE DENTISTS 2 PORTAL")
    menus.disp_menu("MAIN MENU", main_menu_dict)
    
def clear_console():
    try:
        # Check if running on IPython, if it is, simulate clearing by adding newlines
        __IPYTHON__
        print("\n" * 50)
    except NameError:
        # If not running on IPython, clear the console (since this does not work in IPython)
        os.system('cls' if os.name == 'nt' else 'clear')

# Program loop
while True:
    disp_main_menu()
    sel = input(f"Please select an option ({', '.join(key for key in main_menu_dict)}): ").upper()
    print("") # Add a newline
    
    # Handle invalid options
    if sel not in main_menu_dict.keys():
        print("Option selected is invalid! Please try again")
        input("Press ENTER to continue...")
        print("") # Add a newline
        continue
    # Handle valid options
    main_menu_dict.get(sel)[1]()
    # Wait for ENTER before allowing user to choose new option
    input("Press ENTER to continue...")
    # Clear console for better user readability (multi-platform support code)
    clear_console()
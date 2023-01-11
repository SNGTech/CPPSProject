# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 10:13:06 2022

@author: couts
"""

import option_functions as options
from data import year_range, years

sep_len = 80
sep_header = "=" * sep_len
sep = "-" * sep_len

sector_dict = {
    'A': ("Private Sector", 'private'),
    'B': ("Public Sector", 'public')
}

dentist_roles_dict = {
    'A': ("Dental Specialists", 'dental specialists'),
    'B': ("General Dental Practitioners", 'general dental practitioners')
}

def disp_header(header_text: str):
    print(f"""{sep_header}
{header_text:^{sep_len}}
{sep_header}""")
         
def disp_menu(title_text: str, menu_dict: dict):
    print(f"""{title_text:^{sep_len}}
{sep}""")
    for key, val in menu_dict.items():
        print(f"{key}: {val[0]}\n{sep}")

def menu_select(menu_title: str, item_to_select: str, menu_dict: dict):
    sel = ""
    while True:
        disp_menu(menu_title, menu_dict)
        sel = input(f"Please select a {item_to_select} from the above options ({', '.join(key for key in menu_dict)}): ").upper()
        # Handle invalid options
        if sel not in menu_dict.keys():
            print("\nOption selected is invalid! Please try again")
            print("") # Add a newline
            continue
        break
    return menu_dict.get(sel)[1]

def submenu_A():
    year_sel = 0
    disp_header("OPTION A")
    while True:
        # Validate if its a valid year
        try:
            year_sel = int(input(f"Please select a year from {year_range[0]} to {year_range[1]}: "))
            print("") # Add a newline
        except ValueError:
            print("\nYear selected is invalid! Please try again")
            continue
        # Validate if year is in range
        if year_sel not in years:
            print("Year selected is out of range! Please try again")
            continue
        break
    # Execute option A
    options.disp_num_dentists_by_sector(year_sel)

def submenu_B():
    year_range_sel = ""
    start_year, end_year = 0, 0
    disp_header("OPTION B")
    # Sector selection
    sector_sel = menu_select("SECTOR SUBMENU", "sector", sector_dict)
    # Year range selection
    while True:
        try:
            year_range_sel = input(f"Please enter a year range between {year_range[0]} to {year_range[1]}\nCondition: Start year must be less than the end year\n(Separate start and end year with a comma, e.g. 2015,2019): ").split(",")
            print("") # Add a newline
            start_year = int(year_range_sel[0].lower().strip())
            end_year = int(year_range_sel[1].lower().strip())
        except (ValueError, IndexError):
            print("Year range entered is invalid! Please try again")
            continue
        if start_year not in years or end_year not in years:
            print("Year range entered is out of range! Please try again")
            continue
        if   start_year >= end_year:
            print("Start year must be less than end year! Please try again")
            continue
        break
    # Execute option B
    options.disp_avg_and_min_num_dentists(sector_sel, start_year, end_year)

def submenu_C():
    disp_header("OPTION C")
    # Sector Selection
    sector_sel = menu_select("SECTOR SUBMENU", "sector", sector_dict)
    print("") # Add a newline
    # Execute option C
    options.disp_highest_percent_change_yoy(sector_sel)

def submenu_D():
    disp_header("OPTION D")
    role_line = menu_select("DENTIST ROLES FOR LINE PLOT SUBMENU", 'dentist role', dentist_roles_dict)
    print("") # Add a newline
    role_bar = menu_select("DENTIST ROLES FOR BAR PLOT SUBMENU", 'dentist role', dentist_roles_dict)
    print("\nDisplaying Graphs")
    options.disp_line_plot(role_line)
    options.disp_bar_plots(role_bar)
    
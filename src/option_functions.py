# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:21:51 2022

@author: couts
"""

import data
import numpy as np
import matplotlib.pyplot as plt
import sys

def disp_num_dentists_by_sector(year: int):
    """ Display no. of dentists by sector in selected year """
    # Get row data of dentists of selected year
    num_dentists = []
    for row in data.row_data:
        if row[0] == year:
            num_dentists = row
            break
    num_dentists_private = sum([num_dentists[i] for i in data.sector_indices[0]])
    num_dentists_public = sum([num_dentists[i] for i in data.sector_indices[1]])
    
    print(f"""Number of Dentists by Sector in {year}
          
Private:{num_dentists_private:5}
Public:{num_dentists_public:6}""")

def disp_avg_and_min_num_dentists(sector: str, start_year: int, end_year: int):
    """ Display avg. no. of dentists based on sector from any period (ASK IF NEED TO BE 5-YEAR SPAN) """
    # Obtain sum of dentists yearly for selected period and sector
    sum_dentists_yearly_by_sector = data.get_sum_yearly_by_sector(sector, start_year, end_year)
    
    print(f"For {sector} sector from {start_year} to {end_year}: \n")
    # Obtain Average
    year_range = end_year - start_year + 1
    avg_num_dentists = sum(sum_dentists_yearly_by_sector) / year_range
    print(f"Average number of dentists: {avg_num_dentists:.2f}")
   
    # Obtain Minimum Sum and Corresponding Year
    # MAY OR MAY NOT ADD MAX SUM (Ask Cher First)
    # TODO: REFACTOR OUTPUT
    min_sum_dentists = min(sum_dentists_yearly_by_sector)
    min_year = start_year + sum_dentists_yearly_by_sector.index(min_sum_dentists)
    print(f"Year {min_year} had minimum number of dentists of {min_sum_dentists}")
    
def disp_highest_percent_change_yoy(sector: str):
    """ Display highest percentage change year-on-year and corresponding year it occurred in """
    sum_dentists_yearly_by_sector = data.get_sum_yearly_by_sector(sector)
    # Obtain percentage change yearly list based on selected sector
    percent_change_num_dentists_yearly = []
    for i in range(len(sum_dentists_yearly_by_sector) - 1):
        original, new = sum_dentists_yearly_by_sector[i], sum_dentists_yearly_by_sector[i + 1]
        percent_change = data.calc_percent_change(original, new)
        percent_change_num_dentists_yearly.append(percent_change)
        
    print(f"For {sector} sector from {data.year_range[0]} to {data.year_range[1]}: \n")
    # Obtain highest percentage and corresponding year
    highest_percent_change = max(percent_change_num_dentists_yearly)
    max_year = data.year_range[0] + percent_change_num_dentists_yearly.index(highest_percent_change) + 1
    print(f"Year {max_year} had highest percentage change of {highest_percent_change:.2f}% year on year")
   
def disp_line_plot(dentist_role: str):
    """ # Display line graph """
    # Generate column data (y-axis)
    col_index = [i for i, h in enumerate(data.row_header) if dentist_role in h.lower()]
    total_dentists_by_role_yearly = [sum([row[i] for i in col_index]) for row in data.row_data]
    # Sets up default graph config for other plots to use
    plt.rcParams['figure.figsize'] = (11, 7)
    plt.rcParams['axes.edgecolor'] = '#616161'
    plt.rcParams['xtick.color'] = "#010101"
    plt.rcParams['ytick.color'] = "#010101"
    plt.rcParams['axes.labelcolor'] = "#000000"
    plt.rcParams['axes.axisbelow'] = True
    plt.plot(data.years, total_dentists_by_role_yearly,
             color='#4472c4', linewidth=2, marker='o', markeredgecolor='#FFFFFF', markersize=7)
    plt.xticks(data.years, fontsize=12)
    plt.yticks(fontsize=12)
    plt.xlabel("Year", fontsize=15)
    plt.ylabel("Number of Active Dentists", fontsize=15)
    plt.title(f"Total {dentist_role.title()} vs Year", fontsize=15)
    plt.grid()
    plt.show()
    
def disp_bar_plots(dentist_role: str):
    """ Display bar charts """
    dentists_by_private_role_yearly = []
    dentists_by_public_role_yearly = []
    for i, h in enumerate(data.row_header):
        if "private " + dentist_role in h.lower():
            dentists_by_private_role_yearly = [row[i] for row in data.row_data]  
        if "public " + dentist_role in h.lower():
            dentists_by_public_role_yearly = [row[i] for row in data.row_data]
            
    bar_width = 0.4
    x_loc = np.arange(len(data.years))
    plt.bar(x_loc - bar_width / 2, dentists_by_private_role_yearly, bar_width, 
            color='#4472c4', label=f"Private {dentist_role.title()}",
            linewidth=1, edgecolor='#FFFFFF')
    plt.bar(x_loc + bar_width / 2, dentists_by_public_role_yearly, bar_width, 
            color='#ed7d31', label=f"Public {dentist_role.title()}",
            linewidth=1, edgecolor='#FFFFFF')
    plt.xticks(x_loc, data.years, fontsize=12)
    plt.yticks(fontsize=12)
    plt.xlabel("Year", fontsize=15)
    plt.ylabel("Number of Active Dentists", fontsize=15)
    plt.title(f"Private {dentist_role.title()} and Public {dentist_role.title()} vs Year", fontsize=15)
    plt.legend(loc = 'upper left', fontsize=14)
    plt.grid(axis='y')
    plt.show()
    
def disp_data():
    # Wrapping and centering variables
    top_line = [""] * len(data.row_header)
    bottom_line = [""] * len(data.row_header)
    max_header_len = 20
    # Table separator variables
    table_separator = "-" * (max_header_len * len(data.row_header) + 2)
    # Split all header text to its top and bottom for wrapping
    for i, header in enumerate(data.row_header):
        if len(header) >= max_header_len:
            # Add phrase containing less than 25 chars to top line list
            phrase = header.split(" ")
            for word in header.split(" "):
                if len(top_line[i]) + len(word) <= max_header_len:
                    top_line[i] += word
                    phrase.remove(word)
                    top_line[i] += " "
            if phrase == []:
                phrase = ""
            top_line[i] = top_line[i].strip()
            bottom_line[i] = " ".join(phrase)
            continue
        top_line[i] = header
    # Display header text with wrapping and centering
    print("\nTable of data:")
    print(f"\n{table_separator}")
    for top in top_line:
        print(f"{top:^{max_header_len}}", end="")
    print()
    for bottom in bottom_line:
        print(f"{bottom:^{max_header_len}}", end="")
    print()
    # Display data as a table
    for row in data.row_data:
        print(table_separator)
        for item in row:
            print(f"{item:^{max_header_len}}", end="")
    print(table_separator)

def quit_program():
    """ # Exit with exit code 0 (success) """
    print("Thank you for visiting Singapore Active Dentists 2 Portal\nGoodbye!")
    sys.exit(0)
    

# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 09:51:31 2022

@author: couts
"""

# HANDLE ALL MENU OPTIONS AND CALLING OF OPTION FUNCTIONS

import option_functions as options

def submenu_A():
    options.disp_num_dentists_by_sector()

def submenu_B():
    options.disp_avg_and_min_num_dentists(sector, start_yr, end_yr)

def submenu_C():
    options.disp_highest_percent_change_yoy()

def submenu_D():
    options.disp_line_plot()
    options.disp_bar_plots()
    
    
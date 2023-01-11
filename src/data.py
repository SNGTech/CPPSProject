# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:22:09 2022

@author: couts
"""

import csv
import numpy as np

row_header = []
row_data = []
year_range = []
sector_indices = [0, 0]
years = []

with open("sgactivedentists_dataset.csv", "r") as f:
    reader = csv.reader(f)
    # Create row data from csv, obtain header and obtain data rows in int type
    csv_data = np.array([row for row in reader])
    row_header = csv_data[0]
    row_data = csv_data[1:].astype(int).tolist()
    year_range = (row_data[0][0], row_data[-1][0])
    # Obtain sector indices for use in program (index 0 -> Private, index 1 -> Public)
    sector_indices[0] = [i for i, h in enumerate(row_header) if "Private" in h]
    sector_indices[1] = [i for i, h in enumerate(row_header) if "Public" in h]
    years = list(range(year_range[0], year_range[1] + 1))
    
def get_sum_yearly_by_sector(sector: str, start_yr: int = year_range[0], end_yr: int = year_range[1]):
    """ Obtain sum of data yearly for specified period and sector """
    period_data = row_data[start_yr - year_range[0]:end_yr - year_range[0] + 1]
    if sector == "private":
        return [sum(row[sector_indices[0][0]:sector_indices[0][-1] + 1]) for row in period_data]
    elif sector == "public":
        return [sum(row[sector_indices[1][0]:sector_indices[1][-1] + 1]) for row in period_data]
    else:
        raise Exception("Invalid sector passed into function call!")
        
def calc_percent_change(original: int, new: int):
    """ Percentage change utility function """
    if original > 0:
        return (new - original) / original * 100
    return 0
    
    
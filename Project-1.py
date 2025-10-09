# Project 1 Workspace

import csv
import unittest
import kagglehub
path = kagglehub.dataset_download("samuelotiattakorah/agriculture-crop-yield")
print("Path to dataset files:", path)

# load_crop_data(csv_file)
    # Reads the crop_yield.csv file and transforms the data into a list of dictionaries
    # INPUT: csv_file (string)
    # OUTPUT: loaded_data (list of dictionaries)
def load_crop_data(file):
    pass

# get_subject_dict(subject, loaded_data) helper function
    # From loaded data, find a dictionaries with the subject presented
    # Generate a list of dictionaries with the subject
    # INPUT: a string (subject), list of dictionaries (loaded_data)
    # OUTPUT: list of dictionaries with the subject (crop_data)
def get_subject_dict(subject, loaded_data):
    pass

        

# calc_soybean_rain_percent(crop_data) -- Vida
    # Calculates the percentage of soybean crops in sandy soil that also is recorded as the rainy weather condition
    # INPUT: crop_data (list of dictionaries)
    # OUTPUT: soybean_rain_percentage (float)
def calc_soybean_rain_percent(crop_data):
    pass

# calc_avg_temp_south_soybean(crop_data) -- Vida
    # Calculates the average temperature for soybean crops in the south
    # INPUT: crop_data (list of dictionaries)
    # OUTPUT: avg_temp (float)
def calc_avg_temp_south_soybean(crop_data):
    pass


# calc_avg_rainfall_north_rice(crop_data) -- Mizuki
    # Calculates the average rainfall for rice crops in the north
    # INPUT: crop_data (list of dictionaries)
    # OUTPUT: avg_rainfall (float)
def calc_avg_rainfall_north_rice(crop_data):
    pass


# calc_high_yeild_rice_percent(crop_data) -- Mizuki
    # Calculates the percentage of fertilized rice crops that yield more than 8 tons per hectare
    # INPUT: crop_data (list of dictionaries)
    # OUTPUT: high_yield_percentage (float)
def calc_avg_rainfall_north_rice(crop_data):
    pass


# generate_report(results)
    # Takes a dictionary of calculated results
    # Write them to a file
    # INPUT: a dictionary for calculated results
    # OUTPUT: None (a file)
def generate_report(results):
    pass


# main()
    # Runs the entire program
    # INPUT: None
    # OUTPUT: None
def main():
    pass


# 4 test cases for calculations
# 1

# 2

# 3

# 4
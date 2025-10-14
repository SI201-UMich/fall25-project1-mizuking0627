# Project 1 Workspace

import csv
import unittest

# load_crop_data(csv_file)
    # Reads the crop_yield.csv file and transforms the data into a list of dictionaries
    # INPUT: csv_file (string)
    # OUTPUT: loaded_data (list of dictionaries)
def load_crop_data(file):
    with open(file) as fh:
        reader = csv.reader(fh)
        content = list(reader)

        titles = content[0]
        loaded_data = []

        for line in content[1:]:
            line_d = {}
            for i in range(len(line)):
                line_d[titles[i]] = line[i]
            loaded_data.append(line_d)
    
    print(loaded_data)
    return loaded_data
      
load_crop_data('crop_yield.csv')

# get_subject_dict(subject, loaded_data) helper function
    # From loaded data, find a dictionaries with the subject presented
    # Generate a list of dictionaries with the subject
    # INPUT: a string (subject), list of dictionaries (loaded_data)
    # OUTPUT: list of dictionaries with the subject (crop_data)
def get_subject_dict(subject, loaded_data):
    crop_data = []
    for line in loaded_data:
        if subject in line.values():
            crop_data.append(line)
    return crop_data
    pass

# calc_soybean_rain_percent(crop_data) -- Vida
    # Calculates the percentage of soybean crops in sandy soil that also is recorded as the rainy weather condition
    # INPUT: crop_data (list of dictionaries)
    # OUTPUT: soybean_rain_percentage (float)
def calc_soybean_rain_percent(crop_data):
    soybean_count = 0
    sandy_rainy_count = 0

    if len(crop_data) == 0:
        return 0

    for line in crop_data:
        if line['Crop'] == 'Soybean':
            soybean_count += 1
            if line['Soil_Type'] == 'Sandy' and line['Weather_Condition'] == 'Rainy':
                sandy_rainy_count += 1

    if soybean_count == 0:
        return 0
    
    avg = sandy_rainy_count / soybean_count
    return avg
    pass


# calc_avg_temp_south_soybean(crop_data) -- Vida
    # Calculates the average temperature for soybean crops in the south
    # INPUT: crop_data (list of dictionaries)
    # OUTPUT: avg_temp (float)
def calc_avg_temp_south_soybean(crop_data):
    total_temp = 0
    count = 0

    if len(crop_data) == 0:
        return 0
    
    for line in crop_data:
        if line['Crop'] == 'Soybean' and line['Region'] == 'South':
            total_temp += float(line['Temperature_Celsius'])
            count += 1

    if count == 0:
        return 0
    
    avg = total_temp / count
    return avg
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

class TestCropCalculations(unittest.TestCase):
# 4 test cases for each calculations
# Calc 1 (Vida)

# Calc 2 (Vida)

# Calc 3 (Mizuki)

    def test_avg_rainfall_north_general(self):
        result = calc_avg_rainfall_north_rice(self.test_data)
        self.assertEqual(result, 175.0)

    def test_avg_rainfall_north_edge_empty(self):
        data = [{'Crop': 'Rice', 'Region': 'South', 'Rainfall_mm': 120.0}]
        result = calc_avg_rainfall_north_rice(data)
        self.assertEqual(result, 0.0)



#     (not implemented yet)

# Calc 4 (Mizuki)
# (not implemented yet)



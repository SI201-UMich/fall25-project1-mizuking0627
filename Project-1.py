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
    # Regular test case 1
    def test_calc_soybean_rain_percent_single(self):
        sample_data1 = [{'Region': 'North', 'Soil_Type': 'Sandy', 'Crop': 'Soybean', 'Rainfall_mm': '986.8663313367325', 'Temperature_Celsius': '16.64419019137728', 'Fertilizer_Used': 'False', 'Irrigation_Used': 'True', 'Weather_Condition': 'Rainy', 'Days_to_Harvest': '146', 'Yield_tons_per_hectare': '6.517572507555278'},
                        {'Region': 'South', 'Soil_Type': 'Silt', 'Crop': 'Soybean', 'Rainfall_mm': '797.4711823962564', 'Temperature_Celsius': '37.70497446941277', 'Fertilizer_Used': 'False', 'Irrigation_Used': 'True', 'Weather_Condition': 'Rainy', 'Days_to_Harvest': '74', 'Yield_tons_per_hectare': '5.898416311841461'},
                        {'Region': 'North', 'Soil_Type': 'Loam', 'Crop': 'Soybean', 'Rainfall_mm': '600.1997541490214', 'Temperature_Celsius': '20.935360153951528', 'Fertilizer_Used': 'True', 'Irrigation_Used': 'False', 'Weather_Condition': 'Sunny', 'Days_to_Harvest': '75', 'Yield_tons_per_hectare': '4.8981807530789006'}]
        result = calc_soybean_rain_percent(self.sample_data1)
        self.assertAlmostEqual(result, 0.3333)

    # Regular test case 2
    def test_calc_soybean_rain_percent_multiple(self):
        sample_data2 = [{'Region': 'North', 'Soil_Type': 'Sandy', 'Crop': 'Soybean', 'Rainfall_mm': '986.8663313367325', 'Temperature_Celsius': '16.64419019137728', 'Fertilizer_Used': 'False', 'Irrigation_Used': 'True', 'Weather_Condition': 'Rainy', 'Days_to_Harvest': '146', 'Yield_tons_per_hectare': '6.517572507555278'},
                        {'Region': 'South', 'Soil_Type': 'Silt', 'Crop': 'Soybean', 'Rainfall_mm': '797.4711823962564', 'Temperature_Celsius': '37.70497446941277', 'Fertilizer_Used': 'False', 'Irrigation_Used': 'True', 'Weather_Condition': 'Rainy', 'Days_to_Harvest': '74', 'Yield_tons_per_hectare': '5.898416311841461'},
                        {'Region': 'North', 'Soil_Type': 'Loam', 'Crop': 'Soybean', 'Rainfall_mm': '600.1997541490214', 'Temperature_Celsius': '20.935360153951528', 'Fertilizer_Used': 'True', 'Irrigation_Used': 'False', 'Weather_Condition': 'Sunny', 'Days_to_Harvest': '75', 'Yield_tons_per_hectare': '4.8981807530789006'},
                        {'Region': 'West', 'Soil_Type': 'Sandy', 'Crop': 'Soybean', 'Rainfall_mm': '655.5829114621207', 'Temperature_Celsius': '22.490469797002447', 'Fertilizer_Used': 'True', 'Irrigation_Used': 'False', 'Weather_Condition': 'Rainy', 'Days_to_Harvest': '105', 'Yield_tons_per_hectare': '5.268460324634402'}]
        result = calc_soybean_rain_percent(sample_data2)
        self.assertAlmostEqual(result, 0.5)

    # Edge case 1
    def test_no_soybeans(self):
        sample_data3 = [{'Region': 'East', 'Soil_Type': 'Sandy', 'Crop': 'Cotton', 'Rainfall_mm': '145.3006808203336', 'Temperature_Celsius': '19.755534985496798', 'Fertilizer_Used': 'True', 'Irrigation_Used': 'True', 'Weather_Condition': 'Cloudy', 'Days_to_Harvest': '141', 'Yield_tons_per_hectare': '4.367612094467675'},
                        {'Region': 'East', 'Soil_Type': 'Chalky', 'Crop': 'Rice', 'Rainfall_mm': '874.4567441463316', 'Temperature_Celsius': '27.25686895920963', 'Fertilizer_Used': 'True', 'Irrigation_Used': 'False', 'Weather_Condition': 'Sunny', 'Days_to_Harvest': '115', 'Yield_tons_per_hectare': '5.839291310818685'}]
        result = calc_soybean_rain_percent(sample_data3)
        self.assertEqual(result, 0)

    # Edge case 2
    def test_nothing_in_list(self):
        sample_data4 = []
        result = calc_soybean_rain_percent(sample_data4)
        self.assertEqual(result, 0)


# Clac 2 (Vida)
    # Regular test case 1
    def test_calc_avg_temp_south_soybean_multiple(self):
        sample_data1 = [{'Region': 'South', 'Soil_Type': 'Silt', 'Crop': 'Soybean', 'Rainfall_mm': '797.4711823962564', 'Temperature_Celsius': '37.70497446941277', 'Fertilizer_Used': 'False', 'Irrigation_Used': 'True', 'Weather_Condition': 'Rainy', 'Days_to_Harvest': '74', 'Yield_tons_per_hectare': '5.898416311841461'},
                        {'Region': 'South', 'Soil_Type': 'Silt', 'Crop': 'Soybean', 'Rainfall_mm': '713.9886919759452', 'Temperature_Celsius': '33.86148554253913', 'Fertilizer_Used': 'True' , 'Irrigation_Used': 'True', 'Weather_Condition': 'Sunny', 'Days_to_Harvest': '70', 'Yield_tons_per_hectare': '6.960186332830285'}]
        result = calc_avg_temp_south_soybean(sample_data1)
        self.assertAlmostEqual(result, 35.7832)

    # Regular test case 2
    def test_calc_avg_temp_south_soybean_single(self):
        sample_data2 = [{'Region': 'South', 'Soil_Type': 'Silt', 'Crop': 'Soybean', 'Rainfall_mm': '797.4711823962564', 'Temperature_Celsius': '37.70497446941277', 'Fertilizer_Used': 'False', 'Irrigation_Used': 'True', 'Weather_Condition': 'Rainy', 'Days_to_Harvest': '74', 'Yield_tons_per_hectare': '5.898416311841461'}]
        result = calc_avg_temp_south_soybean(sample_data2)
        self.assertAlmostEqual(result, 37.7049)
    
    # Edge case 1
    def test_no_south_soybeans(self):
        sample_data3 = [{'Region': 'North', 'Soil_Type': 'Sandy', 'Crop': 'Soybean', 'Rainfall_mm': '986.8663313367325', 'Temperature_Celsius': '16.64419019137728', 'Fertilizer_Used': 'False', 'Irrigation_Used': 'True', 'Weather_Condition': 'Rainy', 'Days_to_Harvest': '146', 'Yield_tons_per_hectare': '6.517572507555278'},
                        {'Region': 'East', 'Soil_Type': 'Chalky', 'Crop': 'Rice', 'Rainfall_mm': '874.4567441463316', 'Temperature_Celsius': '27.25686895920963', 'Fertilizer_Used': 'True', 'Irrigation_Used': 'False', 'Weather_Condition': 'Sunny', 'Days_to_Harvest': '115', 'Yield_tons_per_hectare': '5.839291310818685'}]
        result = calc_avg_temp_south_soybean(sample_data3)
        self.assertEqual(result, 0)

    # Edge case 2
    def test_nothing_in_list(self):
        sample_data4 = []
        result = calc_avg_temp_south_soybean(sample_data4)
        self.assertEqual(result, 0)

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



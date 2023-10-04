# Author:         Delijah Joseph
# Major:          Information Technology
# Creation Date:  February 25, 2022
# Due Date:       March 4, 2022
# Course:         CSC223
# Professor Name: Professor Earl
# Assignment:     #3
# Filename:       main.py
# Purpose:        Usage of Python Standard Library Modules, Understanding of the CSV and JSON file formats

import csv
import json
def main():
    """
    Description: Converts netflix titles.csv to netflix titles.json
    Parameters: None
    Return Values: None
    """
    data = []
    shows = {}

    f = open('netflix_titles.csv', encoding= 'utf-8')
    csv_reader = csv.reader(f)

    for line in csv_reader:
        if line[1] == 'TV Show':

            shows['show_id'] = line[0]
            shows['title'] = line[2]
            shows['director'] = line[3]
            shows['country'] = line[5]
            shows['date_added'] = line[6]
            shows['duration'] = line[9]
            data.append(shows.copy())
    data = sorted(data, key=lambda d: d['duration'], reverse=True)

    with open('netflix_titles.json', 'w') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
if  __name__ == "__main__":
    main()
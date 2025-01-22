"""
Schengulator is a tool to calculate how many days an individual has been in
Schengen countries out of a specified 180-day period.

@author: Penelope How
"""
import csv
        
def stays_from_csv(csv_file):
    '''Read past stays from CSV
    
    Parameters
    ----------
    csv_file : str
        File path to CSV file containing past stays

    Returns
    -------
    stays : list
      List of date strings of start and end of all stays i.e. [[start1, end1],
      [start2, end2]]
    '''
    stays = []
    print(f'\nImporting stays from {csv_file}')
    with open(csv_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        count=0
        for row in csv_reader:
            if count==0:
                count += 1
            else:
                stays.append([row[0], row[1]])
                print(f'\tStay #{count} ({row[0]} - {row[1]}) {row[2]}')
                count += 1
    return stays
    
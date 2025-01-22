"""
Schengulator is a tool to calculate how many days an individual has been in
Schengen countries out of a specified 180-day period.

@author: Penelope How
"""
from schengulator.check_stay import check_stay
from schengulator.get_date import get_date
from schengulator.schengenstay import SchengenStay
from schengulator.check_days_left import check_days_left
from schengulator.stays_from_csv import stays_from_csv
import datetime as dt
import os

def test_specific_date():
    '''Check Schengen stays from specific date using SchengenStay obj
    #Initialise Schengen evaluation from 01/05/2022
    '''
    ss = SchengenStay('2022-05-01')
    
    #Add all stays
    ss.add_stay('2021-07-01', '2021-07-15')         # Holiday in Greece
    ss.add_stay('2021-09-03', '2021-09-08')         # Business trip in The Netherlands
    ss.add_stay('2021-09-20', '2021-09-25')         # Visiting family in Belgium
    ss.add_stay('2021-12-20', '2022-01-03')         # Family Christmas in Belgium
    ss.add_stay('2022-04-18', '2022-05-01')         # Proposed holiday to Italy
    
    #Check number of days spent in Schengen on 01/05/2022
    flag = ss.check_days()
    if flag==True:
        print('All okay!')  


def test_stays():
    '''Check Schengen stays for all dates in proposed future stay
    '''
    #Create list of all stays
    trips = [['2021-07-01','2021-07-15'],         # Holiday in Greece
            ['2021-09-03', '2021-09-08'],         # Business trip in The Netherlands
            ['2021-09-20', '2021-09-25'],         # Visiting family in Belgium
            ['2021-12-20', '2022-01-03'],         # Family Christmas in Belgium
            ['2022-04-18', '2022-05-01']]         # Proposed holiday to Italy
    
    #Check if new stay is within Schengen 90-day limits
    check_stay(['2022-04-18', '2022-05-01'], trips[:-1])
    
    #See how many days left in Schengen after proposed trip
    check_days_left(trips)


def test_from_csv():
    '''Check Schengen stays from CSV file
    '''
    #Import stays from csv file
    infile = 'examples/example_stays.csv'
    
    pkg_dir, pkg_filename = os.path.split(__file__)
    data_path = os.path.join(pkg_dir, "example_stays.csv")
    csv_trips = stays_from_csv(data_path)
    
    #Check if new trip is within Schengen 90-day limits
    new_trip = ['2022-01-05', '2022-01-20']
    check_stay(new_trip, csv_trips)
    
    #Check how many days left in Schengen after new trip
    csv_trips.append(new_trip)
    check_days_left(csv_trips, d=new_trip[1]) 
    
    
#------------------------------------------------------------------------------
if __name__ == "__main__":
    test_specific_date()
    test_stays()
    test_from_csv()

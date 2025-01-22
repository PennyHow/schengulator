"""
Schengulator is a tool to calculate how many days an individual has been in
Schengen countries out of a specified 180-day period. The Schengulator 
determines the number of days spent and remaining based on the 90/180 Schengen 
Visa Rule:
    
"The 180-day period keeps rolling. Therefore, anytime you wish to enter the 
Schengen, you just have to count backwards the last 180 days, and see if you 
have been present in the Schengen for more than 90 days throughout that period"

This tool was inspired by these related python repositories:
- schengen: https://github.com/weddige/schengen
- schengencalc: https://github.com/nuno-filipe/schengencalc

@author: Penelope How
"""
from schengulator.schengenstay import SchengenStay
from schengulator.check_stay import check_stay
from schengulator.check_days_left import check_days_left
from schengulator.stays_from_csv import stays_from_csv

# Example 1. Check Schengen stays from specific date using SchengenStay obj
#Initialise Schengen evaluation from 01/05/2022
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
    
 
    
# Example 2. Check Schengen stays for all dates in proposed future stay
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



# Example 3. Check Schengen stays from CSV file
#Import stays from csv file
infile = 'example_stays.csv'
csv_trips = stays_from_csv(infile)

#Check if new trip is within Schengen 90-day limits
new_trip = ['2022-01-05', '2022-01-20']
check_stay(new_trip, csv_trips)

#Check how many days left in Schengen after new trip
csv_trips.append(new_trip)
check_days_left(csv_trips, d=new_trip[1]) 

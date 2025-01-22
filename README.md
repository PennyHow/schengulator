# Schengulator

[![Documentation Status](https://readthedocs.org/projects/schengulator/badge/?version=latest)](https://schengulator.readthedocs.io/en/latest/?badge=latest) [![PyPI version](https://badge.fury.io/py/schengulator.svg)](https://badge.fury.io/py/schengulator)

Schengulator is a tool to calculate how many days an individual has been in Schengen countries out of a specified 180-day period.

## The Schengen Visa Rule

The schengulator determines the number of days spent and remaining based on the 90/180-day Schengen Visa Rule, where an individual can stay in Schengen countries for 90 days out of an 180 day time period. The 180-day window is defined as:
    
*"The 180-day period keeps rolling. Therefore, anytime you wish to enter the Schengen, you just have to count backwards the last 180 days, and see if you have been present in the Schengen for more than 90 days throughout that period"* (as stated [here](https://www.schengenvisainfo.com/visa-calculator))

Therefore, schengulator calculates the days spent in the Schengen area based on the 180 days prior to a user-defined date.

For more on the Schengen Visa Rule, see these links:
+ [Schengen visa info](https://www.schengenvisainfo.com)
+ [The 90/180-day rule made easy](https://newlandchase.com/the-schengen-areas-90-180-day-rule-made-easy/)
+ [UK Government on visa permits in Europe](https://www.gov.uk/guidance/check-if-you-need-a-visa-or-permit-for-europe)
+ [The Schengen rule: here's how it works](https://www.frenchentree.com/brexit/eu-90-180-day-rule-heres-how-it-works/)

There are many Schengen stay calculators available online or as apps. The purpose of schengulator is to create a workflow that is **transparent** (i.e. you can see the workings) and **non-repetitive** (i.e. you don't have to log each and every one of your trips to the Schengen area every time you need to use the tool).
 

## Quickstart
To get started, install schengulator using pip.

```python
pip install schengulator
```

Check that the package works by opening a python console and importing it.

```python
python3
import schengulator
```

There are a number of examples in the scripts provided in the [examples](https://github.com/PennyHow/schengulator/tree/main/examples) directory of the [schengulator Github repository](https://github.com/PennyHow/schengulator) to test the installation and see how it works. 

```python
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
```

## Acknowledgements
This tool was inspired by these related python repositories:
+ [schengen](https://github.com/weddige/schengen)
+ [schengencalc](https://github.com/nuno-filipe/schengencalc)

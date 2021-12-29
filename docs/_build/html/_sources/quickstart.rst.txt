Quickstart
==========

To get started, install schengulator using pip.

.. code-block:: python
   pip install schengulator

Schengulator's only dependencies are **datetime** and **csv** for handling date objects and loading from csv files, respectively. These are usually in-built packages to Python distributions, and therefore there should not be any compatibility issues.

Check that the package works by opening a python console and importing it.

.. code-block:: python
   python3
   import schengulator

There are a number of examples in the scripts provided in the `examples <https://github.com/PennyHow/schengulator/tree/main/examples>`_ directory of the `schengulator Github repository <https://github.com/PennyHow/schengulator>`_ to test the installation and see how it works. 

.. code-block:: python
   from schengulator import SchengenStay, checkStay, /
      checkDaysLeft, staysFromCSV

   # Example 1. Check Schengen stays from specific date 
   # using SchengenStay obj

   # Initialise Schengen evaluation from 01/05/2022
   ss = SchengenStay('2022-05-01')

   # Add all stays
   ss.addStay('2021-07-01', '2021-07-15')      # Greece
   ss.addStay('2021-09-03', '2021-09-08')      # Netherlands
   ss.addStay('2021-09-20', '2021-09-25')      # Belgium
   ss.addStay('2021-12-20', '2022-01-03')      # Belgium
   ss.addStay('2022-04-18', '2022-05-01')      # Italy

   # Check number of days spent in Schengen on 01/05/2022
   flag = ss.checkDays()
   if flag==True:
       print('All okay!')
    
 
    
   # Example 2. Check Schengen stays for all dates in 
   # proposed future stay

   # Create list of all stays
   trips = [['2021-07-01','2021-07-15'],     # Greece
           ['2021-09-03', '2021-09-08'],     # Netherlands
           ['2021-09-20', '2021-09-25'],     # Belgium
           ['2021-12-20', '2022-01-03'],     # Belgium
           ['2022-04-18', '2022-05-01']]     # Italy

   # Check if new stay is within Schengen 90-day limits
   checkStay(['2022-04-18', '2022-05-01'], trips[:-1])

   # See how many days left in Schengen after proposed trip
   checkDaysLeft(trips)



   # Example 3. Check Schengen stays from CSV file
  
   # Import stays from csv file
   infile = 'examples/example_stays.csv'
   csv_trips = staysFromCSV(infile)

   # Check if new trip is within Schengen 90-day limits
   new_trip = ['2022-01-05', '2022-01-20']
   checkStay(new_trip, csv_trips)

   # Check how many days left in Schengen after new trip
   csv_trips.append(new_trip)
   checkDaysLeft(csv_trips, d=new_trip[1]) 

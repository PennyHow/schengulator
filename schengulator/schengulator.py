"""
Schengulator is a tool to calculate how many days an individual has been in
Schengen countries out of a specified 180-day period.

@author: Penelope How
"""

import csv
import datetime as dt

#------------------------------------------------------------------------------

class Stay(object):
    '''Holds all attributes atributed to a stay in a country, or a trip away
    from the home country
    
    Attributes
    ----------
    start : datetime.date
      Start date of stay
    end : datetime.date
      End date of stay
    '''
    def __init__(self, start, end):
        '''Initialise Stay object
        
        Parameters
        ----------
        start : str
          Start date of stay
        end : str
          End date of stay
        '''
        self.start = getDate(start)            
        self.end = getDate(end)

    def getDelta(self):
        '''Get time delta between start and end date of stay
        
        Returns
        -------
        datetime.delta
          Time delta of date range'''
        return self.end - self.start
    
    def getDates(self):
        '''Get all dates within start and end date of stay
        
        Returns
        -------
        list
          List of all dates within date range
        '''
        delta = self.getDelta()
        d = [self.start + dt.timedelta(days=i) for i in range(delta.days + 1)]
        return d

    def checkStay(self, d1, d2):
        '''Check if any date of stay is within a given date range
        
        Parameters
        ----------
        d1 : datetime.date
          Start date
        d2 : datetime.date
          End date
        
        Returns
        -------
        flag : bool
          Flag denoting if stay is within (True) or outside (False) of given
          date range
        '''
        d = self.getDates()
        flag=False
        for ele in d:
            if ele >= d1 and ele <= d2:
                flag=True
        return flag
    
    def countStay(self, d1, d2):
        '''Count number of days of stay within a given date range
        
        Parameters
        ----------
        d1 : datetime.date
            Start date
        d2 : datetime.date
            End date

        Returns
        -------
        count : int
            Number of days of stay that are within given date range
        '''
        d = self.getDates()
        count=0
        for ele in d:
            if ele >= d1 and ele <= d2:
                count=count+1
        return count
        

class SchengenStay(object):
    '''Holds all attributes associated with a stay or collection of stays 
    within the Schengen zone (or outside of home country)
    
    Attributes
    ----------
    date1 : datetime.date
      End date
    date0 : datetime.date
      Start date
    window : int
      Window of evaluation to check stays in Schengen area or stays outside of 
      home country (default=180 days)
    stays : list
      List of Stay objects, representing stays within the Schengen zone (or
      outside of home country)
    '''
    def __init__(self, d1=dt.date.today(), window=180):
        '''Initialisation for SchengenStay object
        
        Parameters
        ----------
        d : str, optional
          Date that 180 day period is calculated from. If parameter is not 
          given then today's date is used (default=datetime.date.today())
        '''
        self.date1 = getDate(d1)        
        self.window = window
        self.date0 = self.date1 - dt.timedelta(days=window)
        self.stays = []
    
    def getStartDate(self):
        '''Get start of 180 day period, which is calculated from the inputted
        date to initialise the SchengenStay object
        
        Returns
        -------
        datetime.date
          Start date of 180 day period
        '''
        return self.date0
    
    def addStay(self, start, end):
        '''Add stay (as Stay object)
        
        Parameters
        ----------
        start : str
          Start date of stay
        End : str
          End date of stay
        '''
        new_stay = Stay(start, end)
        self.stays.append(new_stay)
       
    def getDays(self):
        '''Get number of days in Schengen area  (or out of home country) 
        within the given 180 day period, based on inputted stays
        
        Returns
        -------
        days_out : int
          Number of days in Schengen area
        '''
        days_out = 0
        for s in self.stays:
                        
            #Count stay days that are within date range
            c = s.countStay(self.date0, self.date1)
                
            #Add to number of days in schengen
            days_out = days_out + c
        return days_out
    
    def checkDays(self, days=90):
        '''Check if number of days in Schengen period is less than 90 days 
        within the given 180 day period, based on inputted stays
        
        Parameters
        ----------
        days : int, optional 
          Maximum number of days in Schengen area or out of home country
        Returns
        -------
        bool
          Flag denoting if the number of days in below (True) or above (False)
          90 days
        '''
        d = self.getDays()
        print(f'\tDays spent in schengen areas from {self.date0} to ' +
              f'{self.date1}: {d}') 
        if d <= days:
            return True
        else:
            return False

#------------------------------------------------------------------------------        

def checkStay(staydate, stays, window=180):  
    '''Check proposed stay is inkeeping with Schengen 90-day rule and past
    stays in Schengen countries (or out of home country)    

    Parameters
    ----------
    staydate : list
        List containing start and end date of proposed stay
    stays : list
        List of all past stays i.e. [[start1, end1], [start2, end2]]
    '''
    #Initiate proposed stay as object
    stay = Stay(staydate[0], staydate[1])
    print(f'\nChecking stay between {stay.start} and {stay.end}')
    
    #Iterate through all days in proposed stay
    for d in stay.getDates():
        
        #Initialise SchengenStay object and add all past trips
        ss = SchengenStay(d, window)
        [ss.addStay(s[0],s[1]) for s in stays]
        ss.addStay(staydate[0], staydate[1])
        
        #Check how many days in Schengen country
        flag = ss.checkDays()
        if flag == False:
            print('Trip does not work as it is over 90 days!')  

def checkDaysLeft(stays, d=dt.date.today(), max_days=90, window=180): 
    '''Check the number of days left to visit Schengen area (or stay out of 
    home country). Two answers are given - a theoretical leave date and an
    actual leave date. The theoretical leave date is the remaining number of 
    days that you can stay in the Schengen area, assuming that the 180-day 
    window remains static (i.e. evaluated from the same dates). The actual 
    leave date is the remaining number of days that you can stay in the 
    Schengen area, assuming that the 180-day window is dynamic and moves with 
    the final day of the last recorded stay (i.e. as if your final trip keeps
    extending day-to-day as you continue to stay in a Schengen country)
    
    Parameters
    ----------
    stays : list
      List of all past stays e.g. [[start1, end1], [start2, end2]]
    d : str/datetime.date
      Date to evaluate from. Today's date is used if this is not specified 
      (default=datetime.date.today())
    max_days : int
      Maximum number of days that can be spent in Schengen area, or out of
      home country (default=90)
    window : int
      Window of evaluation (default=180)
    '''
    #Initiate object
    d = getDate(d)   
    ss = SchengenStay(d, window)
    print(f'\nChecking days left from {ss.date1}')
    
    #Add all stays and calculate days spent
    [ss.addStay(s[0],s[1]) for s in stays] 
    days_out = ss.getDays()    
    if days_out <= max_days:
        print(f'\tDays remaining in schengen areas from {ss.date0} to ' +
              f'{ss.date1}: {max_days-days_out}') 
        
        #Determine theoretical days left
        days_left = max_days - days_out
        max_enddate = d + dt.timedelta(days=days_left)
        print(f'\tIf you are staying in a schengen country after {d}, you ' +
              f'theoretically need to leave by {max_enddate}')
        
        #Convert all dates to datetime objects
        new_stays=[]
        for s in stays:
            new_stays.append([dt.datetime.strptime(s[0],"%Y-%m-%d").date(),
                              dt.datetime.strptime(s[1],"%Y-%m-%d").date()])
        
        #Iterate until days spent is equal to or more than maximum days
        while True:
            
            #Change last stay day by one day
            n = [new_stays[-1][0], new_stays[-1][1]+dt.timedelta(days=1)]
            new_stays = new_stays[:-1]
            new_stays.append(n)
            
            #Re-initialise SchengenStay object
            ss = SchengenStay(new_stays[-1][1], window)
            [ss.addStay(d[0], d[1]) for d in new_stays]
            
            #Determine days out with revised stays
            days_out = ss.getDays()
            if days_out >= max_days:
                break
        print(f'\tIf you are staying in a schengen country after {d}, you ' +
              f'can actually leave by {ss.stays[-1].end}')           
    else:
        print(f'\tDays over maximum stay period: {days_out-max_days}\n'+
              'Leave the schengen area now!')

def getDate(d):
    '''Export date as datetime.date, or check if date passed is datetime.date
    
    Parameters
    ----------
    d : str/datetime.date
      Date
      
    Returns 
    -------
    datetime.date
      Datetime date
    '''
    if isinstance(d, str):
        return dt.datetime.strptime(d, "%Y-%m-%d").date()
    elif isinstance(d, dt.date):
        return d  
    elif isinstance(d, dt.datetime):
        return d.date()
        
def staysFromCSV(csv_file):
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
    
#------------------------------------------------------------------------------

    
if __name__ == "__main__":
    
    # Example 1. Check Schengen stays from specific date using SchengenStay obj
    #Initialise Schengen evaluation from 01/05/2022
    ss = SchengenStay('2022-05-01')
    
    #Add all stays
    ss.addStay('2021-07-01', '2021-07-15')         # Holiday in Greece
    ss.addStay('2021-09-03', '2021-09-08')         # Business trip in The Netherlands
    ss.addStay('2021-09-20', '2021-09-25')         # Visiting family in Belgium
    ss.addStay('2021-12-20', '2022-01-03')         # Family Christmas in Belgium
    ss.addStay('2022-04-18', '2022-05-01')         # Proposed holiday to Italy
    
    #Check number of days spent in Schengen on 01/05/2022
    flag = ss.checkDays()
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
    checkStay(['2022-04-18', '2022-05-01'], trips[:-1])
    
    #See how many days left in Schengen after proposed trip
    checkDaysLeft(trips)



    # Example 3. Check Schengen stays from CSV file
    #Import stays from csv file
    infile = 'examples/example_stays.csv'
    csv_trips = staysFromCSV(infile)
    
    #Check if new trip is within Schengen 90-day limits
    new_trip = ['2022-01-05', '2022-01-20']
    checkStay(new_trip, csv_trips)
    
    #Check how many days left in Schengen after new trip
    csv_trips.append(new_trip)
    checkDaysLeft(csv_trips, d=new_trip[1]) 

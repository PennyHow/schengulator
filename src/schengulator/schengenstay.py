"""
Schengulator is a tool to calculate how many days an individual has been in
Schengen countries out of a specified 180-day period.

@author: Penelope How
"""
from schengulator.get_date import get_date
from schengulator.stay import Stay
import datetime as dt

#------------------------------------------------------------------------------


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
        self.date1 = get_date(d1)        
        self.window = window
        self.date0 = self.date1 - dt.timedelta(days=window)
        self.stays = []
    
    def get_start_date(self):
        '''Get start of 180 day period, which is calculated from the inputted
        date to initialise the SchengenStay object
        
        Returns
        -------
        datetime.date
          Start date of 180 day period
        '''
        return self.date0
    
    def add_stay(self, start, end):
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
       
    def get_days(self):
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
            c = s.count_stay(self.date0, self.date1)
                
            #Add to number of days in schengen
            days_out = days_out + c
        return days_out
    
    def check_days(self, days=90):
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
        d = self.get_days()
        print(f'\tDays spent in schengen areas from {self.date0} to ' +
              f'{self.date1}: {d}') 
        if d <= days:
            return True
        else:
            return False

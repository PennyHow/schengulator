"""
Schengulator is a tool to calculate how many days an individual has been in
Schengen countries out of a specified 180-day period.

@author: Penelope How
"""
from schengulator.get_date import get_date
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
        self.start = get_date(start)            
        self.end = get_date(end)

    def get_delta(self):
        '''Get time delta between start and end date of stay
        
        Returns
        -------
        datetime.delta
          Time delta of date range'''
        return self.end - self.start
    
    def get_dates(self):
        '''Get all dates within start and end date of stay
        
        Returns
        -------
        list
          List of all dates within date range
        '''
        delta = self.get_delta()
        d = [self.start + dt.timedelta(days=i) for i in range(delta.days + 1)]
        return d

    def check_stay(self, d1, d2):
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
        d = self.get_dates()
        flag=False
        for ele in d:
            if ele >= d1 and ele <= d2:
                flag=True
        return flag
    
    def count_stay(self, d1, d2):
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
        d = self.get_dates()
        count=0
        for ele in d:
            if ele >= d1 and ele <= d2:
                count=count+1
        return count

"""
Schengulator is a tool to calculate how many days an individual has been in
Schengen countries out of a specified 180-day period.

@author: Penelope How
"""

import datetime as dt

def get_date(d):
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

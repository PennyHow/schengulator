"""
Schengulator is a tool to calculate how many days an individual has been in
Schengen countries out of a specified 180-day period.

@author: Penelope How
"""
import datetime as dt
from schengulator.get_date import get_date
from schengulator.schengenstay import SchengenStay

def check_days_left(stays, d=dt.date.today(), max_days=90, window=180): 
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
    d = get_date(d)   
    ss = SchengenStay(d, window)
    print(f'\nChecking days left from {ss.date1}')
    
    #Add all stays and calculate days spent
    [ss.add_stay(s[0],s[1]) for s in stays] 
    days_out = ss.get_days()    
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
            [ss.add_stay(d[0], d[1]) for d in new_stays]
            
            #Determine days out with revised stays
            days_out = ss.get_days()
            if days_out >= max_days:
                break
        print(f'\tIf you are staying in a schengen country after {d}, you ' +
              f'can actually leave by {ss.stays[-1].end}')           
    else:
        print(f'\tDays over maximum stay period: {days_out-max_days}\n'+
              'Leave the schengen area now!')

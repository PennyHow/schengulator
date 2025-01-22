"""
Schengulator is a tool to calculate how many days an individual has been in
Schengen countries out of a specified 180-day period.

@author: Penelope How
"""

from schengulator.stay import Stay
from schengulator.schengenstay import SchengenStay

def check_stay(staydate, stays, window=180):  
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
    for d in stay.get_dates():
        
        #Initialise SchengenStay object and add all past trips
        ss = SchengenStay(d, window)
        [ss.add_stay(s[0],s[1]) for s in stays]
        ss.add_stay(staydate[0], staydate[1])
        
        #Check how many days in Schengen country
        flag = ss.check_days()
        if flag == False:
            print('Trip does not work as it is over 90 days!')  

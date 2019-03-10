import re
from datetime import datetime

from ..util import *

def getPrecincts(crime_horizon: str, crime: str):

    dataset_id = getDatasetID(crime_horizon, crime)
    json_list = makeRequest('precinct', dataset_id) 

    # For every dictionary in json return
    title_text = json_list[0]['Title']
    date_span = __parseDate(title_text)
    precinct_list = []

    for i in json_list:
        precinct = __trimPrecinctNumber(i['SeriesLabel'])
        incidents = int(i['Value'])
        precinct.replace('0', '')
        
        pair = {precinct:incidents}
        precinct_list.append(pair)

    return [date_span, precinct_list]



# Trims excess 0s from the front of precinct numbers,
# e.g: 014 ---> 14
def __trimPrecinctNumber(precinct_num: str) -> str:
    for char in precinct_num:
        if char == '0':
            precinct_num = precinct_num.replace(char, '')
        else:
            return precinct_num
    
    return "0"

def __parseDate(title_text: str) -> list:
    returnList = []
    
    matches = re.findall(r'(\d{2}\/\d{2}\/\d{2})', title_text)

    for match in matches:
        if match is not None:
            date_obj = datetime.strptime(match, '%m/%d/%y').date()
            date = date_obj.strftime('%Y-%m-%d ')
            returnList.append(date)
        else:
            date = "0000-00-00"
    
    return returnList
    
            

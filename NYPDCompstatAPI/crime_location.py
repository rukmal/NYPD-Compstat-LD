from . import util

from bs4 import BeautifulSoup


def getCrimeLocation(crime: str, time_horizon: str) -> list:
    # Getting dataset ID
    dataset_id = util.getDatasetID(time_period=time_horizon, map_id=crime)

    # Getting location data
    loc_data = util.makeRequest(request_type='location', dataset_id=dataset_id)

    formatted_data = []

    for crime_loc_raw in loc_data:
        # Dictionary to store formatted crime data
        crime_loc = dict()

        # Coordinates
        coordinates = crime_loc_raw['Value'].split(',')
        crime_loc['latitude'] = float(coordinates[0])
        crime_loc['longitude'] = float(coordinates[1])

        # Metric
        crime_loc['metric'] = int(crime_loc_raw['Metric'])

        # Getting subtype and time raw text
        parsed = BeautifulSoup(crime_loc_raw['Title'], 'html.parser')
        raw_text = parsed.select('.text-left > span')

        # Subtype and type
        crime_loc['type'] = util.cleanLabel(dirty_label=crime)
        crime_loc['subtype'] = util.cleanLabel(dirty_label=raw_text[0].text)

        # Parsing date and time
        parsed_datetime = util.parseDate(raw=raw_text[1].text)        
        crime_loc['date'] = parsed_datetime['date']
        crime_loc['time'] = parsed_datetime['time']

        formatted_data += [crime_loc]

    return formatted_data

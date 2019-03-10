from datetime import datetime


def parseDate(raw: str) -> dict:
    """Function to parse raw datetime string and extract date and time with
    proper formatting.
    
    Arguments:
        raw {str} -- Raw datetime string.
    
    Returns:
        dict -- Formatted date and time.
    """

    # output object
    output = dict()

    # Date and time extraction (raw)
    raw_date = raw[:8]
    raw_time = raw[8:].strip()

    # Date
    date_obj = datetime.strptime(raw_date, '%m/%d/%y')
    output['date'] = date_obj.strftime('%Y-%m-%d ')

    # Time
    time_obj = datetime.strptime(raw_time, '%I%p')
    output['time'] = time_obj.strftime('%H:%M:%S')

    return output

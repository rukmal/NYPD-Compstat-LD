# Mapping of specific crimes
CRIME = {
    'murder': 'Murder',
    'rape': 'Rape',
    'robbery': 'Robbery',
    'felony_assault': 'Fel. Assault',
    'burglary': 'Burglary',
    'grand_larceny': 'Gr. Larceny',
}

# Mapping of apprehension types
APPREHENSION_TYPE = {
    'patrol': 'PSB',
    'transit': 'Transit',
    'housing': 'Housing'
}

# Mapping of arbitrary crime "groups"
CRIME_GROUP = {
    'shooting_victims': 'Sht. Vic.',
    'shooting_incidents': 'Sht. Inc.',
    'rape_1': 'Rape 1',
    'petit_larceny': 'Petit Larceny',
    'misdemeanor_assault': 'Misd. Assault',
    'misdemeanor_sex_crimes': 'Misd. Sex Crimes'
}

# Mapping of time period prefixes
# NOTE: "YTD" here does not actually mean YTD; NYPD's system makes no sense so
#       this means from January 1st to the current date of that year
TIME_PREFIX = {
    'current_wtd': 'WTD',
    'prev_wtd': 'SPLYWTD',
    'current_28d': '28D',
    'prev_28d': 'SPLY28D',
    'current_ytd': 'YTD',
    'prev_ytd': 'SPLYYTD'
}

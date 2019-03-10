from .request_key_map import *

# Arbitrary ID root
ID_ROOT = '_COMPLAINTS_'


def paramCheckWrapper(func):
    def checkParams(time_period, map_id):
        if (time_period not in TIME_PREFIX.keys()) or \
            ((map_id not in CRIME) and \
            (map_id not in APPREHENSION_TYPE) and \
            (map_id not in CRIME_GROUP)):
            raise KeyError('Invalid time_period or crime')
        return func(time_period, map_id)
    return checkParams


# The following functions build IDs for specific datasets to be included in
# requests to the NYPD Compstat REST API.

@paramCheckWrapper
def getDatasetID(time_period: str, map_id: str) -> str:
    return TIME_PREFIX[time_period] + ID_ROOT + CRIME[map_id]


@paramCheckWrapper
def getCrimeGroupID(time_period: str, map_id: str) -> str:
    return TIME_PREFIX[time_period] + ID_ROOT + CRIME_GROUP[map_id]


@paramCheckWrapper
def getApprehensionTypeID(time_period: str, map_id: str) -> str:
    return TIME_PREFIX[time_period] + ID_ROOT + \
        APPREHENSION_TYPE[map_id]


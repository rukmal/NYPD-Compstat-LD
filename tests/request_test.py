from context import NYPDCompstatAPI

# Getting sample ID
dataset_id = NYPDCompstatAPI.util.getDatasetID('prev_ytd', 'grand_larceny')

# Making request
r = NYPDCompstatAPI.util.makeRequest(request_type='precinct',
                                     dataset_id=dataset_id)

print(r)

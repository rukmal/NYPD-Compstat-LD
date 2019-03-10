import NYPDCompstatAPI

from rdflib import Graph, Literal, BNode, URIRef, Namespace
from rdflib.namespace import FOAF, XSD, RDF, RDFS


# Constants
BASE_URL = 'http://htkg.stevens.edu'
BASE = Namespace(BASE_URL)

CRIME_TYPE = Namespace(BASE_URL + '/crime/type#')
CRIME_SUBTYPE = Namespace(BASE_URL + '/crime/subtype#')
CRIME_INSTANCE = Namespace(BASE_URL + '/crime/incident#')

# Binding external namespaces
GEO = Namespace('http://www.w3.org/2003/01/geo/wgs84_pos#')
GEORSS = Namespace('http://www.georss.org/georss/')

# Creating graphs (once per run)
incident_graph = Graph(identifier=CRIME_INSTANCE)
crime_type_graph = Graph(identifier=CRIME_TYPE)

# Binding prefixes to graph for readability
# Incident Graph:
incident_graph.bind('', BASE)
incident_graph.bind('crime_type', CRIME_TYPE)
incident_graph.bind('crime_subtype', CRIME_SUBTYPE)
incident_graph.bind('geo', GEO)
incident_graph.bind('georss', GEORSS)
# Crime Type Graph:
crime_type_graph.bind('', BASE)
crime_type_graph.bind('crime_type', CRIME_TYPE)
crime_type_graph.bind('crime_subtype', CRIME_SUBTYPE)

def saveCrimeLocationToRDF(crime_locs: list):
    for crime in crime_locs:
        # Crime type and subtype label
        subtype = crime['subtype']
        c_type = crime['type']


        # Crime Type graph
        # (crimeType, hasSubtype, crimeSubtype) triple
        crime_type_graph.add((CRIME_SUBTYPE[subtype], RDFS.subClassOf,
                              CRIME_TYPE[c_type]))

        # Incident Graph
        incident = BNode()
        # (incident, hasType, crimeType)
        incident_graph.add((incident, RDF.type, CRIME_TYPE[c_type]))
        # (incident, hasType, crimeSubType)
        incident_graph.add((incident, RDF.type, CRIME_SUBTYPE[subtype]))
        # (incident, hasDate, date)
        incident_graph.add((incident, FOAF.date, Literal(crime['date'],
                                                         datatype=XSD.date)))
        # (incident, hasTime, time)
        incident_graph.add((incident, FOAF.time, Literal(crime['time'],
                                                         datatype=XSD.time)))

        # Geographic coordinates
        point = BNode()
        incident_graph.add((point, RDF.type, GEO.Point))
        incident_graph.add((point, GEO.lat, Literal(
            NYPDCompstatAPI.util.floatToStrWithDecimals(crime['latitude']),
            datatype=XSD.decimal)))
        incident_graph.add((point, GEO.long, Literal(
            NYPDCompstatAPI.util.floatToStrWithDecimals(crime['longitude']),
            datatype=XSD.decimal)))

        # Adding to incident graph
        incident_graph.add((incident, GEORSS.where, point))




if __name__ == '__main__':
    # Iterating through every type of crime, grabbing current_ytd and prev_ytd
    # crime location data for each one
    for period in ['current_ytd', 'prev_ytd']:
        for crime in NYPDCompstatAPI.util.request_key_map.CRIME:
            # Getting dataset ID
            dataset_id = NYPDCompstatAPI.util.getDatasetID(time_period=period,
                                                        map_id=crime)

            # Getting data for given dataset_id
            loc_data = NYPDCompstatAPI.getCrimeLocation(crime=crime,
                                                        time_horizon=period)

            # Saving to RDF
            saveCrimeLocationToRDF(crime_locs=loc_data)

    with open('output/crime_locations.ttl', 'wb') as f:
        f.write(incident_graph.serialize(format='turtle'))

    with open('output/crime_types.ttl', 'wb') as f:
        f.write(crime_type_graph.serialize(format='turtle'))

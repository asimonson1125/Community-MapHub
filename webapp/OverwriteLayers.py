import OverwriteFS

itemId = "59912e15ab83417dad73b4c56463245c"  # Title: 'My Test Service Item'
sourceUrl = "http://localhost:5000/geojson"

# Import ArcGIS Python API and make a connection to Portal
from arcgis.gis import GIS
# gis = GIS(profile='abs1907', username= 'abs1907@rit.edu_RITArcGIS', password= '<pass>')
gis = GIS("https://shibboleth.main.ad.rit.edu")


# Get item from Portal
item = gis.content.get( itemId)

# Initiate update of service
outcome = OverwriteFS.overwriteFeatureService( item, sourceUrl)

# Check results
if outcome["success"]:
    print( "Service Overwrite was a Success!")

elif outcome["success"] == False:
    print( "Service Overwrite Failed!")

    # Show last three steps, for diagnostics
    for step in outcome[ "items"][-3:]:
        print( " - Action: '{}', Result: '{}'".format( step[ "action"], step[ "result"]))

#else: outcome[ "success"] == None, No Change Required!

LOOKUPS = {
"AirConditioning": {
    "C":"Central",
    "F":"Free Standing",
    "M":"Multi­Zone",
    "N":"None",
    "T":"Through the Wall",
    "U":"Unknown Type",
    "W":"Window Units",
},

"Borough": {
    "BK":"Brooklyn",
    "BX":"Bronx",
    "NY":"Manhattan",
    "QN":"Queens",
    "SI":"Staten Island",
},

"BuildingAccess": {
    "A":"Attended Elevator",
    "E":"Elevator",
    "K":"Keyed Elevator",
    "N":"None",
    "W":"Walk­up",
},

"BuildingAge": {
    "O":"Post­war",
    "R":"Pre­war",
},

"BuildingType": {
    "D":"Development Site",
    "F":"Loft",
    "G":"Garage",
    "H":"High­Rise",
    "L":"Low­Rise",
    "M":"Mid­Rise",
    "O":"Hotel",
    "P":"Parking Lot",
    "S":"House",
    "T":"Townhouse",
    "V":"Vacant Lot",
},

"Heat": {
    "B":"Baseboard",
    "C":"Central",
    "E":"Electric",
    "G":"Gas",
    "M":"Multi­Zone",
    "O":"Oil",
    "R":"Radiator",
    "U":"Unknown Type",
},

"LeaseTerm": {
    "1":"One Year",
    "2":"Two Year",
    "3":"Short­term",
    "4":"Month­to­month",
    "5":"Specific term",
    "6":"One or Two year",
    "7":"Short or Long term",
},

"LeaseType": {
    "B":"Stabilized Lease",
    "C":"Commercial",
    "N":"Non­Stabilized Lease",
    "On­Line":"Residential, Inc | IDX API documentation v1.0 | Published 11/01/2014 | Page 27 of 29",
    "S":"Stabilized Sublease",
    "U":"Non­Stabilized Sublease",
},

"ListingStatus": {
    "A":"Active",
    "B":"Board Approved",
    "C":"Contract Signed",
    "E":"Leases Signed",
    "H":"TOM",
    "I":"POM",
    "J":"Exclusive Expired",
    "L":"Leases Out",
    "O":"Contract Out",
    "P":"Offer Accepted/Application",
    "R":"Rented",
    "S":"Sold",
},

"ListingStatusRental": {
    "A":"Active",
    "E":"Leases Signed",
    "H":"TOM",
    "I":"POM",
    "J":"Exclusive Expired",
    "L":"Leases Out",
    "P":"Application",
    "R":"Rented",
},

"ListingStatusSale": {
    "A":"Active",
    "B":"Board Approved",
    "C":"Contract Signed",
    "H":"TOM",
    "I":"POM",
    "J":"Exclusive Expired",
    "O":"Contract Out",
    "P":"Offer Accepted",
    "S":"Sold",
},

"ListingType": {
    "A":"Ours Alone",
    "B":"Exclusive",
    "C":"COF",
    "L":"Limited",
    "O":"Open",
    "Y":"Courtesy",
    "Z":"Buyer's Broker",
},

"MediaType": {
    "F":"Floor plan",
    "I":"Interior Photo",
    "M":"Video",
    "O":"Other",
    "V":"Virtual Tour",
},

"Ownership": {
    "C":"Commercial",
    "D":"Condop",
    "G":"Garage",
    "I":"Income Property",
    "M":"Multi­Family",
    "N":"Condo",
    "P":"Co­op",
    "R":"Rental Property",
    "S":"Single Family",
    "T":"Institutional",
    "V":"Development Site",
    "X":"Mixed Use",
},

"PayPeriod": {
    "M":"Monthly",
    "Y":"Yearly",
},

"PetPolicy": {
    "A":"Pets Allowed",
    "C":"Case By Case",
    "D":"No Dogs",
    "N":"No Pets",
    "T":"No Cats",
},

"SalesOrRent": {
    "R":"Apartment for Rent",
    "S":"Apartment for Sale",
    "T":"Building for Sale",
},

"ServiceLevel": {
    "A":"Attended Lobby",
    "C":"Concierge",
    "F":"Full Time Doorman",
    "I":"Voice Intercom",
    "N":"None",
    "P":"Part Time Doorman",
    "S":"Full Service",
    "U":"Virtual Doorman",
    "V":"Video Intercom",
}
}

def expand_row(row):
    output = {}
    for k, v in row.items():
        if k in LOOKUPS:
            output[k] = LOOKUPS[k].get(v, 'UNKNOWN')
        elif hasattr(v, 'items'):
            output[k] = expand_row(v)
        else:
            output[k] = v
    return output

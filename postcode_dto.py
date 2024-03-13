class Postcode:
    def __init__(self, postcode, country,region, admin_dist, eastings, northings):
        self.postcode = postcode
        self.eastings = eastings
        self.northings = northings
        self.admin_district = admin_dist
        self.country = country
        self.region = region

    def setEastings(self,eastings):
        self.eastings = eastings

    def setNorthings(self,northings):
        self.northings = northings

    def setAdmindistrict(self, admin_district):
        self.admin_district = admin_district

    def setRegion(self, region):
        self.admin_district = region

    def setCountry(self, country):
        self.country = country

    def __repr__(self):
        postcode_str = f"postcode: {self.postcode}, admin_district: {self.admin_district}, region :{self.region},country: {self.country}, eastings: {self.eastings}, northings:{self.northings} "
        return postcode_str
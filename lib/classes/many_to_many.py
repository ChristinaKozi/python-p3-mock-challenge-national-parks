class NationalPark:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not hasattr(self, "_name") and isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise Exception("The name should be a string greater than 3 characters")
        
    def trips(self):
        trips = []
        for trip in Trip.all:
            if trip.national_park == self:
                trips.append(trip)
        return trips
    
    def visitors(self):
        visitors = []
        for trip in Trip.all:
            if trip.national_park == self:
                visitors.append(trip.visitor)
        return list(set(visitors))
    
    def total_visits(self):
        count = 0
        for trip in Trip.all:
            if trip.national_park == self:
                count += 1
        return count
    
    def best_visitor(self):
        visitors = {}
        for trip in Trip.all:
            if trip.national_park == self:
                if trip.visitor in visitors:
                    visitors[trip.visitor] += 1
                else:
                    visitors[trip.visitor] = 1
            
        if visitors:
            max_count = max(visitors.values())
            for visitor, count in visitors.items():
                if count == max_count:
                    return visitor
        return None


class Trip:
    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, start_date):
        if isinstance(start_date, str) and len(start_date) >= 7:
            self._start_date = start_date
        else:
            raise Exception("Invalid start date format or length.")

    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, end_date):
        if isinstance(end_date, str) and len(end_date) >= 7:
            self._end_date = end_date
        else:
            raise Exception("Invalid end date format or length.")

    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor
        else:
            raise Exception("visitor must be an instance of Visitor")
        
    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park



class Visitor:

    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception("The name should be a string between between 1 and 15 characters, inclusive")
        
    def trips(self):
        trips = []
        for trip in Trip.all:
            if trip.visitor == self:
                trips.append(trip)
        return trips
    
    def national_parks(self):
        parks = []
        for trip in Trip.all:
            if trip.visitor == self:
                parks.append(trip.national_park)
        return list(set(parks))
    
    def total_visits_at_park(self, park):
        count = 0
        trips = self.trips()
        for trip in trips:
            if trip.visitor == self and trip.national_park == park:
                count += 1
        return count
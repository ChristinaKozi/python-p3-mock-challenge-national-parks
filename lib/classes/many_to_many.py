class NationalPark:
    all = []

    def __init__(self, name):
        self.name = name

        self._trips = []
        self._visitors = []

        NationalPark.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not hasattr(self, "name") and isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise Exception("The name should be a string greater than 3 characters")
        
    def trips(self):
        return self._trips
    
    def visitors(self):
        return list(set(self._visitors))
    
    def total_visits(self):
        return len(self._trips)
    
    def best_visitor(self):
        if len(self._visitors) == 0:
            return None
        
        return max(self._visitors, key = self._visitors.count)
    
    @classmethod
    def most_visited(cls):
        curr_park = None
        curr_max_visits = 0
        for national_park in cls.all:
            if len(national_park._trips) > curr_max_visits:
                curr_park = national_park
                curr_max_visits = len(national_park._trips)
        return curr_park

class Trip:
    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date

        self.visitor._trips.append(self)
        self.visitor._parks.append(self.national_park)

        self.national_park._trips.append(self)
        self.national_park._visitors.append(self.visitor)

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

        self._trips = []
        self._parks = []    

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
        return self._trips
    
    def national_parks(self):
        return list(set(self._parks))
    
    def total_visits_at_park(self, park):
        return len([trip for trip in self.trips if trip.national_park == park])
        #count = 0
        #for trip in self._trips:
        #    if trip.visitor == self and trip.national_park == park:
        #        count += 1
        #return count
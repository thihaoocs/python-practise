# Original Tank
class Tank(object):
    def get_damage(self):
        pass

    def get_strength(self):
        pass

    def get_upgraded_part(self):
        pass

# Concrete Tank class
class Original_tank(Tank):
    
    def get_damage(self):
        return 100
    
    def get_strength(self):
        return 100

    def get_upgraded_part(self):
        return 'Nothing'

# Tank Decorator
class Tank_Decorator(Tank):

    def __init__(self, decorated_tank):
        self.decorated_tank = decorated_tank

    def get_damage(self):
        return self.decorated_tank.get_damage()

    def get_strength(self):
        return self.decorated_tank.get_strength()
    
    def get_upgraded_part(self):
        return self.decorated_tank.get_upgraded_part()

# Tank wrappers

class ERA(Tank_Decorator):

    def __init__(self, decorated_tank):
        Tank_Decorator.__init__(self,decorated_tank)

    def get_damage(self):
        return self.decorated_tank.get_damage()
    
    def get_strength(self):
        return self.decorated_tank.get_strength() + 20
    
    def get_upgraded_part(self):
        return self.__class__.__name__

class Main_Battery(Tank_Decorator):
    
    def __init__(self, decorated_tank):
        Tank_Decorator.__init__(self, decorated_tank)
    
    def get_damage(self):
        return self.decorated_tank.get_damage() + 35

    def get_strength(self):
        return self.decorated_tank.get_strength()

    def get_upgraded_part(self):
        return self.__class__.__name__
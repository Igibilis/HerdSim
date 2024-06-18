from main_package.Horse import Draught, Pony


class Field:
    """Class for a basic field on the map. Is used as a parent for other field variations.
     Has 2 parameters: position_on_map and grass_Status and only method stat"""
    def __init__(self, position_on_map: int, grass_status: str):
        self.position_on_map = position_on_map
        self.grassStatus = grass_status

    def stat(self):
        """Method used to print out fields parameters, used while testing"""
        print(self.position_on_map, self.grassStatus)

class Obstacle(Field):
    """Class which is a special variation and a child class to Field. Represents an obstacle that could harm
     a horse object. Has one new parameter obs_type and one new method run_in_obstacle"""
    def __init__(self, position_on_map: int, grass_status: str, obs_type: chr):
        super().__init__(position_on_map, grass_status)
        self.obs_type = obs_type

    def run_in_obstacle(self, obj):
        """Method executes consequences if horse objects finds itself on obstacle field"""
        if self.obs_type == "puddle":
            if obj.health <= 95:
               obj.health += 5
        elif self.obs_type == "rock":
            if isinstance(obj, Draught):
                newfield = Field(self.position_on_map, self.grassStatus)
                self.__del__()
            else :
                obj.health -= 10
        elif self.obs_type == "wood":
            if isinstance(obj, Pony):
                pass
            else:
                obj.health -= 10
        elif self.obs_type == "forest":
            obj.health -= 10



    def stat(self):
        """Method used to print out parameters of Obstacle"""
        print(self.position_on_map, self.grassStatus, self.obs_type)

    def __del__(self):
        """Method used to delete an obstacle field"""
        del self

class PredatorField(Field):
    """Child class of Field. Represents a field with predators that can harm a horse object. Checks predator and horses
    stats and according to them takes away health points from horse object."""
    def __init__(self, position_on_map: int, grass_status: str, pred_speed: int, pred_strenght: int):
        super().__init__(position_on_map, grass_status)
        self.pred_speed = pred_speed
        self.pred_strenght = pred_strenght

    def attack(self, obj):
        """Method comparing stats of horse and predator and executing the results"""
        if obj.speed > self.pred_speed:
            if obj.strenght > self.pred_strenght:
                pass
            else:
                obj.health -= 20
        else:
            if obj.strenght < self.pred_strenght:
                obj.health -= 80
            else:
                obj.health -= 40

    def stat(self):
        """Method that prints parameters of predator field"""
        print(self.position_on_map, self.grassStatus)


class PredatorLair(Field):
    """Child class of Field. Represents a field with many predators whom instantly kill a horse_object that would step
    on it"""
    def group_attack(self, obj):
        """Method killing a horse"""
        obj.health -= 100

    def stat(self):
        """Method that prints out parameters of predator lair"""
        print(self.position_on_map, self.grassStatus)

import random
from abc import ABC, abstractmethod

class Horse(ABC):
    """Abstract class presenting a structure for horse objects. Has 6 parameters: gender, age, health, speed, strenght
     and horse_postition. Has basic method like eat, move, death and breed that every horse object can do regardless of
     its specific type"""

    def __init__(self,gender: chr,age: int,health: int,speed: int,strenght: int,horse_position: int):
        self.gender= gender
        self.age = age
        self.health= health
        self.speed=speed
        self.strenght=strenght
        self.horse_position=horse_position
    def move(self,row,column):
        """Method allowing horses to move on the map. It takes into consideration where horse is currently on the map
         and calcualte possible movement options, then randomly chooses one of them and changes given horses horse_position"""

        if self.horse_position % column == 0:
            if self.horse_position <= column:
                movepossible = [self.horse_position-1, self.horse_position+column]
                self.horse_position=random.choice(movepossible)
                self.health-=10
            elif self.horse_position > column * row - column:
                movepossible = [self.horse_position-column, self.horse_position-1]
                self.horse_position = random.choice(movepossible)
                self.health -= 10
            else:
                movepossible = [self.horse_position-column, self.horse_position-1, self.horse_position+column]
                self.horse_position = random.choice(movepossible)
                self.health -= 10
        elif self.horse_position % column == 1:
            if self.horse_position <= column:
                movepossible = [self.horse_position+1, self.horse_position+column ]
                self.horse_position = random.choice(movepossible)
                self.health -= 10
            elif self.horse_position > column * row - column:
                movepossible = [self.horse_position+1, self.horse_position-column]
                self.horse_position = random.choice(movepossible)
                self.health -= 10
            else :
                movepossible = [self.horse_position+1, self.horse_position-column, self.horse_position+column]
                self.horse_position = random.choice(movepossible)
                self.health -= 10
        else :
            if self.horse_position <= column:
                movepossible = [self.horse_position+1, self.horse_position+column, self.horse_position-1]
                self.horse_position = random.choice(movepossible)
                self.health -= 10
            elif self.horse_position > column * row - column:
                movepossible = [self.horse_position+1, self.horse_position-column, self.horse_position-1]
                self.horse_position = random.choice(movepossible)
                self.health -= 10
            else:
                movepossible = [self.horse_position+1, self.horse_position-column, self.horse_position+column, self.horse_position-1]
                self.horse_position = random.choice(movepossible)
                self.health -= 10

    def eat(self, grass):
        """Method that can restore horse objects health, checks grass status on the field where the horse is currently
         and adds health points accordingly"""
        match grass:
            case 'none':
                self.health=self.health
            case 'fresh':
                if self.health!=100:
                    if self.health>90:
                        self.health+=5
                    else :
                        self.health+=10
            case 'old':
                if self.health<=95:
                    self.health+=5

    def breed(self, obj, herd):
        """Method allowing herd to grow bigger, checks interracting horses gender and if they are of the opposite gender,
        adds a new member to the herd"""
        if self.gender == 'male' and obj.gender == 'male':
            print("Couldn't breed")
        elif self.gender == 'female' and obj.gender == 'female':
            print("Couldn't breed")
        elif self.gender == 'male' and obj.gender == 'female' or obj.gender == 'female' and obj.gender == 'male':
            print("Herd got a new member")
            herd.add_member('n', herd.herd_size+1)
            herd.herd_size += 1

    def death(self, herd):
        """Method deleting a horse from the program. Occurs when health has dropped below or is equal to 0."""
        herd.delete_member(self)
        del(self)

class Pony(Horse):
    """Child class of Horse class, presents a specific type of horse - a pony. It inherits everything from Horse class
    and adds 1 new parameter: speed.Modifier and 1 new method: sneak.Obstacle"""
    def __init__(self,gender: chr,age: int,health: int,speed: int,strenght: int,horse_position: int, speed_Modifier: int):
        super().__init__(gender, age, health, speed, strenght, horse_position)
        self.speed_Modifier= speed_Modifier

    def sneak_obstacle(self, obs_type, field):
        """Method allowing pony object to not lose health points when on obstacle field. Only some obstacles can be
        avioded"""
        if obs_type == 'forset' or obs_type == 'wood':
            pass
        else:
            field.run_in_obstacle(self)

    def stats(self):
        """Method printing out basic parameters of pony"""
        print("Gender:" + str(self.gender), " Age:" + str(self.age), " Health:" + str(self.health),
              " Speed:" + str(self.speed), "Strenght:" + str(self.strenght), " Position:" + str(self.horse_position))

class Normal(Horse):
    """Child class of Horse class, presents a specific type of horse - a normal horse. It inherits everything from Horse class
        adds 1 new method: run"""
    def run(self):
        """Method allowing normal horse to move one more time during a day"""
        self.move()

    def stats(self):
        """Method printing out parameters of normal horse"""
        print("Gender:"+ str(self.gender)," Age:"+str(self.age)," Health:"+str(self.health)," Speed:"+str(self.speed),"Strenght:"+str(self.strenght)," Position:"+str(self.horse_position))

class Draught(Horse):
    """Child class of Horse class, presents a specific type of horse - a draught. It inherits everything from Horse class
        and adds 1 new parameter: strenght.Modifier and 1 new method: move.Obstacle"""
    def __init__(self,gender: chr,age: int,health: int,speed: int,strenght: int,horse_position: int, strenght_Modifier: int):
        super().__init__(gender, age, health, speed, strenght, horse_position)
        self.strenght_Modifier=strenght_Modifier

    def move_obstacle(self, obs_type, field):
        """Method allowing draught horse to delete an obstacle from a field it's currently positioned on. Only certain
         types of obstacles can be removed"""
        if obs_type == 'rock' or obs_type == 'wood':
            new = 'new_field' + str(field.position_on_map)
            new = Field(field.position_on_map, field.grassStatus)
            field.__del__()
        else:
            field.run_in_obstacle(self)

    def stats(self):
        """Method printing parameters of draught horse"""
        print("Gender:"+ str(self.gender)," Age:"+str(self.age)," Health:"+str(self.health)," Speed:"+str(self.speed),"Strenght:"+str(self.strenght)," Position:"+str(self.horse_position))
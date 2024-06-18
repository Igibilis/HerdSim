from main_package.Field import Field, Obstacle, PredatorField, PredatorLair
import random
from math import floor


class Map:
    """Class responsible for creating a map. Creates list of fields and also possesses a method that prints the map"""
    def __init__(self, row: int, columns: int, num_of_fields: int, mapp: [int], climate: str):
        self.row = row
        self.columns = columns
        self.num_of_fields = num_of_fields
        self.mapp = mapp
        self.climate = climate

    def get_fields(self):
        """Method generating fields. Generation is fully randomized. Require a map class already existing"""
        for i in range(1, self.num_of_fields+1):
            options = ['f', 'o', 'p', 'pl']
            grass = ['none', 'fresh', 'old']
            match random.choice(options):
                case 'f':
                    name = str('f')+str(i)
                    name = Field(i, random.choice(grass))
                    self.mapp.append(name)
                    # name.stat()  # tymczasowo
                case 'o':
                    obtype = ['puddle', 'rock', 'wood', 'forest']
                    name = str('o') + str(i)
                    name = Obstacle(i, random.choice(grass), random.choice(obtype))
                    self.mapp.append(name)
                    # name.stat()  # tymczasowo
                case 'p':
                    name = str('p') + str(i)
                    name = PredatorField(i, random.choice(grass), random.randint(30, 100),
                                         random.randint(30, 100))
                    self.mapp.append(name)
                    # name.stat()  # tymczasowo
                case 'pl':
                    name = str('pl') + str(i)
                    name = PredatorLair(i, random.choice(grass))
                    self.mapp.append(name)
                    # name.stat()  # tymczasowo

    def print_map(self, herdm):
        """Method printing map, matching horses positions and field types with a "square" representing a field of
         fitting number."""
        map_to_print = []
        for i in range(self.columns*2+self.columns+1):
            map_to_print.append("0")
        mtp = []
        for i in range(self.row*2+self.row+1):
            mtp.append(list(map_to_print))
        mtp[0][0] = "a"
        for i in range(self.row*2+self.row+1):
            mtp[i][0] = "|"
            for j in range(self.columns*2+self.columns+1):
                if j % 3 == 0:
                    mtp[i][j] = "|"
                if i % 3 == 0:
                    mtp[i][j] = "-"
        for o in range(len(herdm)):
            if herdm[o].horse_position <= self.columns:
                mtp[2][2+(3*(herdm[o].horse_position-1))] = 'h'
            elif herdm[o].horse_position > self.columns and herdm[o].horse_position % self.columns != 0:
                mtp[2+3*round((herdm[o].horse_position-(herdm[o].horse_position % self.columns))/self.columns)][2+(3*(herdm[o].horse_position-(self.columns*floor(herdm[o].horse_position/self.columns))-1))] = 'h'
            else:
                mtp[2+3*round((herdm[o].horse_position-(herdm[o].horse_position % self.columns))/self.columns)-3][2+3*(self.columns-1)] = 'h'
        for x in range(self.num_of_fields+1):
            match type(self.mapp[x]).__name__:
                case 'Field':
                    if self.mapp[x].position_on_map <= self.columns:
                        mtp[1][1 + (3 * (self.mapp[x].position_on_map - 1))] = 'f'
                    elif self.mapp[x].position_on_map > self.columns and self.mapp[x].position_on_map % self.columns != 0:
                        mtp[1 + 3 * round(
                            (self.mapp[x].position_on_map - (self.mapp[x].position_on_map % self.columns)) / self.columns)][2 + (
                                    3 * (self.mapp[x].position_on_map - (
                                        self.columns * floor(self.mapp[x].position_on_map / self.columns)) - 1))] = 'f'
                    else:
                        mtp[1 + 3 * round(
                            (self.mapp[x].position_on_map - (self.mapp[x].position_on_map % self.columns)) / self.columns) - 3][
                            1 + 3 * (self.columns - 1)] = 'f'
                case 'Obstacle':
                    if self.mapp[x].position_on_map <= self.columns:
                        mtp[1][1 + (3 * (self.mapp[x].position_on_map - 1))] = 'o'
                    elif self.mapp[x].position_on_map > self.columns and self.mapp[x].position_on_map % self.columns != 0:
                        mtp[1+3*round((self.mapp[x].position_on_map-(self.mapp[x].position_on_map % self.columns)) / self.columns)][1+(3 * (self.mapp[x].position_on_map-(self.columns * floor(self.mapp[x].position_on_map / self.columns)) - 1))] = 'o'
                    else:
                        mtp[1 + 3 * round(
                            (self.mapp[x].position_on_map - (
                              self.mapp[x].position_on_map % self.columns))/self.columns)-3][1+3*(self.columns-1)] = 'o'
                case 'PredatorField':
                    if self.mapp[x].position_on_map <= self.columns:
                        mtp[1][1 + (3 * (self.mapp[x].position_on_map - 1))] = 'p'
                    elif self.mapp[x].position_on_map > self.columns and self.mapp[
                        x].position_on_map % self.columns != 0:
                        mtp[1 + 3 * round((self.mapp[x].position_on_map-(self.mapp[x].position_on_map % self.columns)) /
                                          self.columns)][1+(3 * (self.mapp[x].position_on_map-(self.columns
                                            * floor(self.mapp[x].position_on_map / self.columns)) - 1))] = 'p'
                    else:
                        mtp[1 + 3 * round(
                            (self.mapp[x].position_on_map - (
                                        self.mapp[x].position_on_map % self.columns)) / self.columns) - 3][
                            1 + 3 * (self.columns - 1)] = 'p'
                case 'PredatorLair':
                    if self.mapp[x].position_on_map <= self.columns:
                        mtp[1][1 + (3 * (self.mapp[x].position_on_map - 1))] = 'l'
                    elif self.mapp[x].position_on_map > self.columns and self.mapp[x].position_on_map % self.columns != 0:
                        mtp[1 + 3 * round((self.mapp[x].position_on_map - (self.mapp[x].position_on_map % self.columns)) / self.columns)][1+(3 * (self.mapp[x].position_on_map - (self.columns * floor(self.mapp[x].position_on_map / self.columns)) - 1))] = 'l'
                    else:
                        mtp[1 + 3 * round(
                           (self.mapp[x].position_on_map - (self.mapp[x].position_on_map % self.columns
                                                            )) / self.columns) - 3][1 + 3 * (self.columns - 1)] = 'l'

        for i in mtp:
            print(*i)

from main_package.Herd import Herd
from main_package.Map import Map


class Base:
    """ Class that collects parameters and handles the whole simulation """
    def __init__(self):
        self.duration = int

    def get_parameters(self):
        """ Method responsible for gathering parameters from file input by user, also checks if given parameters are
        correct and if file exist. After making sure inputs are correct generates map fields by calling other classes
        methods and horses objects by calling other classes methods"""

        __p = 'p'
        __n = 'n'
        __d = 'd'
        while True:
            try:
                file = str(input('Enter file name: '))
                open(file, 'r')
            except FileNotFoundError:
                print('File not found.')
            except AssertionError:
                print('Please enter a valid file name.')
            else:
                break
        with open(file, 'r') as f:
            self.duration = int(f.readline())
            i = int(f.readline())
            if i > 14:
                print("Zbyt duże stado, program nie wyrabia")
                quit()
            herd1 = Herd(i)
            while True:
                try:
                    pnum = int(f.readline())
                except ValueError:
                    print("Proszę wprowadzić liczbe int")
                    quit()
                if pnum > herd1.herd_size:
                    print("Ilość przekracza liczbe koni w stadzie")
                    quit()
                else:
                    herd1.add_member(__p, pnum)
                    break
            while True:
                try:
                    nnum = int(f.readline())
                except ValueError:
                    print("Proszę wprowadzić liczbe int")
                    quit()
                if nnum + pnum > herd1.herd_size:
                    print("Ilość przekracza liczbe koni w stadzie")
                    quit()
                else:
                    herd1.add_member(__n, nnum)
                    break
            while True:
                try:
                    dnum = int(f.readline())
                except ValueError:
                    print("Proszę wprowadzić liczbe int")
                    quit()
                if dnum + nnum + pnum > herd1.herd_size:
                    print("Ilość przekracza liczbe koni w stadzie")
                    quit()
                elif dnum + nnum + pnum != herd1.herd_size:
                    print("Poszczególne typy koni nie sumują się do deklarowanej wielkości stada")
                    quit()
                else:
                    herd1.add_member(__d, dnum)
                    break
            while True:
                try:
                    clim = str(f.readline())
                finally:
                    pass
                if clim == "warm\n" or clim == "cold\n" or clim == "tropical\n":
                    break
                else:
                    print("Proszę wprowadzić jedną z podanych opcji: warm,cold,tropical")
                    quit()
            while True:
                try:
                    row = int(f.readline())
                    column = int(f.readline())
                except ValueError:
                    print("Proszę wprowadzić liczbe int")
                    quit()
                if herd1.herd_size * 2 >= row * column:
                    print("Za duże stado jak na taką mape")
                    quit()
                else:
                    map1 = Map(row, column, row * column, [row * column], clim)
                    map1.get_fields()
                    break
        f.close()
        herd1.set_starting_position(map1.num_of_fields)
        return [row, column, map1, herd1]

    def run_simulation(self, listo):
        """ Method that runs the whole simulation, using parameters and objects gathered in function get_parameters.
         Moves horses around the map and handles events related with map fields and interactions between horses.
         Prints out the map and horses statuses. After simulation ends, writes information about every herd member
         well-being and size of herd at the end, summing up the simulation in a file called end.txt"""
        match listo[2].climate:
            case 'warm\n':
                for u in range(0, listo[3].herd_size-1):
                    match type(listo[3].herd_members[u]).__name__:
                        case 'Pony':
                            listo[3].herd_members[u].speed -= 10
                            listo[3].herd_members[u].strenght += 10
                        case 'Normal':
                            listo[3].herd_members[u].speed += 10
                            listo[3].herd_members[u].strenght += 10
                        case 'Draught':
                            listo[3].herd_members[u].speed += 10
                            listo[3].herd_members[u].strenght -= 10
            case 'cold\n':
                for u in range(0, listo[3].herd_size - 1):
                    match type(listo[3].herd_members[u]).__name__:
                        case 'Pony':
                            listo[3].herd_members[u].speed += 10
                            listo[3].herd_members[u].strenght += 10
                        case 'Normal':
                            listo[3].herd_members[u].speed -= 10
                            listo[3].herd_members[u].strenght -= 10
                        case 'Draught':
                            listo[3].herd_members[u].speed += 10
                            listo[3].herd_members[u].strenght += 10
            case 'tropical\n':
                for u in range(0, listo[3].herd_size - 1):
                    match type(listo[3].herd_members[u]).__name__:
                        case 'Pony':
                            listo[3].herd_members[u].speed -= 10
                            listo[3].herd_members[u].strenght -= 10
                        case 'Normal':
                            listo[3].herd_members[u].speed += 20
                            listo[3].herd_members[u].strenght += 20
                        case 'Draught':
                            listo[3].herd_members[u].speed -= 20
                            listo[3].herd_members[u].strenght -= 20
        for i in range(1, self.duration+1):
            print("Horses status, day:" + str(i))
            j = 0
            while j < len(listo[3].herd_members):
                is_alive = True
                listo[3].herd_members[j].eat(listo[2].mapp[listo[3].herd_members[j].horse_position].grassStatus)
                match type(listo[2].mapp[listo[3].herd_members[j].horse_position]).__name__:
                    case 'Obstacle':
                        if type(listo[3].herd_members[j]).__name__ == 'Pony':
                            listo[3].herd_members[j].sneak_obstacle(
                                listo[2].mapp[listo[3].herd_members[j].horse_position].obs_type,
                                listo[2].mapp[listo[3].herd_members[j].horse_position])
                        elif type(listo[3].herd_members[j].horse_position).__name__ == 'Draught':
                            listo[3].herd_members[j].move_obstacle(listo[2].mapp[listo[3].herd_members[j].horse_position].obs_type, listo[2].mapp[listo[3].herd_members[j].horse_position])
                        else:
                            listo[2].mapp[listo[3].herd_members[j].horse_position].run_in_obstacle(listo[3].herd_members[j])
                    case 'PredatorField':
                        listo[2].mapp[listo[3].herd_members[j].horse_position].attack(listo[3].herd_members[j])
                    case 'PredatorLair':
                        listo[2].mapp[listo[3].herd_members[j].horse_position].group_attack(listo[3].herd_members[j])
                    case 'Field':
                        pass
                if listo[3].herd_members[j].health <= 0 or listo[3].herd_members[j].age == 30:
                    print(str(type(listo[3].herd_members[j]).__name__) + " is dead")
                    listo[3].herd_members[j].death(listo[3])
                    is_alive = False
                    j -= 1
                for o in range(0, listo[3].herd_size-1):
                    if j != i:
                        if listo[3].herd_members[j].horse_position == listo[3].herd_members[o].horse_position and listo[3].herd_members[j].health >= 50 and listo[3].herd_members[o].health >= 50 and listo[3].herd_members[o].age >= 3 and listo[3].herd_members[j].age >= 3:
                            listo[3].herd_members[j].breed(listo[3].herd_members[o], listo[3])
                if not is_alive:
                    pass
                else:
                    if i % 4 == 0:
                        listo[3].herd_members[j].age += 1
                    listo[3].herd_members[j].move(listo[0], listo[1])
                    listo[3].herd_members[j].stats()
                if len(listo[3].herd_members) == 0:
                    break
                j += 1
            if len(listo[3].herd_members) == 0:
                break
            listo[2].print_map(listo[3].herd_members)
            input()
        plik = open('end.txt', 'w')
        for i in range(0, len(listo[3].herd_members)):
            if listo[3].herd_members[i].health >= 80:
                plik.write(str(type(listo[3].herd_members[i]).__name__)+" is in great condition \n")
            elif 50 >= listo[3].herd_members[i].health < 80:
                plik.write(str(type(listo[3].herd_members[i]).__name__)+" is doing fine \n")
            elif 0 < listo[3].herd_members[i].health < 50:
                plik.write(str(type(listo[3].herd_members[i]).__name__)+" is badly injured \n")
        plik.write(str(listo[3].herd_size)+" horses live in this herd \n")


b1 = Base()
b1.run_simulation(b1.get_parameters())

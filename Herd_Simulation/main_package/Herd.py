import random
from main_package.Horse import Pony, Normal, Draught


class Herd:
    """Class responsible for creating a list of horse objects, and setting them a starting position on the map."""

    def __init__(self, herd_size: int):
        self.herd_size = herd_size
        self.herd_members = []

    def set_starting_position(self, numfields):
        """Picks a starting position for a horse in herd. Only 2 horses can start from the same field"""
        for i in range(0, self.herd_size):
            check = 0
            while True:
                self.herd_members[i].horse_position = random.randint(1, numfields)
                for j in range(0, self.herd_size):
                    if self.herd_members[i].horse_position == self.herd_members[j].horse_position:
                        check += 1
                if check > 2:
                    continue
                if check <= 2:
                    break

    def stats(self):
        print(self.herd_members)

    def add_member(self, typ: chr, num):
        """Method responsible for adding a member to the herd. Creates a horse object and appends it to the herd list.
        Every horse object is randomly generated,except for their type which is chosen by the user"""
        gender = ['m', 'f']
        match typ:
            case 'p':
                for j in range(1, num+1):
                    name = typ+str(j)
                    # print(name)
                    name = Pony(random.choice(gender), random.randint(1, 25), 100, random.randint(1, 100),
                                random.randint(1, 100), 0, random.randint(1, 10))
                    self.herd_members.append(name)
                    name.speed = round(name.speed / name.speed_Modifier)
                    # name.stats()
            case 'n':
                for j in range(1, num + 1):
                    name = typ + str(j)
                    # print(name)
                    name = Normal(random.choice(gender), random.randint(1, 25), 100,
                                  random.randint(1, 100), random.randint(1, 100), 0)
                    self.herd_members.append(name)
                    # name.stats()
            case 'd':
                for j in range(1, num + 1):
                    name = typ + str(j)
                    # print(name)
                    name = Draught(random.choice(gender), random.randint(1, 25), 100,
                                   random.randint(1, 100), random.randint(1, 100),
                                   0, random.randint(1, 10))
                    self.herd_members.append(name)
                    name.strenght = round(name.strenght + 5 * name.strenght_Modifier)
                    # name.stats()

    def delete_member(self, h):
        """Method that deletes a horse from the herd, so it is no longer on the herd list"""
        for index, x in enumerate(self.herd_members):
            if x == h:
                objindex = index

        del (self.herd_members[objindex])
        self.herd_size -= 1

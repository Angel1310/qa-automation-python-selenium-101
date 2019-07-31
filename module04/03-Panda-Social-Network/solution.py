class Panda():

    def __init__(self, name, email, gender):
        self.nameP = name
        self.emailP = email
        if gender == 'male':
            self.genderP = True
        else:
            self.genderP = False

    def name(self):
        return self.nameP

    def email(self):
        return self.emailP

    def gender(self):
        if self.genderP:
            return 'male'
        else:
            return 'female'

    def isMale(self):
        return self.genderP

    def isFemale(self):
        return not self.genderP

    def __str__(self):
        return self.nameP + self.emailP + self.genderP

    def __hash__(self):
        return hash((self.nameP, self.emailP, self.genderP))

    def __eq__(self, other):
        return hash(self) == hash(other)


class PandaSocialNetwork():
    def __init__(self):
        self.pandas = []
        self.counted_friends = dict()

    def add_panda(self, panda):
        if self.has_panda(panda):
            raise PandaAlreadyThere
        self.pandas.append(panda)
        self.counted_friends[panda] = []

    def make_friends(self, panda1, panda2):
        if self.has_panda(panda1) is False:
            self.add_panda(panda1)
        if self.has_panda(panda2) is False:
            self.add_panda(panda2)
        if self.are_friends(panda1, panda2):
            raise PandasAlreadyFriends

        else:
            self.counted_friends.get(panda1).append(panda2);
            self.counted_friends.get(panda2).append(panda1);

    def are_friends(self, panda1, panda2):
        return panda2 in self.counted_friends.get(panda1)

    def friends_of(self, panda):
        if self.has_panda(panda):
            return self.counted_friends.get(panda)
        else:
            return False

    def has_panda(self, panda_to_add):
        for panda in self.pandas:
            if panda.__eq__(panda_to_add):
                return True
        return False

    def connection_level(self, panda1, panda2):

        if self.has_panda(panda1) is False:
            return False
        if self.has_panda(panda2) is False:
            return False
        if self.are_friends(panda1, panda2):
            return 1

class Panda(object):

    def __init__(self,name,email,gender):
        self._name=name
        self._email=email
        self._gender=gender

    def name(self):
        return self._name
    def email(self):
        return self._email
    def gender(self):
        return self._gender
    def isMale(self):
        male=('male')
        if self._gender==male:
            return True
        else:
            return False
    def isFemale(self):
        female=('female')
        if self._gender==female:
            return True
        else:
            return False


    def __hash__(self):
        return hash(self._name and self._email and self._gender)
    def __eq__(self, other):
        return (
                self._gender == other._gender and
                self._name==other._name and
                self._email==other._email )

class PandaSocialNetwork(object):
    pass
            













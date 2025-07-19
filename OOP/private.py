#private variables

class private:
    __cat="Whiskers"

    def name(self):
        print(self.__cat)


class Pets(private):
    def show_pet(self):
        print("the pet is :",self.__cat)




if __name__=="__main__":
    obj1=private()
    obj1.name()
    obj2=Pets()
    obj2.show_pet()

import pickle
import os.path

class Human():
    def __init__(self, weight=0, height=0):
        self.Weight = weight
        self.Height = height


    def __eq__(self,other):
        return (self.height, self.weight) == (other.height, other.weight)


    def __hash__(self):
        return hash(self.height)+hash(self.weight)


class Deputat(Human):
    def __init__(self, surname=None, name=None, weight=None, height=None, date_of_birth=None, corupted =None):
        # instance dict fields should be edited here
        self.Surname = surname
        self.Name = name
        super().__init__(weight, height)
        self.Date_of_birth = date_of_birth
        self.Corupted = corupted
        self.__bribe_size__ = 0
        for element in self.__dict__:
            if element[0] != "_":
                print("Change value for the deputy: {}, current value is {} (Press Return to skip)".format(element, self.__dict__[element]))
                inp = input("")
                if inp != '':
                    self.__dict__[element] = inp

    def change_deputy_state(self):
        for element in self.__dict__:
            if element[0] != "_":
                print("Change value for the deputy: {}, current value is {} (Press Return to skip)".format(element, self.__dict__[element]))
                inp = input("")
                if inp != '':
                    self.__dict__[element] = inp


    def __eq__(self,other):
        return (self.Surname,self.Name)== (other.Surname,other.Name)


    def __hash__(self):
        return hash(self.Surname)+hash(self.Name)

    def  give_tribute(self):
        if self.corupted == False:
            print ("He takes no bribes")
            return
        input("Enter bribe amount: ")
        if tribute_amount >= 10000:
            print("Міліція ув’язнить депутата")
        else:
            self.bribe_size += tribute_amount

class Fraction():
    def __init__(self, name=None):
        self.name = name
        if self.name == None:
            self.name = input("Input fraction name: ")
        self.members = list()
        self.current_deputy = None

    def add_deputy(self):
        new_deputat = Deputat(None,None,None,None,None)
        if new_deputat not in self.members:
            self.members.append(new_deputat)
        if self.current_deputy !=None:
            self.current_deputy = new_deputat

    def print_deputy_list(self):
        for element in self.members:
            print(element.__dict__["Surname"])

    def remove_deputy(self):
        surname = input("Enter the surname of the deputy to be removed from fraction {}: ".format(self.name))
        for element in self. members:
            if element["Surname"] == surname:
                self.members.remove(element)
                print("Deputy {} had been removed from the fraction".format(surname))

    def __save_fraction_to_file__(self):
        with open(self.name + ".data", "bw") as filehandler:
            pickle.dump(self.members, filehandler)

    def __load_fraction_from_file__(self):
        with open(self.name + ".data", "br") as filehandler:
            self.members = pickle.load(filehandler)

class Sorter():
    def __init__(self,value="sorted"):
        self.value = value
    def __call__(self, fraction):
        if self.value == "corupted":
            print("Corupted in {} are: ".format(fraction.name))
            for element in fraction.members:
                if elementp["Corupted"] == True:
                    print(element["Name"] + " " + element["Surname"])
        elif self.value == "top_corupted":
            top_coruptor = None
            for element in fraction.members:
                if top_coruptor == None:
                    if elementp["Corupted"] == True:
                        if top_coruptor == None:
                            top_coruptor = element
                        if element["__bribe_size__"] >= top_coruptor["__bribe_size__"]:
                            top_coruptor = element
            print("Top coruptor in fraction {} is: ".format(fraction.name))
            print(top_coruptor["Name"] + " " + top_coruptor["Surname"])
        elif self.value == "sorted":
            fraction.members.sort(key=lambda x: x[0])
            print(fraction.members)




class VerkhovnaRada:
    def __init__(self):
        self.members = dict()
        self.current_fraction = None

    def add_fraction(self,fraction=None):
        # print("add_fraction executed")
        fraction = Fraction()
        self.members[fraction.name] = fraction
        print("Fraction {} added".format(fraction.name))
        if self.current_fraction == None:
            self.current_fraction = fraction.name

    def remove_fraction(self, name=None):
        # print("remove_fraction executed")
        if name == None:
            choise = input("would you like to remove the current fraction?(Y/N): " )
            if choise == "Y" or choise =="y":
                name = self.current_fraction
                self.current_fraction =None
            elif choise == "N" or choise =="n":
                name = input("enter the name of the fraction to be removed: ")
            else:
                print("incorect input")
                return
        if self.members.pop(name,None) == None:
            print("Such fraction does not exist")
            input("Press enter")
        else:
            print("Done")
            input("Press enter")

    def clear_fraction(self, name=None):
        if name == None:
            choise = input("would you like to clear e the current fraction?(Y/N): " )
            if choise == "Y" or choise =="y":
                name = self.current_fraction
            elif choise == "N" or choise =="n":
                name = input("enter the name of the fraction to be cleared: ")
            else:
                print("incorect input")
                return
        if self.members.get(name) == None:
            print("Such fraction does not exist")
            input("Press enter")
        else:
            self.members[name].members = []
            print("Done")
            input("Press enter")

    def print_fractions(self):
        for element in self.members:
            print(element)
        input("Avalible fractions have been printed. Press enter")

    def save_rada_to_file(self):
        with open("rada.data", "bw") as filehandler:
            pickle.dump(self.members, filehandler)

    def change_current_fraction(self):
        print("Change the curent fraction {} to one of thees:".format(self.clear_fraction()))
        self.print_fractions()
        name = input("Enter fraction name")
        if name != self.members:
            print("Invalid Input")
        else:
            self.current_fraction = name

    def load_rada_from_file(self):
        with open("rada.data", "br") as filehandler:
            self.members = pickle.load(filehandler)
        self.current_fraction = random.choise(list(self.members.items()))







# vava = Fraction("dsodu")
# vava.load_fraction_from_file()
# print(vava.members)
# # for i in range(3):
# #     vava.add_deputy()
# for member in vava.members:
#     print(member.Surname)
# # vava.save_fraction_to_file()


if __name__ == "__main__":
    rada = VerkhovnaRada()
    if os.path.isfile("rada.data"):
        rada.load_rada_from_file()
    while True:
        print("""
Введіть 1, щоб додати фракцію
Введіть 2, щоб видалити фракцію
Введіть 3, щоб очистити фракцію
Введіть 4, щоб вивести фракції
Введіть 5, to change the current fraction
Введіть 6, щоб додати депутата у фракцію
Введіть 7, to change the current deputy
Введіть 8, щоб вивести список хабарників у фракції
Введіть 9, щоб вивести список  хабарників у раді
Введіть 10, щоб вивести найбільшого хабарника у раді
Введіть 11, щоб вивести найбільшого хабарника у фракції.
Введіть 12, щоб перевірити чи є дупутат у фракції
Введіть 13, щоб перевірити чи є депутат у раді
Введіть 14, щоб дати хабаря депутату.
Введіть 0, щоб вийти із програми.
Current fraction is {}""".format(rada.current_fraction))
        if rada.current_fraction != None:
            print("Current deputy is {}".format(rada.members[rada.current_fraction].current_deputy))
        try:
            choise = int(input())
            if choise not in range(15):
                print("Incorect input")
                continue
        except:
            print("Incorect input")
            continue
        if choise == 1:
            rada.add_fraction()
        elif choise == 2:
            rada.remove_fraction()
        elif choise == 3:
            rada.clear_fraction()
        elif choise == 4:
            rada.print_fractions()
        elif choise == 5:
            rada.change_current_fraction()
        elif choise == 6:
            rada.members[rada.current_fraction].add_deputy
        # elif choise == 7:







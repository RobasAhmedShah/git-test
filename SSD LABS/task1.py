from abc import ABC,abstractmethod

class Building(ABC):
    @abstractmethod
    def build(self):
        return None 
    
class Home(Building):
    def build(self):
        print("Home is Built")

class House(Building):
    def build(self):
        print("House is Built")

class Hut(Building):
    def build(self):
        print("Hut is Built")



class BuildingFactory(Home,House,Hut):
    def getbuilding(self):
        choice=input("home/house/hut: ")
        if choice =="home":
            return Home()


build=BuildingFactory()
instance=build.getbuilding()
instance.build()



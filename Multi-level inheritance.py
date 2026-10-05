#Without Constructor — Camera + GPS → Smartphone
class Camera:
    def take_photo(self):
        print("Taking photo")
class GPS(Camera):
    def find_location(self):
        print("Finding Location")
class Smartphone(GPS):
    def make_call(self):
        print("Making Phone call")
s=Smartphone()
s.take_photo()
s.find_location()
s.make_call()

# With Constructor — Engine + Battery → HybridCar
print("---------car details----------")
class Engine:
    def __init__(self):
        print("Engine")
    def petrol_mode(self):
        print("Petrol engine running")
class Battery(Engine):
    def __init__(self):
        print("Battery")
    def electric_mode(self):
        print("Electric battery running")
class HybridCar(Battery):
    def __init__(self):
        print("hybrid car")
h=HybridCar()
h.petrol_mode()
h.electric_mode()

# With Constructor + super() — Chef + Manager → RestaurantOwner
print("---------Restaurant details----------")
class Chef:
    def __init__(self,name):
        self.name=name
    def cook(self):
        print("Chef Name",self.name)
        print("Chef is Preparing food")
class Manager(Chef):
    def __init__(self,name,experience):
        super().__init__(name)
        self.experience=experience
    def manager(self):
        print("Manger Experience=",self.experience)
        print("Manager is managing the restaurant")
class RestaurantOwner(Manager):
    def __init__(self,name,experience,restaurant):
        super().__init__(name,experience)
        self.restaurant=restaurant
    def display(self):
        self.cook()
        self.manager()
        print("Restaurant Name=",self.restaurant)
        
r=RestaurantOwner("Ram","5 years","Spice Garden")
r.display()
#--------------------------------------------------------------------------
print("-----FashionCreator Details--------")
class Photographer:
    def __init__(self,camera):
        self.camera=camera
    def takePhoto(self):
        print("Camera=",self.camera)
class Desingner(Photographer):
    def __init__(self,camera,design):
        super().__init__(camera)
        self.design=design
    def createDesign(self):
        print("Design=",self.design)
class FashionCreator(Desingner):
    def __init__(self,camera,design,name):
        super().__init__(camera,design)
        self.name=name
    def displayDetails(self):
        print("creator Name=",self.name)
        self.createDesign()
        self.takePhoto()
f=FashionCreator("Canon Camera","Traditional Dress","Shylusha")
f.displayDetails()


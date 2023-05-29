class ParkingSystem(object):

    def __init__(self, big, medium, small):
        # Arguments entered represent the amount of slots available for that type
        self.b = big
        self.m = medium 
        self.s = small
      

    def addCar(self, carType):
        # Check if car has an available slots, and update accordingly as slots are filled
        if carType == 1 and self.b >=1:
            self.b = self.b - 1
            return True

        elif carType == 2 and self.m >= 1:
            self.m = self.m - 1
            return True

        elif carType == 3 and self.s >=1:
            self.s = self.s - 1 
            return True
        
        else:
            return False

            

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
    


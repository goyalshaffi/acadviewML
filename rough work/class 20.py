class Car:
    def __init__(self):
        #self.__updatesoftware()
        pass
    def drive(self):
        print('driving')
    def __updateSoftware__(self):
        print'updating software'
redcar=Car()
redcar.drive()
#redcar.updateSoftware() as it is private fun
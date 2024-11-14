#10-2 PROGRAMMING EXERCISE
#WRITE A CLASS NAMED CAR THAT HAS THE FOLLOWING ATTRIBUTES:
#__year_model (for the car's year model), __make(for the make of the car), __speed(for the car's current speed)
#THE CLASS SHOULD HAVE AN __init__ method THAT ACCEPTS THE CAR'S YEAR MODEL AS ARGUMENTS.
#THESE VALUES SHOULD BE ASSIGNED TO THE OBJECTS:
#__year_model and __make DATA ATTRIBUTES. IT SHOULD ALSO ASSIGN 0 TO __speed data attribute
#SHOULD HAVE THE FOLLOWING METHODS:
#ACCELERATE: ACCELERATE METHOD SHOULD ADD 5 TO SPEED DATA ATTRIBUTE EACH TIME IT IS CALLED
#BRAKE: BRAKE METHOD SHOULD SUBTRACT 5 FROM SPEED DATA ATTRIBUTE EACH TIME IT IS CALLED
#get_speed : get_speed METHOD SHOULD RETURN THE CURRENT SPEED
#NEXT DESIGN A PROGRAM THAT CREATES A CAR OBJECT THEN CALLS THE ACCELERATE METHOD 5 TIMES
#AFTER EACH CALL TO THE ACCLERATE METHOD, GET THE CURRENT SPEED OF THE CAR AND DISPLAY IT.
#THEN CALL BRAKE METHOD FIVE TIMES. AFTER EACH CALL TO BRAKE METHOD,
#GET THE CURRENT SPEED OF THE CAR AND DISPLAY IT

#CREATE A CLASS NAMED CAR
class Car:
      def __init__(self, year_model, make):#METHOD THAT ACCEPTS THE CAR'S YEAR MODEL AND MAKE AS ARGUMENTS
            self.__year_model= year_model
            self.__make = make
            self.__speed = 0#ASSIGN 0 TO THE SPEED DATA ATTRIBUTE
      #METHODS TO GET CAR ATTRIBUTES(MUTATOR)
      def get_year_model(self):
            return self.__year_model
      def get_make(self):
            return self.__make
      
      #METHOD TO INCREASE THE CAR'S SPEED BY 5(ACCELERATE)
      def accelerate(self):
            self.__speed += 5
      #METHOD TO SUBTRACT 5 FROM THE SPEED DATA(BRAKE)
      def brake(self):
            if self.__speed >= 5:
                  self.__speed -= 5
            else:
                  self.__speed = 0
      def get_speed(self):
            return self.__speed
#DESIGN PROGRAM THAT DEMONSTRATES CAR CLASS
def main ():
      year_model = input("PLEASE ENTER YEAR MODEL OF CAR: ")
      make = input("PLEASE ENTER THE MAKE OF THE CAR: ")
      
      user_car = Car(year_model,make)

      #ACCELERATE/BRAKING
      for i in range(1, 6):#ACCELERATE 5 TIMES
            user_car.accelerate()
            print (f"ACCLERATION SPEED {i}: {user_car.get_speed()} mph")
      for i in range (1, 6): #BRAKE 5 TIMES
            user_car.brake()
            print(f"SPEED AFTER BRAKE:{i}: {user_car.get_speed()}")
#RUN
main()

      

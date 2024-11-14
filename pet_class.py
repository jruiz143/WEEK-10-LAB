#10-1 PROGRAMMING EXERCISE
#WRITE A CLASS NAMED PET, WHICH SHOULD HAVE THE FOLLOWING DATA ATTRIBUTES
#__name(for the name of a pet)
#__animal_type (for the type of animal that a pet it. Example values are 'Dog', 'Cat', and 'Bird')
#__age (for the pet's age)
#THE PET CLASS SHOULD HAVE AN __INIT__METHOD THAT CREATES THESE ATTRIBUTES.
#IT SHOULD ALSO HAVE THE FOLLOWING METHODS:
#set_name (This methods assigns a value to the __name field).
#set_animal_type (This method assigns a value to the _animal_type field)
#set_age (This method assigns a value to the _age field)
#get_name, get_animal_type, get_age
#WRITE A PROGRAM THAT CREATES AN ONJECT OF THE CLASS AND PROMPTS THE USER
#TO ENTER THE NAME, TYPE, AND AGE OF HIS OR HER PET
#USE THE OBJECT'S ACCESSOR METHODS TO RETRIEVE THE PERT'S NAME, TYPE, AND AGE AND DISPLAY THIS DATA

#WRITE A CLASS NAMED PET
class Pet:
      def __init__(self, name, animal_type, age):#__INIT__ METHOD THAT CREATES ATTRIBUTES
            self.__name = name
            self.__animal_type = animal_type
            self.__age = age
      #MUTATOR(SETTERS)
      def set_name(self, name):
            self._name = name
      def set__animal_type(self, animal_type):
            self._animal_type = animal_type
      def set__age(self, age):
            self._age = age
      #ASSESOR METHOD(RETRIEVE VALUE OF ATTRIBUTES OR GETTERS)
      def get_name(self):
            return self.__name
      def get_animal_type(self):
            return self.__animal_type
      def get_age(self):
            return self.__age
#WRITE A PROGRAM THAT CREATES AN OBJECT OF THE CLASS AND PROMPTS USER FOR INPUT
def main():
      name = input("PLEASE ENTER YOUR PET'S NAME: ")
      animal_type = input("PLEASE ENTER THE ANIMAL TYPE: ")
      age = input("PLEASE ENTER YOUR PET'S AGE: ")

      user_pet = Pet(name, animal_type, age)

      #DISPLAY USER DATA
      print("PET'S INFORMATION IS DISPLAYED BELOW")
      print("PET NAME:", user_pet.get_name())
      print("PET TYPE:", user_pet.get_animal_type())
      print ("PET AGE:", user_pet.get_age())
#RUN THE MAIN FUNCTION
main()
     






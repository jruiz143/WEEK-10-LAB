#10-3 PROGRAMMING EXERCISE:
#DESIGN A CLASS THAT HOLDS THE FOLLOWING PERSONAL DATA:
#NAME, ADDRESS, AGE, AND PHONENUMBER. WRITE APPROPIATE ACCESSOR AND MUTATOR METHODS.
#ALSO, WRITE A PROGRAM THAT CREATES THREE INSTANCES OF THE CLASS.
#EACH INSTANCE SHOULD HOLD FICTIONAL INFO FOR A FAKE NAME

#DESIGN A PERSONAL DATA CLASS
class personal_data:
      def __init__(self, name, address, age, phone_number):
            self.__name= name
            self.__address = address
            self.__age = age
            self.__phone_number = phone_number
      #WRITE ACCESSOR METHODS(GETTERS)
      def get_name(self):
            return self.__name
      def get_address(self):
            return self.__address
      def get_age(self):
            return self.__age
      def get_phone_number(self):
            return self.__phone_number
      
#PROGRAM THAT CREATES 3 INSTANCES OF THE CLASS
def main():
     person_one = personal_data("BOB BURGER", "123 CANDY CANE LANE", 65,"999-876-2222")
     person_two = personal_data("MARGE SIMPSON", "742 EVERGREEN TERRACE", 36,"888-888-888")
     person_three = personal_data("PAUL HOLLYWOOD", "BRITISH LAND AVENUE", 54,"123-456-789")
     #DISPLAY INFORMATION
     print(f"PERSON'S NAME: {person_one.get_name()}, ADDRESS: {person_one.get_address()}, AGE: {person_one.get_age()} PHONE #: {person_one.get_phone_number()}.")
     print(f"PERSON'S NAME: {person_two.get_name()}, ADDRESS: {person_two.get_address()}, AGE: {person_two.get_age()} PHONE #: {person_two.get_phone_number()}.")
     print(f"PERSON'S NAME: {person_three.get_name()}, ADDRESS: {person_three.get_address()}, AGE: {person_three.get_age()} PHONE #: {person_three.get_phone_number()}.")
main()#RUN

     
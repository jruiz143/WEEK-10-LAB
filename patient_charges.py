#10-6 PROGRAMMING EXERCISE
#WRITE A CLASS NAME PATIENT THAT HAS ATTRIBUTES FOR THE FOLLOWING:
#FIRST NAME, MIDDLE NAME, AND LAST NAME
#ADDRESS, CITY, STATE, AND ZIP CODE
#PHONE NUMBER
#NAME AND PHONE NUMBER OF EMERGENCY CONTACT
#THE PATIENT'S CLASS'S __INIT__METHOD SHOULD ACCEPT AN ARGUMENT
#FOR EACH ATTRIBUTE. THE PATIENT CLASS SHOULD ALSO HAVE AN ACCESSOR AND
#MUTATOR FOR EACH ATTRIBUTE

#WRITE A CLASS NAME PATIENT
class Patient:
      def __init__(self, first_name, middle_name, last_name, address, city, state, zip_code, phone_number, emergency_contact_name, emergency_contact_phone):
        #INTIALIZE ATTRIBUTES
            self.__first_name = first_name
            self.__middle_name = middle_name
            self.__last_name = last_name
            self.__address = address
            self.__city = city
            self.__state = state
            self.__zip_code = zip_code
            self.__phone_number = phone_number
            self.__emergency_contact_name = emergency_contact_name
            self.__emergency_contact_phone = emergency_contact_phone
      #ACCESOR METHODS
      def get_first_name(self):
        return self.__first_name
      def get_middle_name(self):
        return self.__middle_name

      def get_last_name(self):
        return self.__last_name

      def get_address(self):
        return self.__address

      def get_city(self):
        return self.__city

      def get_state(self):
        return self.__state

      def get_zip_code(self):
        return self.__zip_code

      def get_phone_number(self):
        return self.__phone_number

      def get_emergency_contact_name(self):
        return self.__emergency_contact_name

      def get_emergency_contact_phone(self):
        return self.__emergency_contact_phone

      #MUTATOR METHODS
      def set_first_name(self, first_name):
        self.__first_name = first_name

      def set_middle_name(self, middle_name):
        self.__middle_name = middle_name

      def set_last_name(self, last_name):
        self.__last_name = last_name

      def set_address(self, address):
        self.__address = address

      def set_city(self, city):
        self.__city = city

      def set_state(self, state):
        self.__state = state

      def set_zip_code(self, zip_code):
        self.__zip_code = zip_code

      def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

      def set_emergency_contact_name(self, emergency_contact_name):
        self.__emergency_contact_name = emergency_contact_name

      def set_emergency_contact_phone(self, emergency_contact_phone):
        self.__emergency_contact_phone = emergency_contact_phone
#WRITE A PROGRAM THAT CREATES AN INSTANCE OF THE PATIENT CLASS, INTIALIZED WITH SAMPLE DATE
#THE CREATE THREE INSTANCES OF THE PROCEDURE CLASS INTIALIZED WITH THE FOLLOWING DATA:

#WRITE PROCEDURE CLASS
class Procedure:
    def __init__(self, name, date, practitioner, charge):
        #INTIALIZE ATTRIBUTES
        self.__name = name
        self.__date = date
        self.__practitioner = practitioner
        self.__charge = charge

    #ACCESSOR METHODS
    def get_name(self):
        return self.__name

    def get_date(self):
        return self.__date

    def get_practitioner(self):
        return self.__practitioner

    def get_charge(self):
        return self.__charge

    # SET METHODS (MUTATORS)
    def set_name(self, name):
        self.__name = name

    def set_date(self, date):
        self.__date = date

    def set_practitioner(self, practitioner):
        self.__practitioner = practitioner

    def set_charge(self, charge):
        self.__charge = charge
# PROGRAM THAT CREATES AN INSTANCE OF THE PATIENT CLASS
def main():
    # INSTANCE OF PATIENT CLASS
    patient1 = Patient("HOMER", "J", "SIMPSON", 
        "742", "Springfield", "IL", "95555", 
        "888-8880", "NED FLANDERS", "666-6660")

    # TODAY'S DATE
    today_date = "NOVEMBER 13TH, 2024"

    #THREE INSTANCES OF PROCEDURE CLASS
    procedure_one = Procedure("Physical Exam", today_date, "Dr. Irvine", 250.00)
    procedure_two = Procedure("X-ray", today_date, "Dr. Jamison", 500.00)
    procedure_three = Procedure("Blood Test", today_date, "Dr. Smith", 200.00)

    # DISPLAY PATIENT
    print(f"Patient Name: {patient1.get_first_name()} {patient1.get_middle_name()} {patient1.get_last_name()}")
    print(f"Address: {patient1.get_address()}, {patient1.get_city()}, {patient1.get_state()} {patient1.get_zip_code()}")
    print(f"Phone Number: {patient1.get_phone_number()}")
    print(f"Emergency Contact: {patient1.get_emergency_contact_name()} - {patient1.get_emergency_contact_phone()}")

    # DISPLAY PROCEDURES
    print("\nPROCEDURES:")
    print(f"PROCEDURE #1: {procedure_one.get_name()}\nDATE: {procedure_one.get_date()}\nPRACTITIONER: {procedure_one.get_practitioner()}\nCHARGE: ${procedure_one.get_charge():,.2f}")
    print(f"PROCEDURE #2: {procedure_two.get_name()},\nDATE: {procedure_two.get_date()}\nPRACTITIONER: {procedure_two.get_practitioner()}\nChARGE: ${procedure_two.get_charge():,.2f}")
    print(f"PROCEDURE #3: {procedure_three.get_name()},\nDATE: {procedure_three.get_date()}\nPRACTITIONER: {procedure_three.get_practitioner()}\nCHARGE: ${procedure_three.get_charge():,.2f}")


# RUN
main()
  
      
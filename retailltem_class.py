#10-5PROGRAMMING EXERCISE
#WRITE A CLASS NAME RETAILLTEM THAT HOLDS DATA ABOUT AN ITEM IN A RETAIL STORE
#THE CLASS SHOULD STORE THE FOLLOWING DATA IN ATTRIBUTES:
#ITEM DESCRITPTION, UNITS IN INVENTORY, AND PRICE

#ONCE YOU HAVE WRITTEN THE CLASS, WRITE A PROGRAM THAT CREATES THREE
#RETAILITEM OBJECTS AND STORES THE FOLLOWING DATA
#ITEM #1: DESCRIPTION: JACKET, UNITS: 12, PRICE: 59.95 
#ITEM #2: DESCRIPTION: DESIGNER JEANS, UNITS: 40, PRICE: 34.95 
#ITEM #3: DESCRIPTION: SHIRT, UNITS: 20, PRICE: 24.95 
#WRITE A CLASS NAME RETAILLTEM 
class RetailItem:
      def __init__(self,description,units,price):
            #INITIALIZE ATTRIBUTES
            self.__description = description
            self.__units = units
            self.__price = price
      #MUTATOR METHOD(SET)
      def set_description(self, description):
            self.__description = description
      def set_units(self,units):
            self.__units = units
      def set_price(self, price):
            self.__price = price
      #ASSESOR(GET)
      def get_description(self):
            return self.__description
      def get_units(self):
            return self.__units
      def get_price(self):
            return self.__price
      #__str__ METHOD THAT RETURNS THE OBJECTS STATE AS A STRING
      def __str__(self):
            return f'ITEM DESCRIPTION: {self.__description}\n' + \
                   f'UNITS IN INVENTORY: {self.__units}\n' + \
                   f'UNIT PRICE: ${self.__price}'
#WRITE A PROGRAM THAT CREATES THREE RETAILITEM OBJECTS
def main():
      item_one = RetailItem("Jacket", 12, 59.95)
      item_two = RetailItem("Designer Jeans", 40, 34.95)
      item_three = RetailItem("Shirt", 20, 24.95)
      #DISPLAY INFO FOR INSTANCES
      print(f"ITEM #1:\n{item_one}")
      print(f"ITEM #2:\n{item_two}")
      print(f"ITEM #3:\n{item_three}")
#RUN
main()

      


            


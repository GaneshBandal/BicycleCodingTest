import sqlite3

class PricingEngine:
  def __init__(self):
    input_file = open('input.txt')
    self.component = []
    for each in input_file:
        self.component.append(each.strip())
    print("we have:"+str(self.component))

  def menu(self):
      print("Welcome TO Pricing Engine")
      print("1. Generate Pricing")
      print("2. Add New Part")
      print("3. Add New Component")
      print("4. Exit")
      userInput = input("Enter Your Choice:")
      return int(userInput)

  def operation(self, input):
      if(input == 1):
          self.display();
          exit()
      elif(input == 2):
          print("Input Action")
          exit()
      elif(input==3):
          print("Please Provide Information for Component")
          self.addComponent()
          exit()
      else:
          exit()

  def addComponent(self):
      compName = input("Enter Component Name:")
      compPrice = input("Component Price")
      input_file = open('pricing.txt', 'a+')
      input_file.write("\n" + compName + "," + compPrice)


  def display(self):
      print("Calculating Price")
      pricing_file = open('pricing.txt')
      input_file = open('input.txt')
      total = 0
      for component in input_file:
          componentName = component.strip()
          for componentPrice in pricing_file:
              if(componentName == componentPrice.split(',')[0]):
                  total += int(componentPrice.split(',')[1])
                  break
      print("Total Price of Given Component Combination:"+str(total))



s1 = PricingEngine()

while(True):
    choice = s1.menu()
    s1.operation(choice)

# print("User Entered:"+s1.menu())

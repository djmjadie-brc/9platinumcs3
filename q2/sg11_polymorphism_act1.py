# created the parent class called "Patient"
class Patient:
  def __init__(self, name, bill_amount):
    self.__name = name
    self.__bill_amount = bill_amount

  def get_name(self):  # getter method for the name of the patient
    return self.__name

  def set_name(self, name):  # allows you to set the name of the patient
    self.__name = name

  def get_bill_amount(self):  # getter method for the bill amount
    return self.__bill_amount

  def set_bill_amount(self, bill_amount):  # allows you to set the bill amount of the patient
    self.__bill_amount = bill_amount

  def calculate_bill(self):  # calculates the full bill of a patient w or w/o a discount
    return self.__bill_amount

  def display_patient_type(self):  # displays the type of patient
    print("Patient Type: Regular Patient")

# created a child class called "Senior Patient"
class Senior_Patient(Patient):
  def calculate_bill(self):  # overrides the calculate_bill on the parent class and added a 20% discount 
    return self.get_bill_amount() * 0.8

  def display_patient_type(self):  # overrides the display_patient_type and show a new patient type
    print("Patient Type: Senior Citizen")

# created another child class called "PhilHealth Patient"
class PhilHealth_Patient(Patient):
  def calculate_bill(self):  # also overrides the calculate_bill method and added a 15% discount instead
    return self.get_bill_amount() * 0.85

  def display_patient_type(self):  # also overrides the display_patient_type and shows a new patient type
    print("Patient Type: PhilHealth Patient")

# creating the objects for each class
regular = Patient("Juan Dela Cruz", 15000)
senior = Senior_Patient("Maria Santos", 15000)
philhealth = PhilHealth_Patient("Pedro Reyes", 15000)

# displays the information of all patients with the name, original bill, final bill, and patient type
print("Hospital Billing System")
print("-----------------------")

print(f"Patient Name: {(regular.get_name())}")
print(f"Original Bill: {(regular.calculate_bill()):,.2f}")
(regular.display_patient_type())
print(f"Final Bill: {(regular.calculate_bill()):,.2f}")

print(" ")
print(f"Patient Name: {(senior.get_name())}")
print(f"Original Bill: {(senior.get_bill_amount()):,.2f}")
(senior.display_patient_type())
print(f"Final Bill: {(senior.calculate_bill()):,.2f}")

print(" ")
print(f"Patient Name: {(philhealth.get_name())}")
print(f"Original Bill: {(philhealth.get_bill_amount()):,.2f}")
(philhealth.display_patient_type())
print(f"Final Bill: {(philhealth.calculate_bill()):,.2f}")   

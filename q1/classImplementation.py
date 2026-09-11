class Typhoon:
    def __init__(self, name, signal_number, max_windspeed, isin_PAR):
        self.name = name
        self.signal_number = signal_number
        self.__max_windspeed = max_windspeed
        self.__isin_PAR = isin_PAR

    def create_summary(self):
        print(f"Typhoon Name: {self.name}")
        print(f"Signal Number: {self.signal_number}")
        print(f"Maximum Wind Speed: {self.__max_windspeed} km/h")
        print(f"Is in PAR: {self.__isin_PAR}")

    def update_signalnumber(self, new_signalnumber):
        self.signal_number = new_signalnumber

    def give_currentlocation(self):
        if self.__isin_PAR:
            print(f"{self.name} is in the Philippine Area of Responsibility (PAR).")
        else:
            print(f"{self.name} is outside the Philippine Area of Responsibility (PAR).")


typhoon1 = Typhoon("Typhoon Yolanda (Haiyan)", 5, 315, True)
typhoon2 = Typhoon("Typhoon Pepito (Man-yi)", 5, 260, False)

print("--- BEFORE ---")
print("Typhoon 1:")
typhoon1.create_summary()
print(" ")
print("Typhoon 2:")
typhoon2.create_summary()

print(" ")
print("Updating signal number on Typhoon 1...")
typhoon1.update_signalnumber(4)
print(" ")

print("--- AFTER ---")
print("Typhoon 1: (Changed)")
typhoon1.create_summary()
print(" ")
print("Typhoon 2: (Unchanged)")
typhoon2.create_summary()

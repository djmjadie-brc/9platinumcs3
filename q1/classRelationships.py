class Typhoon:
    def __init__(self, name, signal_number, max_windspeed, isin_PAR):
        self.name = name
        self.signal_number = signal_number
        self.__max_windspeed = max_windspeed
        self.__isin_PAR = isin_PAR
        
        self.bulletins = []
    def add_bulletin(self, bulletin):
        self.bulletins.append(bulletin)


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
    

class CycloneBulletin:
    def __init__(self, bulletinNumber, windSignal, category, potentialImpacts):
        self.bulletinNumber = bulletinNumber
        self.windSignal = windSignal
        self.__category = category
        self.__potentialImpacts = potentialImpacts

    def bulletinSummary(self):
        print("Cyclone Bulletin:")
        print(f"Bulletin Number: {self.bulletinNumber}")
        print(f"Wind Signal: {self.windSignal}")
        print(f"Category: {self.__category}")
        print(f"Potential Impacts: {self.__potentialImpacts}")

    def showWarning(self):
        if self.windSignal == 5:
            print("Warning: Extremely strong wind signal, evacuate immediately and seek shelter!")
        elif self.windSignal == 4:
            print("Warning: Very strong wind signal, stay indoors and avoid travel, evacuate if needed!")
        elif self.windSignal == 3:
            print("Warning: Strong wind signal, secure loose objects and stay indoors!")
        elif self.windSignal == 2:
            print("Warning: Moderate wind signal, stay alert and monitor updates!")
        else:
            print("No immediate warning, stay alert for updates!")


print("--- BEFORE RELATIONSHIP ---")

typhoon1 = Typhoon("Typhoon Yolanda (Haiyan)", 5, 315, True)
cyclone_bulletin1 = CycloneBulletin(1, 5, "Super Typhoon", "Extreme threat to life and property.")
cyclone_bulletin2 = CycloneBulletin(2, 4, "Typhoon", "Significant to severe threat to life and property.")
cyclone_bulletin3 = CycloneBulletin(3, 3, "Severe Tropical Storm", "Moderate to significant threat to life and property.")

print(f"Independent typhoon: {typhoon1.name}")
print(f"Independent bulletins: #{cyclone_bulletin1.bulletinNumber}, #{cyclone_bulletin2.bulletinNumber}, #{cyclone_bulletin3.bulletinNumber}")
print(" ")

print("--- BUILDING RELATIONSHIP ---")

typhoon1.add_bulletin(cyclone_bulletin1)
typhoon1.add_bulletin(cyclone_bulletin2)
typhoon1.add_bulletin(cyclone_bulletin3)

print(f"typhoon1.add_bulletin(cyclone_bulletin1), typhoon1.add_bulletin(cyclone_bulletin2), typhoon1.add_bulletin(cyclone_bulletin3)")
print(" ")

print("--- AFTER RELATIONSHIP ---")
typhoon1.create_summary()
print(" ")

print("--- Related object(s): ---")
for bulletin in typhoon1.bulletins:
    bulletin.bulletinSummary()

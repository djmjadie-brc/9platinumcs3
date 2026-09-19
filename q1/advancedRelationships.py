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

class WarningData:
    def __init__(self, windSignal, evacuationRequired, emergencyProcedures=None):
        self.windSignal = windSignal
        self.evacuationRequired = evacuationRequired
        self.emergencyProcedures = emergencyProcedures

class CycloneWarningBulletin(CycloneBulletin):
    def __init__(self, bulletinNumber, windSignal, evacuationRequired, emergencyProcedures):
        super().__init__(bulletinNumber, windSignal, category=None, potentialImpacts=None)
        self.evacuationRequired = evacuationRequired
        self.emergencyProcedures = emergencyProcedures
        self.alert_data = WarningData(windSignal, evacuationRequired, emergencyProcedures)

    def bulletinSummary(self):
        print("Cyclone Warning Bulletin:")
        print(f"Bulletin Number: {self.bulletinNumber}")
        print(f"Evacuation Required: {self.evacuationRequired}")
        print(f"Emergency Procedures: {self.emergencyProcedures}")

    def impactedRegions(self, regions):
        print("Impacted Regions:")
        for region in regions:
            print(f"- {region}")

print("Test 1 — Inheritance")
print(" ")

CycloneWarningBulletin1 = CycloneWarningBulletin(bulletinNumber=1, windSignal=5, evacuationRequired=True, emergencyProcedures="Evacuate to nearest shelter.")
WarningData1 = WarningData(windSignal=5, evacuationRequired=True)

print("Parent attributes:")
print(f"wind signal = {CycloneWarningBulletin1.windSignal}")
print(f"evacuation required = {CycloneWarningBulletin1.evacuationRequired}")

print("Child object:")
print("WarningData1")
print(f"wind signal = {WarningData1.windSignal}")
print(f"evacuation required = {WarningData1.evacuationRequired}")
print(" ")

print("Test 2 — Composition/Aggregation")
print(" ")
print("CycloneWarningBulletin1 contains WarningData1:")
print(f"wind signal = {CycloneWarningBulletin1.alert_data.windSignal}")
print(f"evacuation required = {CycloneWarningBulletin1.alert_data.evacuationRequired}")
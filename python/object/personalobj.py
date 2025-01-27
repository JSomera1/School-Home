#warframe
class arsenal:

    def __init__(self, name, primary, secondary, melee, companion):
        self.name = name
        self.primary = primary
        self.secondary = secondary
        self.melee = melee
        self.companion = companion

    def show_arsenal(self):
        print("I don't know what to say")

    def change_warframe(self, name):
        self.name = name
    
        
class loadout(arsenal):

    def __init__(self, name, primary, secondary, melee, companion, nechramech):
        #super needs to be called in the __init__ function 
        super().__init__(name, primary, secondary, melee, companion)
        self.nechramech = nechramech

    def show_arsenal(self):
        print(f"Name:{self.name}, Primary:{self.primary}, Secondary:{self.secondary}, Melee:{self.melee}, Companion:{self.companion}, nechramech:{self.nechramech}")

    
    def show_nechramech(self):
        print(self.nechramech)

l1 = loadout('Gauss Prime', 'Acceltra Prime', 'Akarius Prime', 'Innodem', 'Carrier Prime' ,'')

l1.show_arsenal()

l1.change_warframe('Ember')
l1.show_arsenal()

l2 = loadout('Qorvex', 'braton', 'lex', 'kronen', 'dethcube', 'nech')
l2.show_arsenal()
class pet:
    def __init__(self, name, happiness = 0, hunger = 0):
        self.name = name
        self.happiness = happiness
        self.hunger = hunger

    def __repr__(self):
        return 'Your pet: \n Pet name is ' + self.name + '\n and they are ' + str(self.happiness) + ' out of 10 happy,\n and ' + str(self.hunger) + ' out of 10 hungry.'
    
    def feed(self):
        if self.hunger == 0:
            self.hunger += 0
        else:
            self.hunger -= 1
        
    def play(self):
        if self.happiness == 10:
            self.happiness += 0
        else:
            self.happiness += 1

all_pets = ['Josh', 5, 3, 'Dom', 8, 1, 'Ines', 6, 3]

def start_game():
    print(' ' + '1. ' + all_pets[0],'\n','2. ' + all_pets[3],'\n','3. ' + all_pets[6] )
    pet_choice = int(input('Pick you pet to interact with!'))
    if pet_choice == 1:
        print('you picked Josh!')
    elif pet_choice == 2:
        print('you picked Dom!')
    elif pet_choice == 3:
        print('you picked Ines')


def create_new():
    create_or_play = int(input('1. Create new\n2. Use existing\n'))
    if create_or_play == 2:
        start_game()
    elif create_or_play == 1:
        new_name = input('Enter new pet name: ')
        new_happy = int(input('Enter happy level: '))
        if new_happy > 10:
            while new_happy > 10:
                print('Your value is too high must be between 1-10')
                new_happy = int(input('Enter happy level: '))               
        new_hunger = int(input('Enter hunger level: '))
        if new_hunger > 10:
            while new_hunger > 10:
                print('Your value is too high must be between 1-10')
                new_hunger = int(input('Enter hunger level: '))
        new_pet = pet(new_name, new_happy, new_hunger)
        print(new_pet)
        feed = int(input('Do you want to feed your pet?     0=no/1=yes'))
        if feed == 1:
            new_pet.feed()
        elif feed == 0:
            pass
        else:
            while feed != 0 and feed != 1:
                print('You must enter 0 or 1.')
                feed = int(input('Do you want to feed your pet?     0=no/1=yes'))
        play = int(input('Do you want to play your pet?     0=no/1=yes'))
        if play == 1:
            new_pet.play()
        elif play == 0:
            pass
        else:
            while play != 0 and play != 1:
                print('You must enter 0 or 1.')
                play = int(input('Do you want to play your pet?     0=no/1=yes'))
        print(new_pet)
        all_pets.append(new_pet)
        
create_new()

from item import Item, button

class Player:
    def __init__(self):
        self.inventory = []
    def show_item(self):
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("")

        if len(self.inventory) == 0:
            print("If you don't pick things up, do props grow out of the bag on their own?")
        index = 1
        for i in self.inventory:
            print(index,end = ". ")
            print(i.the_type)
            i.check()
            index += 1
        
        print("")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

    


    
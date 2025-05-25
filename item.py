class Item:
    def __init__(self, the_type:str, description:str,able_grab:bool):
        self.the_type = the_type
        self.description = description
        self.able_grab = able_grab

    def check(self):
        print(self.description)
    
        
class table(Item):
    def __init__(self):
        super().__init__('Table', 'An old table, covered in dust, and on closer inspection there appeared to be a drawer with perhaps something in it?',False)
        self.storage = []

    def grab_item(self,grab_item:Item):
        if grab_item in self.storage:
            if grab_item.able_grab == True:
                self.storage.remove(grab_item)
    
    def add_item(self,the_item:Item):
        self.storage.append(the_item)
    
    def show_items(self):
        index = 1
        for i in self.storage:
            print(index,end = ". ")
            print(i.the_type)
            i.check()
            index += 1


class key(Item):
    def __init__(self, influence,colour:str,position):
        super().__init__(f'{colour}_key', f"A {colour} key that seems to be used to open a certain lock...",True)
        self.influence = influence
        self.colour = colour
        self.position = position
    
    def use(self,current):
        if current == self.position:
            self.influence.unlock()
            print(f"You use the key on the door to {self.influence.name}, the door opens, push on till the tasks end....")
        else: 
            print("You cant use the key here....")

class button(Item):
    def __init__(self,influence:Item):
        super().__init__('button', 'A button. What happens when you push it? I don\'t know...', False)
        self.is_pressed = False
        self.influence = influence
    
    def interact(self):
        if self.is_pressed == True:
            print("The button has been pressed, and pressing it again has no effect...")
        else:
            print("You press the button, and there's a loud bang from within the maze, as if something has been triggered...")
            self.influence.unlock()


class code_lock(Item):
    def __init__(self,code:int,influence):
        super().__init__('code_lock', 'It\'s a four-digit combination lock. Look for clues to open this lock. Or try them slowly one by one, provided you have enough patience...', False)
        self.code = code
        self.locked = True
        self.influence = influence
    
    def interact(self):
        if not self.locked:
            print("🔓 The lock is already unlocked.")
        else:
            attempt = input("🔐 Enter the 4-digit code: ").strip()
            if attempt == self.code:
                self.locked = False
                self.influence.unlock()
                print("Correct code! The lock clicks open.")
            else:
                print("Wrong code. The lock remains locked.")

class note(Item):
    def __init__(self,number:int,description):
        super().__init__(f'note_{number}', description, True)

class balls_basket(Item):
    def __init__(self,description):
        super().__init__('balls_basket', description, False)


    

    
    


        



from item import Item

class Room:
    def __init__(self,the_name:str,the_description:str):
        self.name = the_name
        self.description = the_description
        self.N = None
        self.S = None
        self.W = None
        self.E = None
        self.locked = False
        self.storage = []

    def read_description(self):
        print(self.description)
    
    def set_connection(self,connect,direction:str):
        match direction.upper():
            case 'N':
                self.N = connect
                connect.S = self
            
            case 'S':
                self.S = connect
                connect.N = self
            
            case 'E':
                self.E = connect
                connect.W = self
            
            case 'W':
                self.W = connect
                connect.E = self
    
    def get_connection(self,target):
        if self.N == target:
            return 'N'
        elif self.E == target:
            return 'E'
        elif self.W == target:
            return 'W'
        elif self.S == target:
            return 'S'
        else:
            return None
        
    def lock_room(self):
        self.locked = True
    
    def unlock(self):
        self.locked = False
    
    def add_item(self,the_item:Item):
        self.storage.append(the_item)

    def show_items(self):
        index = 1
        for i in self.storage:
            print(index,end = ". ")
            print(i.the_type)
            i.check()
            index += 1

class destination_room(Room):
    def __init__(self):
        super().__init__("Exit", "You've reached the final room. The door creaks open...")

        
    
    
            

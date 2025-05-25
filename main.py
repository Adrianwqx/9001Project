from map import create_first_map, show_map
from player import Player
from item import table,  button,Item
from rooms import Room,destination_room

def main():
    first_level_map=create_first_map()
    player = Player()

    print()
    print("Welcome to Escape Maze!")
    print("Type 'help' to see available commands.\n")
    print()

    play_level(first_level_map,[2,4],player)

def play_level(map_data:list, start_position:list,player:Player):

    current_room = map_data[start_position[0]][start_position[1]]
    print(show_map(current_room,map_data))
    print()

    while True:
        command = input("Enter your command: ").strip().lower()

        # moving senarios
        direction_map = {
        'w': ('N', 'North'),
        's': ('S', 'South'),
        'a': ('W', 'West'),
        'd': ('E', 'East'),
        }

        match command:
            case cmd if cmd in direction_map:
                dir_attr, dir_name = direction_map[cmd]
                next_room = getattr(current_room, dir_attr)

                if next_room:
                    if getattr(next_room, "locked", False):
                        print("🔒 The room is locked! You can't go there yet.")
                    else:
                        print(f"You walk slowly towards the {dir_name}...")
                        current_room = next_room
                        current_room.read_description()
                        print(show_map(current_room, map_data))
                        print()
                else:
                    print("You head for the wall... BANG!!! You hit the wall! What were you doing! DUDE!")

            case 'map':
                print(show_map(current_room, map_data))
                print()

            case 'look':
                print()
                current_room.read_description()
                print()

            case 'bag':
                player.show_item()
                
            case cmd if cmd.startswith('search'):
                parts = cmd.split()
                if len(parts) != 2:
                    print("Wrong format. Use: search <container> or search room")
                    continue

                target = parts[1].lower()

                if target == 'room':
                    if len(current_room.storage) == 0:
                        print("You searched and found nothing directly in the room.")
                    else:
                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
                        current_room.show_items()
                        print()
                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
                else:
                    item_found = False
                    for i in current_room.storage:
                        print (i.the_type.lower())
                        if target == i.the_type.lower():
                            item_found = True
                            try:
                                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
                                i.show_items()
                                print()
                                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
                            except AttributeError:
                                print(f"{target} doesn't have any places to hide items...")
                            continue
                    if item_found == False:
                        print(f"There is no {target} in the room...")

            case cmd if cmd.startswith('grab'):
                parts = cmd.split()
                if len(parts) != 3:
                    print("Wrong format Dude! Corret format is this：grab <container> <item>")
                    continue
                
                _, container_name, item_name = parts
                item_name = item_name.lower()
                container_name = container_name.lower()

                if container_name == 'room':
                    if len(current_room.storage) == 0:
                                print(f"The room is empty....")
                    for obj in current_room.storage:
                        if obj.the_type.lower() == item_name and obj.able_grab:
                            current_room.storage.remove(obj)
                            player.inventory.append(obj)
                            print(f"You picked up the {item_name} in the room")
                            continue
                        elif obj.able_grab == False:
                            print(f"{item_name} can not be picked up")
                        else:
                            print(f"There is no {item_name} in the room...")
                else:
                    for obj in current_room.storage:
                        if obj.the_type.lower() == container_name and hasattr(obj, 'storage'):
                            if len(obj.storage) == 0:
                                print(f"{container_name} is empty....")
                            for inner_item in obj.storage:
                                if inner_item.the_type.lower() == item_name and inner_item.able_grab:
                                    obj.storage.remove(inner_item)
                                    player.inventory.append(inner_item)
                                    print(f"You picked up {item_name} from {container_name}")
                                    continue
                                else:
                                    print(f"There is no {item_name} in the {container_name} ")
                                    continue
                        else:
                            print(f"We cant find {container_name}!") 

            case cmd if cmd.startswith('use'):
                parts = cmd.split()
                if len(parts) != 2:
                    print("Wrong format. Use: use <item>")
                    continue

                target_name = parts[1].lower()
                found = False

                for item in player.inventory:
                    if item.the_type.lower() == target_name:
                        found = True
                        try:
                            item.use(current_room)
                        except Exception as e:
                            print(f"Something went wrong while using the item: {e}")
                        break

                if not found:
                    print(f"You don't have an item named '{target_name}' in your inventory.")
            
            case cmd if cmd.startswith('interact'):
                parts = cmd.split()
                if len(parts) != 2:
                    print("Wrong format. Use: interact <item>")
                    continue

                target = parts[1].lower()
                found = False

                for obj in current_room.storage:
                    if obj.the_type.lower() == target:
                        found = True
                        try:
                            obj.interact()
                        except AttributeError:
                            print(f"The object '{target}' cannot be interacted with.")
                        break

                if not found:
                    print(f"No item named '{target}' found in this room.")

            case cmd if cmd.startswith('check'):
                parts = cmd.split()
                if len(parts) != 2:
                    print("Wrong format. Use: check <item>")
                    continue

                target = parts[1].lower()
                found = False

                for item in player.inventory:
                    if item.the_type.lower() == target:
                        item.check()
                        found = True
                        break

                if not found:
                    for item in current_room.storage:
                        if item.the_type.lower() == target:
                            item.check()
                            found = True
                            break

                if not found:
                    print(f"Cannot find an item named '{target}' in your inventory or this room.")
            
            case 'help':
                print('''
Available commands:
- w/a/s/d           : Move up / left / down / right
- look              : Look around the room
- quit              : Leave the game
- map               : Shows the map of this level
- seach <container> 
                    : Seach around the <container> to find out some useful things
                      EX. <search room> <search table>
- grab <container> <item>             
                    : Grab <item> from <container>, grab <container> <item>
                      EX. <grab table key>, <grab room black_key>
- bag               : Show the items in your bag
- use <item>        : Use the item in your bag
                      
''')

            case 'quit':
                print()
                print("Sometimes giving up is a choice...")
                print()
                quit(0)

            case _:
                print("I don't understand that command. Type 'help' if you're lost.")
        print()
        if isinstance(current_room, destination_room):
            print('''
As you step into the final chamber, the heavy door creaks open behind you.

The silence is no longer oppressive — it is peaceful.  
Light breaks through cracks in the ceiling,  
And for the first time, the air smells of freedom.

You have outwitted the riddles,  
Untangled the traps,  
And walked the path no fool could follow.

The maze fades behind you.  
You are free.

Congratulations — You have escaped.
                  ''')
            
main()
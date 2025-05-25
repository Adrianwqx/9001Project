from item import key, table, button,code_lock,note,balls_basket
from rooms import destination_room,Room

first_level_map = []
second_level_map = []
third_level_map = []

def create_first_map():

    # rooms creation           
    start_room = Room("Start Room", "An old dusty study with a wooden table in the corner and a large black door in this wall.")

    A = Room("First Room","A gray room, like no one's been in it for a long time.")
    A1 = Room("First Room","A gray room, like no one's been in it for a long time.")
    A2 = Room("First Room","A gray room, like no one's been in it for a long time.")
    A3 = Room("First Room","A gray room, like no one's been in it for a long time.")
    A4 = Room("First Room","A gray room, like no one's been in it for a long time.")

    B = Room("Second Room","A room that is as plain as most people's lives...")
    B1 = Room("Second Room","A room that is as plain as most people's lives...")
    B2 = Room("Second Room","A room that is as plain as most people's lives...")
    B3 = Room("Second Room","A room that is as plain as most people's lives...")
    B4 = Room("Second Room","A room that is as plain as most people's lives...")
    B5 = Room("Second Room","A room that is as plain as most people's lives...")

    C = Room("Empty Room","Oh no, it's a dead end .... There's nothing in the room ....")
    C1 = Room("Empty Room","Oh no, it's a dead end .... There's nothing in the room ....")
    C2 = Room("Empty Room","Oh no, it's a dead end .... There's nothing in the room ....")
    C3 = Room("Empty Room","Oh no, it's a dead end .... There's nothing in the room ....")
    
    D = Room("First Room","A gray room, like no one's been in it for a long time.")
    D1 = Room("First Room","A gray room, like no one's been in it for a long time.")
    D2 = Room("First Room","A gray room, like no one's been in it for a long time.")
    D3 = Room("First Room","A gray room, like no one's been in it for a long time.")
    D4 = Room("First Room","A gray room, like no one's been in it for a long time.")
    D5 = Room("First Room","A gray room, like no one's been in it for a long time.")

    end_room = destination_room()

    start_room.set_connection(A, 'W')
    A.set_connection(A1, 'N')
    A1.set_connection(A2, 'E')
    A1.set_connection(A3, 'N')
    A3.set_connection(A4, 'E')

    A.set_connection(B, 'W')
    B.set_connection(B1, 'S')
    B1.set_connection(B2, 'E')
    B2.set_connection(B3, 'E')
    B3.set_connection(B4, 'S')
    B1.set_connection(B5, 'W')

    B.set_connection(C, 'W')
    C.set_connection(C1, 'N')
    C1.set_connection(C2, 'E')
    C1.set_connection(C3, 'N')

    C.set_connection(D, 'W')
    D.set_connection(D1, 'N')
    D1.set_connection(D2, 'N')
    D.set_connection(D3, 'S')
    D3.set_connection(D4, 'S')
    D4.set_connection(D5, 'E')
    D5.set_connection(end_room, 'E')

    #lock rooms
    
    A.lock_room()
    A2.lock_room()
    A4.lock_room()

    B.lock_room()
    B3.lock_room()
    B4.lock_room()
    B5.lock_room()

    C.lock_room()
    
    D.lock_room()
    
    end_room.lock_room()

    # A1
    black_key = key(A,'black',start_room)
    table1 = table()
    table1.add_item(black_key)
    start_room.add_item(table1)

    # A2
    code_lock1 = code_lock("3512",A2)
    A1.add_item(code_lock1)
    note1 = note(1,"This note has the numbers 3512 written on it.")
    A3.add_item(note1)

    # A4
    code_lock2 = code_lock("6632",A4)
    A3.add_item(code_lock2)
    note2 = note(2,"This note has the numbers 6632 written on it.")
    table2 = table()
    table2.add_item(note2)
    D5.add_item(table2)

    # B
    white_key = key(B,'white',A)
    A2.add_item(white_key)

    # B3 B4 B5
    balls_basket1 = balls_basket('''
One flame flickers — red, lone and defiant.  
Three rays of golden light fall — never enough to warm the stone.  
No blue ripples stir the still pond — a silence too deep for movement.  
Two green sprouts curl beneath the soil — unseen, but waiting.

What you do not see speaks loudest.  
Listen to the colors that do not speak aloud.
                                 ''')
    B.add_item(balls_basket1)

    code_lock3 = code_lock("1032",B5)
    note3 = note(3,"Red,Blue,Yellow,Green")
    B1.add_item(code_lock3)
    B1.add_item(note3)

    code_lock4 = code_lock("1302",B3)
    note4 = note(4,"Red,Yellow,Blue,Green")
    B2.add_item(code_lock4)
    B2.add_item(note4)

    code_lock5 = code_lock("0213",B4)
    note5 = note (5,"Blue,Green,Red,Yellow")
    B3.add_item(code_lock5)
    B3.add_item(note5)

    # C
    note6 = note (6,"(37 x 42) + (81 x 23)")
    B4.add_item(note6)
    code_lock6 = code_lock("3417",C)
    B.add_item(code_lock6)

    # D
    note7 = note(7,"Thrice to thine, and thrice to mine,")
    C1.add_item(note7)
    note8 = note(8,"And thrice again, to make up nine. ")
    C2.add_item(note8)
    note9 = note(9,"Nine... and again nine — the charm's wound tight.")
    C3.add_item(note9)

    code_lock7 = code_lock("3339",D)
    C.add_item(code_lock7)

    # end_room
    green_key = key(end_room,'green',D5)
    table3 = table()
    table3.add_item(green_key)
    A4.add_item(table3)

    first_floor = [D2,C3,None,A3,A4]

    second_floor = [D1,C1,C2,A1,A2]

    third_floor = [D,C,B,A,start_room]

    fourth_floor = [D3,B5,B1,B2,B3]

    fifth_floor = [D4,D5,end_room,None,B4]

    first_level_map.extend([first_floor, second_floor, third_floor, fourth_floor, fifth_floor])

    return first_level_map

def create_second_map():
    return
def create_third_map():
    return

def show_map(current_position:Room, map_data: list) -> str:
    rows = len(map_data)
    cols = len(map_data[0])
    result = ""

    for r in range(rows):
        
        room_line = ""
        for c in range(cols):
            room = map_data[r][c]
            if room:
                if room == current_position:
                    label = "[O]" 
                elif isinstance(room, destination_room):
                    label = "[D]" 
                elif room.locked:
                    label = "[X]"
                else:
                    label = "[ ]"
            else:
                label = "   "
            room_line += label

            if c < cols - 1:
                right_room = map_data[r][c + 1]
                if room and right_room and hasattr(room, 'E') and room.E == right_room:
                    room_line += "-----"
                else:
                    room_line += "     "
        result += room_line + "\n"

        if r < rows - 1:
            conn_line = " "
            for c in range(cols):
                room = map_data[r][c]
                down_room = map_data[r + 1][c]
                if room and down_room and hasattr(room, 'S') and room.S == down_room:
                    conn_line += "|  "
                else:
                    conn_line += "   "

                if c < cols - 1:
                    conn_line += "     "
            result += conn_line + "\n"

    return result.rstrip()

def test():
    first_level_map = create_first_map()
    the_start = first_level_map[2][3]
    print(show_map(the_start,first_level_map))











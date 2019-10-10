def iterative_helper(game_state: Any):
    stack = Stack()
    stack.add(Storage(0, game_state))
    ID = 0
    place = []
    place_count = 0
    while stack.is_empty() == False:
        current_item = stack.remove()
        if current_item.state.get_possible_moves() == []:
            current_item.score = -1
            place.append(current_item)
            place_count += 1
        else:
            if current_item.children == []:
                temp = []
                for move in current_item.state.get_possible_moves():
                    temp.append(
                        Storage(ID + 1, current_item.state.make_move(move)))
                    ID += 1
                for item in temp:
                    current_item.children.append(item.id)
                stack.add(current_item)
                for item in temp:
                    stack.add(item)
            else:
                temp1 = []
                for item in place:
                    if item.id in current_item.children:
                        temp1.append(-1 * item.score)
                if not temp1 == []:
                    current_item.score = max(temp1)
                else:
                    current_item.score = 1
                place.append(current_item)
                place_count += 1
    print(place)
    return place[place_count - 1].score

ID = -1
    stack = Stack()
    stack.add(Storage(ID + 1, game_state))
    ID += 1
    place = []
    place_count = 0
    # experimental loop condition
    while not stack.is_empty():
        current_item = stack.remove()
        if current_item.state.get_possible_moves() == []:
            current_item.score = -1
            place.append(current_item)
            place_count += 1
        else:
            if current_item.children == []:
                temp = []
                for move in current_item.state.get_possible_moves():
                    temp.append(
                        Storage(ID + 1, current_item.state.make_move(move)))
                    ID += 1
                for item in temp:
                    current_item.children.append(item.id)
                stack.add(current_item)
                for item in temp:
                    stack.add(item)
            else:
                temp1 = []
                for item in place:
                    if item.id in current_item.children:
                        temp1.append(-1 * item.score)
                if not temp1 == []:
                    current_item.score = max(temp1)
                else:
                    current_item.score = 1
                place.append(current_item)
                place_count += 1
    print(place)
    return place[place_count - 1].score












stack = Stack()
    stack.add(Storage(0, game_state))
    ID = 0
    place = []
    place_count = 0
    loop = 1
    while stack.is_empty() == False:
        current_item = stack.remove()
        print("player: ", current_item.state.get_current_player_name(),
              "total: ", current_item.state.current_total, "loop = ", loop)
        if current_item.state.get_possible_moves() == []:
            print("yes")
            current_item.score = -1
            place.append(current_item)
            place_count += 1
        else:
            if current_item.children == []:
                print("no")
                temp = []
                moves = current_item.state.get_possible_moves()
                print("moves:" , len(moves))
                for move in moves:
                    print("move :", move)
                    new_state = current_item.state

                    new_state = new_state.make_move(move)
                    temp.append(
                        Storage(ID + 1, new_state))
                    ID += 1
                for item in temp:
                    item.children = []
                for item in temp:
                    current_item.children.append(item.id)

                stack.add(current_item)
                for item in temp:
                    stack.add(item)
                    print("player: ",
                          item.state.get_current_player_name(),
                          "total: ", item.state.current_total,
                          "children: ", item.children,
                          "Score: ", item.score)


            else:
                print("okay")
                temp1 = []
                for item in place:

                    if item.id in current_item.children:
                        temp1.append(-1 * item.score)
                if not temp1 == []:
                    current_item.score = max(temp1)
                else:
                    current_item.score = 1
                place.append(current_item)
                place_count += 1
        loop += 1
    for item in place:
        print(str(item.id) + ':' + str(item.score))
    print(ID)
    r = place[place_count - 1].score
    print(r)
    print("len of place =", len(place), place_count)

    return r










edits:

stack = Stack()
    stack.add(Storage(0, game_state))
    ID = 0
    place = []
    place_count = 0
    loop = 1
    while stack.is_empty() == False:
        current_item = stack.remove()
        if current_item.state.get_possible_moves() == []:
            current_item.score = -1
            place.append(current_item)
            place_count += 1
        else:
            if current_item.children == []:
                temp = []
                moves = current_item.state.get_possible_moves()
                for move in moves:
                    new_state = current_item.state
                    new_state = new_state.make_move(move)
                    temp.append(
                        Storage(ID + 1, new_state))
                    ID += 1
                for item in temp:
                    item.children = []
                for item in temp:
                    current_item.children.append(item.id)
                stack.add(current_item)
                for item in temp:
                    stack.add(item)
            else:
                temp1 = []
                for item in place:
                    if item.id in current_item.children:
                        temp1.append(-1 * item.score)
                if not temp1 == []:
                    current_item.score = max(temp1)
                else:
                    current_item.score = 1
                place.append(current_item)
                place_count += 1
    r = place[place_count - 1].score
    return r





edits:

def recursive_helper(game_state: Any) -> int:
    if game_state.get_possible_moves() == []:
        return -1
    else:
        move_scores = []
        for move in game_state.get_possible_moves():
            state_score = recursive_helper(game_state.make_move(move))
            move_scores.append(-1 * state_score)
        return max(move_scores)








loop = 1
    move_score = []
    print("player 1?: ", game_state.get_current_player_name(), "total: ",
          game_state.current_total)
    if game_state.get_possible_moves == []:
         state_score = -1
    else:
        for move in game_state.get_possible_moves():
            new_state = game_state.make_move(move)
            # print("player 1?: ", new_state.get_current_player_name(), "total: ", new_state.current_total, "loop: ", loop, "move: ", move)
            state_score = recursive_helper(new_state)
            #move_score = []
            move_score.append(-1 * state_score)
        if not move_score == []:
            state_score = max(move_score)
        else:
            state_score = 1
        loop += 1
    return state_score

edits:

def iterative_helper(game_state: Any) -> int:
    storage_list = []
    storage_list.append(Storage(game_state))
    stack = Stack()
    stack.add(storage_list[0])
    while not stack.is_empty:
        current_item = stack.remove()
        current_id = storage_list.index(current_item)
        if current_item.state.get_possible_moves == []:
            storage_list[current_id].score = -1
        else:
            if current_item.children == []:
                for move in current_item.state.get_possible_moves():
                    child_state = current_item.state.make_move(move)
                    storage_list.append(Storage(current_item.state.make_move(move)))


class Node:
    def __init__(self):
        self.id: int
        self.state: Any
        self.children: list
        self.score: int

def iterative_helper(game_state: Any) -> int:
    stack = Stack()
    first_node = Node()
    first_node.id = 0
    ID = 0
    first_node.state = game_state
    first_node.children = []
    first_node.score = None
    stack.add(first_node)
    place = []
    place_last_index = -1
    while not stack.is_empty():
        current_item = stack.remove()
        if current_item.state.get_possible_moves() == []:
            current_item.score = -1
            place.append(current_item)
            place_last_index += 1
        else:
            if current_item.children == []:
                states_list = []
                nodes_list = []
                for move in current_item.state.get_possible_moves():
                    states_list.append(current_item.state.make_move(move))
                for state in states_list:
                    node = Node()
                    node.id = ID + 1
                    ID += 1
                    node.state = state
                    node.children = []
                    node.score = None
                    nodes_list.append(node)
                for node_index in nodes_list:
                    current_item.children.append(node_index.id)
                stack.add(current_item)
                for node_index in nodes_list:
                    stack.add(node_index)
            else:
                scores_list = []
                for item in place:
                    if item.id in current_item.children:
                        scores_list.append(-1 * item.score)
                current_item.score = max(scores_list)
                place.append(current_item)
                place_last_index += 1
    return place[place_last_index].score





old:
stack = Stack()
    stack.add(Storage(0, game_state))
    ID = 0
    place = []
    place_count = 0
    loop = 1
    while stack.is_empty() == False:
        current_item = stack.remove()
        if current_item.state.get_possible_moves() == []:
            current_item.score = -1
            place.append(current_item)
            place_count += 1
        else:
            if current_item.children == []:
                temp = []
                moves = current_item.state.get_possible_moves()
                for move in moves:
                    new_state = current_item.state
                    new_state = new_state.make_move(move)
                    temp.append(
                        Storage(ID + 1, new_state))
                    ID += 1
                for item in temp:
                    item.children = []
                for item in temp:
                    current_item.children.append(item.id)
                stack.add(current_item)
                for item in temp:
                    stack.add(item)
            else:
                temp1 = []
                for item in place:
                    if item.id in current_item.children:
                        temp1.append(-1 * item.score)
                if not temp1 == []:
                    current_item.score = max(temp1)
                else:
                    current_item.score = -1
                place.append(current_item)
                place_count += 1
    r = place[place_count - 1].score
    return r



old: kinda

stack = Stack()
    first_node = Node()
    first_node.id = 0
    ID = 0
    first_node.state = game_state
    first_node.children = []
    first_node.score = None
    stack.add(first_node)
    place = []
    place_last_index = -1
    while not stack.is_empty():
        current_item = stack.remove()
        print(current_item is first_node)
        if current_item.state.get_possible_moves() == []:
            print("okay1")
            current_item.score = -1
            place.append(current_item)
            place_last_index += 1
        else:
            if current_item.children == []:
                print("okay3")
                states_list = []
                nodes_list = []
                for move in current_item.state.get_possible_moves():
                    states_list.append(current_item.state.make_move(move))
                for state in states_list:
                    node = Node()
                    node.id = ID + 1
                    ID += 1
                    node.state = state
                    node.children = []
                    node.score = None
                    nodes_list.append(node)
                for node_index in nodes_list:
                    current_item.children.append(node_index.id)
                stack.add(current_item)
                for node_index in nodes_list:
                    stack.add(node_index)
            else:
                print("okay4")
                scores_list = []
                for item in place:
                    if item.id in current_item.children:
                        scores_list.append(-1 * item.score)
                current_item.score = max(scores_list)
                place.append(current_item)
                place_last_index += 1

    return place[place_last_index].score






CORRECTCODE:

stack = Stack()
    first_node = Node()
    first_node.id = 0
    ID = 0
    first_node.state = game_state
    first_node.children = []
    first_node.score = None
    stack.add(first_node)
    place = []
    place_last_index = -1
    while not stack.is_empty():
        current_item = stack.remove()
        if current_item.state.get_possible_moves() == []:
            current_item.score = -1
            place.append(current_item)
            place_last_index += 1
        else:
            if current_item.children == []:
                states_list = []
                nodes_list = []
                for move in current_item.state.get_possible_moves():
                    states_list.append(current_item.state.make_move(move))
                for state in states_list:
                    node = Node()
                    node.id = ID + 1
                    ID += 1
                    node.state = state
                    node.children = []
                    node.score = None
                    nodes_list.append(node)
                for node_index in nodes_list:
                    current_item.children.append(node_index.id)
                stack.add(current_item)
                for node_index in nodes_list:
                    stack.add(node_index)
            else:
                scores_list = []
                for item in place:
                    if item.id in current_item.children:
                        scores_list.append(-1 * item.score)
                current_item.score = max(scores_list)
                place.append(current_item)
                place_last_index += 1
    return place[place_last_index].score

for letter in self.current_board:
    if letter.isalpha():
        self.cell_list.append(letter)
self.rows = []
start = 0
count = 2
while count <= side_length + 1:
    self.rows.append(self.cell_list[start:start + count])
    start = start + count
    count = count + 1
self.rows.append(self.cell_list[len(self.cell_list) - side_length:])
self.row_ley_lines = {}
self.up_ley_lines = {}
self.down_ley_lines = {}
if side_length == 1:
    self.row_ley_lines = {51: ['A', 'B'], 52: ['C']}
    self.up_ley_lines = {31: ['A'], 32: ['B', 'C']}
    self.down_ley_lines = {41: ['B'], 42: ['A', 'C']}
if side_length == 2:
    self.row_ley_lines = {51: ['A', 'B'], 52: ['C', 'D', 'E'], 53: ['F', 'G']}
    self.up_ley_lines = {31: ['A', 'C'], 32: ['B', 'D', 'F'], 33: ['E', 'G']}
    self.down_ley_lines = {41: ['B', 'E'], 43: ['A', 'D', 'G'], 42: ['C' 'F']}
if side_length == 3:
    self.row_ley_lines = {51: ['A', 'B'], 52: ['C', 'D', 'E'],
                          53: ['F', 'G', 'H', 'I'], 54: ['J', 'K', 'L']}
    self.up_ley_lines = {31: ['A', 'C', 'F'], 32: ['B', 'D', 'G', 'J'],
                         33: ['E', 'H', 'K'], 34: ['I', 'L']}
    self.down_ley_lines = {41: ['B', 'E', 'I'], 43: ['C', 'J', 'K'],
                           42: ['J' 'F'], 44: ['A', 'D', 'H', 'L']}
if side_length == 4:
    self.row_ley_lines = {51: ['A', 'B'], 52: ['C', 'D', 'E'],
                          53: ['F', 'G', 'H', 'I'],
                          54: ['J', 'K', 'L', 'M', 'N'],
                          55: ['O', 'P', 'Q', 'R']}
    self.up_ley_lines = {31: ['A', 'C', 'F', 'J'],
                         32: ['B', 'D', 'G', 'K', 'O'],
                         33: ['E', 'H', 'L', 'P'], 34: ['I', 'M', 'Q'],
                         35: ['N', 'R']}
    self.down_ley_lines = {41: ['B', 'E', 'I', 'N'], 43: ['F', 'P', 'K'],
                           42: ['J' 'O'], 44: ['C', 'G', 'Q', 'L'],
                           45: ['A', 'D', 'H', 'M', 'R']}
if side_length == 5:
    self.row_ley_lines = {51: ['A', 'B'], 52: ['C', 'D', 'E'],
                          53: ['F', 'G', 'H', 'I'],
                          54: ['J', 'K', 'L', 'M', 'N'],
                          55: ['O', 'P', 'Q', 'R', 'S', 'T']
                          56: ['U', 'V', 'W', 'X', 'Y']}
    self.up_ley_lines = {31: ['A', 'C', 'F', 'J', 'O'],
                         32: ['B', 'D', 'G', 'K', 'P', 'U'],
                         33: ['E', 'H', 'L', 'Q', 'V'],
                         34: ['I', 'M', 'R', 'W'], 35: ['N', 'S', 'X'],
                         36: ['T', 'Y']}
    self.down_ley_lines = {41: ['B', 'E', 'I', 'N', 'T'], 43: ['J', 'P', 'V'],
                           42: ['U' 'O'], 44: ['F', 'K', 'Q', 'W'],
                           45: ['C', 'G', 'L', 'X', 'R'],
                           46: ['A', 'D', 'H', 'M', 'S', 'Y']}

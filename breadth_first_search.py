from collections import deque
 
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["alice"] = ["PEGGY"]
graph["bob"] = ["anuj", "PEGGY"]
graph["claire"] = ["thom", "jonney"]
graph["PEGGY"] = []
graph["anuj"] = []
graph["thom"] = []
graph["jonney"] = []

def mango_seller(name):
    """search if there any mango seller"""
    if name[-1] == "m": # work for example
        return True
    
def search(name):
    """Search the friends network"""
    search_queue = deque()
    search_queue += graph["you"]
    checked = []
    while search_queue:
        person = search_queue.popleft()
        if person not in checked:
            if mango_seller(person):
                print(f"{person} is mango seller")
                return True
            else:
                search_queue += graph[person]
                checked.append(person)
        
    return False

search("you")
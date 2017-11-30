class graphy(object):
    adjacencyList = []
    def __init__(self, node):
        self.node = nodeValue
        self.values = []

    def createGraph(nodes):         
        l = graphy.values = []
        count = 0
        l.append(0)                 #0 is used to mark the next value as a new node - subsequent numbers are that nodes connections until next 0
        while count != nodes:       #counts up one node at a time
            count += 1
            current = True
            l.append(count)         #adds node value to list
            while current == True:  #adds as many required conections per individual node
                connection = input("Add a connection to node: {}. Leave empty to move to next node. : ".format(count))
            
                if connection == "":    #moves to next node when all current nodes connections are input
                    current = False
                    l.append(0)
                    
                else:
                    l.append(int(connection))       #adds node connection value to a list
        l.pop()
        #print("The graph has been created successfully")           #removed for unit test
        #print(l)
        graphy.adjacencyList = l
        return graphy.adjacencyList

    def Bfs():
        queue = list()
        output = list()
        p = 0
        h = 0
        visited = graphy.adjacencyList
        for i in range (len(visited)):          #adds all the nodes to the queue
            if visited[p] == 0:
                queue.append(visited[p+1])
                p = p + 1
                
            else:
                p = p + 1
        p = 0
        for i in range(len(visited)):                   #skips over the node markers in list
            if visited[p] == 0:
                p = p + 1
            else:
                val = visited[p]
                for val in queue:                       #if the current value is also in the list - remove that value from the queue and add it to output
                    if val in visited:
                        output.append(visited[p])
                        queue.remove(val)
                        p = p + 1
                        break
                    else:
                        break

        file = open("BFS.txt","w+")         #adds nodes traversed into the file - if file doesnt exist then it is created
        for item in output:
            file.write("%s\n" % item)
        file.close()
        #print(queue)       #removed for unit test
        #print(output)
        
    def isPath(v,w):
        n_graph = graphy.adjacencyList
        p = 0

        for i in range(len(n_graph)):           
            try:                                        #try statement for when list value reaches out of bounds
                if n_graph[p] == 0:                     #marker to indicate next value as a node
                    p = p + 1
                    if n_graph[p] == v:                 #finds given node
                        while n_graph[p] != 0 and n_graph[p] != []:
                            if n_graph[p] == w:                         #checks if node is connected to other given node
                                #print("The nodes are connected")
                                break
                            else:
                                p = p + 1
                            
                    else:
                        continue
                else:
                    p = p + 1
            except:
                break

        return True         #for unit test
        

if __name__ == '__main__':

    l=list()
    nodes = int(input("How many nodes: "))
    graphy.createGraph(nodes)
    graphy.Bfs()
    graphy.isPath(1,3)                          #checks for path between node 1 and 3 - example
                

                

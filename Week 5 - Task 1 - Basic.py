class Node(object):
      def __init__(self, value):
          self.value=value
          self.next=None
          self.prev=None
 
class List(object):
      def __init__(self):
          self.head=None
          self.tail=None
      def insert(self,n,x):
          #Not actually perfect: how do we prepend to an existing list?
          if n!=None:
              x.next=n.next
              n.next=x
              x.prev=n
              if x.next!=None:
                  x.next.prev=x              
          if self.head==None:
              self.head=self.tail=x
              x.prev=x.next=None
          elif self.tail==n:
              self.tail=x
      def display(self):
          values=[]
          n=self.head
          while n!=None:
              values.append(str(n.value))
              n=n.next  
          print ("List: ",",".join(values))

      def duplicate(self):
            n = dupe = self.head                            #assigns the checkers to the start of the lists
            while n is not None:                            #checks that the current node has a value
                  while dupe.next is not None:              #checks if the next node has a value
                        if dupe.next.value == n.value:
                              dupe.next = dupe.next.next    #if they match, the duplicate is removed
                        else:
                              dupe = dupe.next
                  n = dupe = n.next
         
if __name__ == '__main__':
      l=List()
      l.insert(None, Node(4))
      l.insert(l.head,Node(6))
      l.insert(l.head,Node(8))
      l.insert(l.head,Node(8))                              #duplicate node added for testing
      l.duplicate()                                         #runs the duplicate remover before displaying the results and after node values have been inserted
      l.display()

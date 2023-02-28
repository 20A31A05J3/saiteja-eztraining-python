'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def printList(self):
        temp=self.head
        if not temp:
            print("list is empty")
            return
        else:
            print('Start:',end=' ')
        while temp:
            print(temp.data,end='->')
            temp=temp.next
        print('end.')
    def insert(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        #if data is smaller than the head
        elif self.head.data>=new_node.data:
            new_node.next=self.head
            self.head=new_node
        else:
            #locate node before the insertion point
            current=self.head
            while current.next and new_node.data>current.next.data:
                current=current.next
            #insertion
            new_node.next=current.next
            current.next=new_node
    def delete(self,key):
            #if the list is empty
        if self.head is None:
            print("Deletion Error.The list is empty")
            return
            #if the key is in head
        if self.head.data==key:
            self.head=self.head.next
            return
        current=self.head
        while current:
            if current.data==key:
                break
            previous=current
            current=current.next
            #if the key is not found
        if current is None:
            print("Deletion Error:Key is not found")
        else:
            previous.next=current.next
#__name is python special variable
if __name__=='__main__':
    #create an object
    LL=LinkedList()
    print(' ')
    #insert some nodes
    LL.insert(10)
    LL.insert(12)
    LL.insert(8)
    LL.insert(11)
    LL.insert(10)
    LL.printList()
    LL.delete(12)
    LL.delete(8)
    LL.delete(10)
    LL.printList()'''

'''#creating my modules
#fn in my another file,acting as a module here
import fn
fn.printing()

print(__name__)'''

'''#lets say you have a lot of functions in your project
#you can give all definitions at one place
#and give all function calls inside main
#easy to read,especially for others
print("before function")
def f1():
    print("f1")
def f2():
    print("f2")
def f3():
    print("f#")
if __name__=="__main__":'''

'''#create node
class Node:
    def __init__(self,data):
         self.data=data
         self.previous=None
         self.next=None

class dll:
    def __init__(self):
        self.head=None

    def display(self):
        if self.head is None:
            print('empty')
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next

l=dll()
n1= Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
l.display()'''

'''class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None

    def insert_start(self):

        n=Node(300)
        temp=self.head
        temp.prev=n
        n.next=temp
        self.head=n
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
l.insert_start()
l.display()'''

'''class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None

    def insert_end(self):
        n=Node(300)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=n
        n.prev=temp
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
l.insert_end()
l.display()'''

'''class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None

    def insert_pos(self,pos):
        n=Node(300)
        temp=self.head
        for i in range (1,pos-1):
            n.prev=temp
            n.next=temp.next
            temp.next.prev=n
            temp.next=n
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
l.insert_pos(2)
l.display()'''

'''class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None

    def delete_beginning(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
       
    def display(self):
        if self.head is None:
            print("ll is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
l.delete_beginning()
l.display()'''

'''class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None

    def delete_end(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
    def display(self):
        if self.head is None:
            print("ll is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
l.delete_end()
l.display()'''

'''class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None

    def delete_position(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
    def display(self):
        if self.head is None:
            print("ll is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
l.delete_position(1)
l.display()'''

'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CreateList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next  = self.head
    #adding node at the end of LL
    def add(self,data):
        newNode = Node(data)
    #Is empty?
        if self.head.data is None:
            self.head = newNode
            self.tail = newNode
            newNode.next = self.head
        else:
            self.tail.next = newNode
            self.tail = newNode
            #It is CLl,so tail will point to head
            self.tail.next = self.head

    def display(self):
        current = self.head
        if self.head is None:
            print("List is empty")
            return
        else:
            print("Nodes of the linked list:")
            print(current.data,"-->")
            while (current.next != self.head):
                current = current.next
                print(current.data,"-->")

class CircularLinkedList:
    c1 = CreateList()
    c1.add("S")
    c1.add("M")
    c1.add("I")
    c1.add("L")
    c1.add("E")
    c1.display()'''
    


    
    
        

        

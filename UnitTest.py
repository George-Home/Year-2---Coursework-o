from Week1Task1Basic import string_join
from Week1Task2Basic import Armstrong_Chk
from Week2Task1Basic import m_Poly
from Week2Task2Basic import palindrome
from Week3Task1Basic import mirror
from Week3Task2Basic import linear
from Week4Task1Basic import *
from Week5Task1Basic import *
from Week7Task123Basic import *

	#name of file to test 		                #name of methods to test
import unittest

class Test(unittest.TestCase):
	
#testcase each test case must begin with test
    def test_week1_task1(self):                         #test if function output is equal to expected output
        
        actual = string_join('unit','test')
        expected = "utneistt"
        self.assertIn(actual, expected)

    def test_week1_task2(self):                         #test if output is true

        actual = Armstrong_Chk (371)
        self.assertTrue(actual)

    def test_week2_task1(self):                         #test if function output is equal to expected output

        expected =[6, 5, 25, 14, 19, 9]
        actual = m_Poly([3,1,9],[2,1,2,1],2,3)
        self.assertListEqual(actual, expected)
        
    def test_week2_task2(self):                         #test if output is true

        actual = palindrome([1,3,6,6,3,1])
        self.assertTrue(actual)

    def test_week3_task1(self):                         #test if function output is equal to expected output

        actual = mirror('testing')
        expected = "gnitset"
        self.addTypeEqualityFunc(actual, expected)

    def test_week3_task2(self):                         #test if output is true

        actual = linear(5)
        self.assertTrue(actual)

    def test_week4_task1(self):                         #test if function outputs are equal to expected output

        expected = [0,1,2,3,4,5,6,7,8,9]
        sequence = [2,7,9,4,1,5,3,6,0,8]
        try:
            actual = bubbleSort([2,7,9,4,1,5,3,6,0,8])          #performs all three checks in one test for each sort method
            self.assertEqual(actual, expected)
            actual = insertionSort([2,7,9,4,1,5,3,6,0,8])
            self.assertListEqual(actual, expected)
            actual = selectionSort([2,7,9,4,1,5,3,6,0,8])
            self.assertListEqual(actual, expected)
        except:
            print("sequence is invalid")

    #Week 4 - Task 2 - no test required for the guessing game as it essentially tests itself every time it is run

    def test_week5_task1(self):                         #test if function output is equal to expected output

        expected = ['4','8','6']
        l=List()
        l.insert(None, Node(4))                         #adds values to the list
        l.insert(l.head,Node(6))
        l.insert(l.head,Node(8))
        l.insert(l.head,Node(8))
        l.duplicate()                                   #remove the duplicates from list
        actual = l.display()                            #displays the list and outputs result

        self.assertListEqual(actual, expected)
        
    def test_week7_task1(self):

        expected = [0, 1, 3, 0, 2, 0, 3, 1]

        l=list()
        nodes = int(3)                      #for test - input is node 1 connected to 3 and vice versa
        #actual = graphy.createGraph(nodes) #adjust this to begin test
        #self.assertListEqual(actual, expected)

        
        graphy.Bfs()
        actual = graphy.isPath(1,3)
        #self.assertTrue(actual)

        
# run tests		
if __name__ == "__main__":
	unittest.main()
	

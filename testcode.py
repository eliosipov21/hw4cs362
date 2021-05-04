import unittest
import code 

class testCaseAdd(unittest.TestCase):
    def cubetest_1(self):
        result = code.volume_cube(3)
        self.assertEqual(result, 27)
    def cubetest_2(self):
        result = code.volume_cube(-3)
        self.assertEqual(result, "error, input less than zero")
    def cubetest_3(self):
        result = code.volume_cube("five")
        self.assertEqual(result, "error, input not an int")

    def listtest_1(self):
        list1 = [1,2,3]
        result = code.avg_list(list1)
        self.assertEqual(result, 6)
    def listtest_2(self):
        list2 = []
        result = code.avg_list(list2)
        self.assertEqual(result, "empty list, try again")
    def listtest_3(self):
        list3 = "[1,2,3]" 
        result = code.avg_list(list3)
        self.assertEqual(result, "not a list, try again")

    def nametest_1(self):
        fname = "Joe"
        lname = "Rogan"
        result = code.full_name(fname, lname)
        self.assertEqual(result, "Joe Rogan")
    def nametest_2(self):
        fname = "FM"
        lname = 2030
        result = code.full_name(fname, lname)
        self.assertEqual(result, "FM 2030")
    def nametest_3(self):
        fname = [1,3,3] 
        lname = 456 
        result = code.full_name(fname, lname)
        self.assertEqual(result, "error")








if __name__ == '__main__':
    unittest.main()

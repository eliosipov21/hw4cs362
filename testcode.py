import unittest
import code 

class testCaseAdd(unittest.TestCase):
    def test_cube1(self):
        result = code.volume_cube(3)
        self.assertEqual(result, 27)
        result2 = code.volume_cube(3.1)
        self.assertEqual(result2, pow(3.1, 3))
    def test_cube2(self):
        result = code.volume_cube(-3)
        self.assertEqual(result, "error, input less than zero")
        result2 = code.volume_cube(-3.5)
        self.assertEqual(result2, "error, input less than zero")
        result3 = code.volume_cube(1000000000)
        self.assertEqual(result3, pow(1000000000, 3))
    def test_cube3(self):
        result = code.volume_cube("five")
        self.assertEqual(result, "error, input not an int")
        result2 = code.volume_cube("5")
        self.assertEqual(result2, "error, input not an int")


    def test_list1(self):
        list1 = [1,2,3]
        result = code.avg_list(list1)
        self.assertEqual(result, 6)
    def test_list2(self):
        list2 = []
        result = code.avg_list(list2)
        self.assertEqual(result, "empty list, try again")
    def test_list3(self):
        list3 = "[1,2,3]" 
        result = code.avg_list(list3)
        self.assertEqual(result, "not a list, try again")

    def test_name1(self):
        fname = "Joe"
        lname = "Rogan"
        result = code.full_name(fname, lname)
        self.assertEqual(result, "Joe Rogan")
    def test_name2(self):
        fname = "FM"
        lname = 2030
        result = code.full_name(fname, lname)
        self.assertEqual(result, "FM 2030")
    def test_name3(self):
        fname = [1,3,3] 
        lname = 456 
        result = code.full_name(fname, lname)
        self.assertEqual(result, "error")








if __name__ == '__main__':
    unittest.main()

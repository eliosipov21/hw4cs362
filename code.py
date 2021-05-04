#Question 1
def volume_cube(x):
    if(x<0):
        return "error, input less than zero"
    if(not(isinstance(x, int)) and not(isinstance(x, float))):
        return "error, input not an int"
    return pow(x, 3)


#Question 2
def avg_list(mylist):
    mysum = mylist[0] 
    for nt in mylist:
        mysum += element
    avg = mysum/(len(mylist))
    return avg

#Question 3
def full_name(fname, lname):
    return fname + " " + lname 


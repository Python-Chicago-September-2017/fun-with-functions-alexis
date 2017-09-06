def odd_even():
    for num in range(1,2001):
        if num %2 == 0:
            print "Number is {}. This is an even number.".format(num)
        else:
            print "Number is {}. This is an odd number.".format(num)

def multiply(the_list, num):
    for x in range(len(the_list)):
        the_list[x] *= num
    return the_list

def layered_multiples(arr):
    new_arr = []
    for x in arr:
        in_arr = []
        for i in range(x):
            in_arr.append(1)

        new_arr.append(in_arr)    
    return new_arr

a = [2,4,10,16]

mult = multiply(a, 5)
lala = multiply([2,4,5], 3)
print mult
print lala
hacker = layered_multiples(multiply([2,4,5],3))
print hacker
odd_even()
# Name : Oscar Keur	
# Student number : 11122102
'''
This module contains an implementation of split_string.
'''

# You are not allowed to use the standard string.split() function, use of the
# regular expression module, however, is allowed.
# To test your implementation use the test-exercise.py script.

# A note about the proper programming style in Python:
#
# Python uses indentation to define blocks and thus is sensitive to the
# whitespace you use. It is convention to use 4 spaces to indent your
# code. Never, ever mix tabs and spaces - that is a source of bugs and
# failures in Python programs.


def split_string(source, separators):
    '''
    Split a string <source> on any of the characters in <separators>.

    The ouput of this function should be a list of strings split at the
    positions of each of the separator characters.
    '''
    # initialize variables
    separator = [separators]
    locations = []
    output = []
    i = 0
    j = 0
    k = 0

    # determine where the separators are
    for i in range(len(source)):
        if source[i] in separators:
            locations.append(i)

    # split source on basis of locations
    while j in range(len(source)):
        if j not in locations:
            k = j + 1
            while k not in locations and k in range(len(source)):
                k += 1
            output.append(source[j:k])
        if k > 1:
            j += len(output[-1])
        else:
            j += 1


    # return the outputlist   
    return output


if __name__ == '__main__':
    # You can try to run your implementation here, that will not affect the
    # automated tests.
    # should print: ['c', 'd', 'r']
    print split_string('abacadabra', 'ab')  
    # should print: ['abc']
    print split_string('abc', '')  
    # should print: ['aba', 'adaba', 'a']
    print split_string('abacadabra', 'cr')  
    # should print: ['a', 'acada']
    print split_string('abacadabra', 'b')  


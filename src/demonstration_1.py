"""
Define a function that transforms a given string into a new string where the
original string was split into strings of a specified size.

For example:
If the input string was this:

"supercalifragilisticexpialidocious"

and the specified size was 3, then the return string would be:

"sup erc ali fra gil ist ice xpi ali doc iou s"

The assumptions we are making about our input are the following:

- The input string's length is always greater than zero.
- The string has no spaces.
- The specified size is always a positive integer.
"""
def split_in_parts(s, part_length):
    # Your code here
    # we need to split the input string into smaller chunks of characters 

    # init an output list 
    output = []
    # need to iterate over characters in the input string
    for index in range(0, len(s), part_length):
        output.append(s[index: index + part_length])
    return output
        # a counter will count up to part_length
            # if counter is == part_length, the substring amount is met 
                # push the substring to a list 
                    # return the contents of the list the substrings were place in 

printed_list = split_in_parts("supercalifragilisticexpialidocious", 3)
# print(printed_list)
# Your code here

# List comprehension syntax
# This accomplishes the same thing as the above function, but it uses LIST COMPREHENSION syntax
def split_comprehension(string, part_length):
    return [string[i:i + part_length] for i in range(0, len(string), part_length)]

print(split_comprehension("supercalifragilisticexpialidocious", 3))


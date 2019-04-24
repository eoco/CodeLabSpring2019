# A hashmark (or what was known as a pound symbol before twitter came along) is used to make a comment in Python. The interpreter ignores any text after a hashmark and does not consider it code.
# sys is a built-in python module that gives us some 'system' level abilities. Here, we use it to get arguments from the command line
# To use a module you must first import it in, so that your code has access to it
# A module is just more python code in another file (or files) that has been written in such a way to allow for importing
import sys

# this imports the regular expression module. Regular expressions are great for finding/changing/counting text, but can be pretty hard to understand at first. Luckily you can usually find code someone else has written just by asking Google the right question!
import re

# put a check in to stop running the script if we do not receive the right number of arguments on the command line
# the 'sys ' module has an 'argv' property, which returns any arguments (parameters) that were passed via the command line
# there is always an sys.argv[0] which is the script itself
# So since we have three expected arguments (the script, which is argv[0], the text file to search (argv[1]), and the word to search for (argv[2])) we can check and make sure that
# we did indeed get 3 arguments passed to us. If we did not (we forgot to pass the word or whatever), the check below will stop the script and tell the user that they must supply a text file and a word
# 'len' is a Python function that returns the length or count of something- in this case the 'count' of passed arguments
if len(sys.argv) != 3:
    print("You must supply a text file and a word in quotes to this script.")
else:
    # if we have made it to this point, that means that we have the expected amount of arguments passed to us
    #  First we assign a variable named 'passedTextFilePath' to the value that was passed in the command line arguments. We assume that this is indeed a path to a text file
    passedTextFilePath = sys.argv[1]
    # we then assign a variable named "passedTextFile" to the actual file at the path (open tells Python to access the file)
    passedTextFile = open(passedTextFilePath)
    # finally, we set up a third variable named fileText to capture all the text in the file by using the 'read' function
    fileText = passedTextFile.read()

    # Now, one great thing about Python is that you can be very succinct. The above could all be written as one line:
    # fileText = open(sys.argv[1]).read()
    # but when you are learning, I think it is more helpful to break this all apart into separate variables to make it clearer what you are doing

    # so now that we have gotten our text loaded into a variable, we need to get our other 'word' argument that was passed
    word = sys.argv[2]

    # this is the actual code that gets the count. It is a little dense! But it is bascially setting a 'count' varaible that gets a summed (total) value from iterating the text file with the re module with the provided word.
    count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word), fileText))

    # finally, we just give our results back to the user using our string substitutions we have been working with today
    print("The word '%s' is in %s %s times." % (word, passedTextFilePath, count))

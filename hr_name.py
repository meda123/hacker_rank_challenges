def print_full_name():
    firstname = raw_input()
    lastname = raw_input()

    message = "Hello %s %s ! You just delved into python. " %(firstname,lastname) 
    return message 

test = print_full_name()
print test 

# Guido Rossum
# Hello Guido Rossum! You just delved into python.
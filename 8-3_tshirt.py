def make_shirt(shirt_size, message_text):
    '''Display information about size and message message to print 
       on the make shirt request.'''
    print(f"The size of the requested is {shirt_size}.")
    print(f"The message to printed on the shirt is {message_text.capitalize()}.")
    
make_shirt(12,"its raining cats and dogs!!!")
make_shirt(message_text = "its raining cats and dogs!!!", shirt_size=12)
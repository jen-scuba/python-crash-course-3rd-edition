def make_shirt(message_text, shirt_size='large'):
    '''Display information about size and message message to print 
       on the make shirt request.'''
    print(f"The size of the shirt requested is {shirt_size.title()}.")
    print(f"The message to printed on the shirt is: {message_text.capitalize()}.")
    
make_shirt("its raining cats and mice!!!")
make_shirt(message_text = "the sun is shining today!", shirt_size="medium")
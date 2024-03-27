def show_messages(text_messages):
    """
    Make a list cintaing a series of short text messages
       Pass a list to a function that pints each text message.
    """
    for message in text_messages:
        print(message)

text_messages = ["Good afternoon!","Good evening Jill, how was your day?","How about dinner at 6pm?"]
show_messages(text_messages)
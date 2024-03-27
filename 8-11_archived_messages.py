def send_messages(text_messages, sent_messages):
    """
    This function prints each text message
    and moves the printed message to a new list
    """
    while text_messages:
          send_text = text_messages.pop()
          print(f"Sending text: {send_text}")
          sent_messages.append(send_text)


def show_sent_messages(sent_messages):
    """
    Print the list of text messages sent
    """
    for message in sent_messages:
        print(message)


text_messages = ["Good afternoon!","Good evening Jill, how was your day?","How about dinner at 6pm?"]
sent_messages = []

send_messages(text_messages[:], sent_messages)
show_sent_messages(sent_messages)
print("\nOriginal list:")
for message in text_messages:
    print(message)
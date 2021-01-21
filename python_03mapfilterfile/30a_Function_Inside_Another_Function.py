def display(name, msg_value):
    def message(message_value):
        return "Hello " + message_value + " "
    result = message(msg_value) + name
    return result

print(display("Vishal", "Agarwal"))
# A function cannot be called outside if the function is defined inside another function
print(message("Agarwal"))    

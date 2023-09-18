from neuralite.interpreter import ai # Imports framework

assistant = ai.compiled('model.nlite') # Loads the compiled model

cycle_end = False # Starts the AI cycle

while not cycle_end: # Main cycle
    message = input("Enter a message: ") # Prompts user with message
    if message.lower() == "stop": # Exit with 'stop'
        cycle_end = True # Ends cycle
    else:
        print(assistant.process_input(message)) # Prints the response
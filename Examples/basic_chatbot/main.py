from neuralite.interpreter import ai

assistant = ai('dataset.json')

cycle_end = False

while not cycle_end:
    message = input("Enter a message: ")
    if message.lower() == "stop":
        cycle_end = True
    else:
        print(assistant.process_input(message))

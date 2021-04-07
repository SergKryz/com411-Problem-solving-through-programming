
import basics.output.simple_message as simple_message
import basics.output.multiline_message as multiline_message
import basics.output.escape_characters as escape_characters
def run_block_a():
    print("\n Which program in 'Block A: Basics' do you wish to run?")
    response = input()
    if (response == "simple message"):
      simple_message.run()
    elif (response == "multiline message"):
      multiline_message.run()
    elif (response == "escape characters"):
      escape_characters.run()
    else:
      print("\nInvalid option, please try again:")

def run():
    is_running = True

    while(is_running):
        print("\nWhat would you like to do?")
        print("[a] Run 'Block A: Basics' programs")
        print("[q] Quit")
        response = input()

        if (response == "a"):
            run_block_a()
        elif (response == "q"):
            print("End of the program.")
            break
        else:
            print("\nInvalid option! Please try again.")

run()
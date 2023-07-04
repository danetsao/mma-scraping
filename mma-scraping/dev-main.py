import curses

OPTIONS = ['Option 1', 'Option 2', 'Go']

def get_options():
    selected_indexes = []
    current_option = 0

    while True:
        # Display the OPTIONS
        for i, option in enumerate(OPTIONS):
            symbol = '◉' if i in selected_indexes else '◯'
            print(f'{symbol} {option}')

        # Handle user input
        choice = input("Select an option (Enter to toggle selection, 'Go' to finish): ")

        if choice == 'Go':
            return selected_indexes
        elif choice.isdigit() and 0 <= int(choice) < len(OPTIONS):
            option_index = int(choice)
            if option_index in selected_indexes:
                selected_indexes.remove(option_index)
            else:
                selected_indexes.append(option_index)


def do_process(selected_indexes):
    pass

def intro():
    # Print cool ascii art
    print('''
                                                          _             
 _ __ ___  _ __ ___   __ _       ___  ___ _ __ __ _ _ __ (_)_ __   __ _ 
| '_ ` _ \| '_ ` _ \ / _` |_____/ __|/ __| '__/ _` | '_ \| | '_ \ / _` |
| | | | | | | | | | | (_| |_____\__ \ (__| | | (_| | |_) | | | | | (_| |
|_| |_| |_|_| |_| |_|\__,_|     |___/\___|_|  \__,_| .__/|_|_| |_|\__, |
                                                   |_|            |___/ 
''')


def main():
    intro()
    selected_indexes = get_options()

    print('Selected OPTIONS:')
    
    for i in selected_indexes:
        print(OPTIONS[i])
    do_process(selected_indexes)

if __name__ == '__main__':
    main()
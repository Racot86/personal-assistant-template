def c_show_cmd(cmd):
    #print('contacts show command')
    print(cmd)
    range_days = None
    if not cmd:
        print("Empty command. Please enter a command.")
        return
    
    try:  

        for item in cmd:
            try:
                range_days = int(item)
            except ValueError:
                pass

        if "all" in cmd and "show" in cmd:
            print("run Show all")
        elif "birthdays" in cmd and range_days:
            print("run birthdays" )
        elif cmd[0] == "show" and cmd[1]:
            print("run birthday Name show")
        else:
            print("Invalid command. Please check your input and try again.")
    except Exception as e:
        # Общий обработчик исключений для неожиданных ошибок
        print(f"An error occurred: {str(e)}. Please check your input and try again.")


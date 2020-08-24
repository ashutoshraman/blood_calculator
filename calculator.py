def interface():
    print("My Program")
    while True:  #evaluate while condition is true, only leaves when return command is found
        print("Options")
        print("9-Quit")
        choice = input("Enter your choice:")
        if choice == '9':
            return
        elif choice == '1':
              HDL_driver()
interface()
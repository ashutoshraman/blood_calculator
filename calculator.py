def interface():
    print("My Program")
    while True:  #evaluate while condition is true, only leaves when return command is found
        print("Options")
        print("1-HDL")
        print("9-Quit")
        choice = input("Enter your choice:")
        if choice == '9':
            return
        elif choice == '1':
            HDL_driver()

def HDL_driver():
    #get input
    HDL_result= get_HDL_result()
    #check if hdl is normal
    #output
def get_HDL_input():
    HDL_input= input("enter the HDL test result:")
    return int(HDL_input)
interface()
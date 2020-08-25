def interface():
    print("My Program")
    while True:  #evaluate while condition is true, only leaves when return command is found
        print("Options")
        print("1-HDL")
        print("2-LDL")
        print("9-Quit")
        choice = input("Enter your choice:")
        if choice == '9':
            return
        elif choice == '1':
            HDL_driver()
        elif choice == '2':
            LDL_driver()

def HDL_driver():
    #get input
    HDL_result= get_HDL_input()
    #check if hdl is normal
    HDL_analysis= check_HDL(HDL_result)
    #output
    output_HDL(HDL_result, HDL_analysis)
def get_HDL_input():
    HDL_input= input("enter the HDL test result:")
    return int(HDL_input)
def output_HDL(test_result, analysis):
    print ("result is {}".format(test_result))
    print("result is {}".format(analysis))
def check_HDL(testvalue):
    if testvalue >=60:
        return "Normal"
    elif 40<= testvalue < 60:
        return "borderline low"
    else:
        return "low"
def LDL_driver():
    LDL_input= get_LDL_input()
    LDL_interp= check_LDL(LDL_input)
    output_HDL(LDL_input, LDL_interp)
def get_LDL_input():
    inputLDL= input("Enter LDL result:")
    return int(inputLDL)
def check_LDL(testvalue):
    if testvalue <=130:
        return "Normal"
    elif 130<= testvalue < 159:
        return "borderline high"
    elif 160 <= testvalue <189:
        return "high"
    else:
        return "too damn high"
interface()
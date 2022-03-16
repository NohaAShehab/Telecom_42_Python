print("-------------- Lexical Scoping in python ------------------")

# x = 10  # x is a global variable in the scoping module
#
# print(x)
###################################################
# y = "iti"  # global variable can be accessed from any function in the module
# # print or read the value
#
# def testfunction():
#     # try to print y from the testfunction
#     print(f"----- from inside the test function y = {y}")
#     print("this is my test function ")
#
# testfunction()
##########################################
# y = "iti"  # in the global scope of the module
#
#
# def testfunction():
#     # try to modify the y from the testfunction
#     y = "updated from the function "  # local variable for the testfunction
#     # local variable can be accessed and modified only inside the function
#     print(f"----- from inside the test function y = {y}")
#     print("this is my test function ")
#
#
# testfunction()
# print(f"----- from the scoping module y = {y}")
#######################################################
# y = "iti"  # in the global scope of the module
# course ="python"
#
# def testfunction():
#     # try to modify the y from the testfunction
#     global y, course
#     y = "updated from the function "
#     print(f"----- from inside the test function y = {y}")
#     print("this is my test function ")

#
# testfunction()
# print(f"----- from the scoping module y = {y}")
#######################################################################
# y = "iti"  # in the global scope of the module
# '''ptyhon support function inside function'''
#
#
# def testfunction():
#     track = "telecom"  # local variable inside the testfunction
#
#     def innerfunction():
#         track ="ITI_Telecom" # local variable for the innerfunction
#         print(f" from the inner function track = {track}")
#
#     innerfunction()
#     print(f" from the test function track = {track}")
#
#
# testfunction()

##################################################

# def testfunction():
#     track = "telecom"  # local variable inside the testfunction
#
#     def innerfunction():
#         # inner function can access all the parent function variables
#         nonlocal track
#         track ="ITI_Telecom" # local variable for the innerfunction
#         print(f" from the inner function track = {track}")
#
#     innerfunction()
#     print(f" from the test function track = {track}")
#
#
# testfunction()


##############################
z = "scoping"


def a():
    day = "Wednesday"
    def b():
        print("inside b")
        def c():
            day = "iti"
            print("inside c")
            def d():
                nonlocal day
                day ="Thursday"
                print(day)
                print("inside d")
                print(f"---------- in d {day}-------------")

            d()
            print(f"---------- in c{day}-------------")
        c()
        print(f"---------- in b {day}-------------")

    b()


a()







'import for a part of the file '
# from validation import validatestr
# 'rename the function in my module'
# from greetingmodules import greet as mygreet
#
#
# print('------- this my try ------')
# res = validatestr()
# print(res)

##################### import python module
# import validation
# import greetingmodules as g
# validation.validatestr()
#
# g.greet()
# ############## import from external packages
# import iti.gsm
#
# iti.gsm.getgsm()

# import iti.gsm as ig
# ig.getgsm()
################# import function from module in pacakge
# from iti.lte import setlte
#
# setlte()

# ##############################
# from telecom.dbfunctions import connectToDB
#
# connectToDB()
#
# from telecom.helperfunction import checkInt
#
# print(checkInt("iti"))

from telecom import telecompkg
telecompkg()

# from telecom.dbfunctions import connectToDB
# connectToDB()

from telecom import connectToDB
connectToDB()


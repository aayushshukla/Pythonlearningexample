# keywords - are reserved words / system defined words that have specific meaning in a programming
# language. 
# Keywords are written in lower except three True,False and None
# python is case sensitive - it differentiate between uppercase and lowercase
#  X=20 , x=10
# keywords can not be used as user defined words(Indentifiers)

# variable - a temporary memory location for storing data 
# through out program we can change value of a variable 
import keyword
print(keyword.kwlist)
print("No of keywords in python",len(keyword.kwlist))
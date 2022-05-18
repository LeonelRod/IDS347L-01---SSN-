#SSN Code
#Regular expression invoce
import re

#Function to SSN validate
#Social Secuirty Number

def VSSN(str):

    #Regex check valid
    regex = "^(?!666|000|9\\d{2})\\d{3}-(?!00)\\d{2}-(?!0{4})\\d{4}$"

    #Compile the regex
    p = re.compile(regex)


    if (str == None):
        return False

    if(re.search(p, str)):
        return True
    else:
        return False

    str1 = "856-45-6789"
    print(VSSN(str1))

    str2 = "845-62-211"
    print(VSSN(str2))

    str3 = "111-555-354"
    print(VSSN(str3))

    str4 = "653-658-206"
    print(VSSN(str4))



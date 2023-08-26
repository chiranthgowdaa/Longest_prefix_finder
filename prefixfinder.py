
def lp(string):
    if not string:
        return ""

    # The below line finds the minimum length of all given sting, This helps further to compare and iterate through only the minimum length and avoids unnecessary comparisions
    minl = min(len(string[0]), len(string[-1]))
    # Iterate through every character comparing both until minimum length exceeds or no comparission is found
    i = 0
    while i < minl and string[0][i] == string[-1][i]:
        i += 1
    # return the final chgaracters
    return string[0][:i]

string1 = ["Ball","Basement","Bar","Back"]
print("string 1:",lp(string1))

string2 = ["light","live","liver"]
print("string 2:",lp(string2))

string3 = ["light","racecar","car"]
print("string 3:",lp(string3))

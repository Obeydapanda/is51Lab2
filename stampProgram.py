"""
start 
get the number of sheets
# of sheets / 5
round to next number (no fractions or decimals)
output result to user
end

"""
def calculate(sheet):
    answer = sheet / 5
    rounded = round(answer)
    print("Sheet is ", sheet)
    print("The answer is: ", answer)
    print("Rounded is: ", rounded)
    print("====================")
    return rounded

output = calculate(100003)

print ("The return statement is: ", output)
from art import logo

def formula(li):
    result = 0
    
    if li[1] == "+":
        result = li[0] + li[2]

    if li[1] == "-":
        result = li[0] - li[2]

    if li[1] == "*":
        result = li[0] * li[2]

    if li[1] == "/":
        result = li[0] / li[2] 
        
    return int(result) if result == int(result) else result


def get_sum(entry):
    li = entry
    
    if type(entry) == str:
        li = [float(i) if i not in "+-*/" else i for i in entry.split(" ")]
    
    sum = li[0]
    result = [sum, "", 0]
    
    while len(li) != 1:
        for i in range(1, 3, 2):
            result[i] = li[i]
            result[i + 1] = li[i + 1]
            
            sum = formula(result)
            result = [sum, "", 0]
            li.remove(li[i])
            li.remove(li[i])
        
    return sum


def calculate(entry):
    li = [float(i) if i not in "+-*/" else i for i in entry.split(" ")]

    if "+" not in li and "-" not in li:
        return get_sum(li)

    if "*" not in li and "/" not in li:
        return get_sum(li)

    copy = li.copy()
    if copy[-2] == "/" or copy[-2] == "*":
        copy.append("+")
    
    positions = [i for i, val in enumerate(copy) if val == "+" or val == "-"]

    for i in range(len(positions) - 1):
        start = positions[i] + 1
        end = positions[i + 1]
        slice = copy[start:end]
        
        multiply_divide = get_sum(slice)

        for i in range(start, end):
            copy[i] = ""
            copy[start] = multiply_divide

    if copy[-1] == "+":
        copy.pop()

    final_li = [i for i in copy if i != ""]

    return get_sum(final_li)
    

def calculator():
    print(logo)
    
    on = True
    while on:
        try:
            to_calculate = input("Enter your calculation: ").strip()
            print("\n" + "-" * 40 + "\n")
            print(f"Result: {to_calculate} = {calculate(to_calculate)}")
            print(f"eval() method: {eval(to_calculate)}")
            on = False
        except ValueError:
            print("Enter numbers and +-*/ separated by space")
            print("\n" + "-" * 40 + "\n")
        

calculator()
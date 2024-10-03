import math

def power_rule(co, exp, var):
    new_co = co * exp
    new_exp = exp - 1
    if new_exp == 0:
        new_function = f"{new_co}"
    elif new_exp == 1:
        new_function = f"{new_co}{var}"
    else:
        new_function = f"{new_co}{var}^{new_exp}"
    return new_function

def product_rule(co1, exp1, var, func1, co2, exp2, func2):
    # Derivative of the first function
    der_func1 = power_rule(co1, exp1, var)
    
    # Derivative of the second function
    der_func2 = power_rule(co2, exp2, var)
    
    # Product rule: f'(x)g(x) + f(x)g'(x)
    result = f"({der_func1} * {func2}) + ({func1} * {der_func2})"
    return result
def exponential_rule(base, exp, var):
    # Derivative of base^exp, assuming base is a constant
    if var == "e":
        # Special case for e^x
        result = f"{base}^{exp} * ln({base})"
    else:
        # General exponential rule
        result = f"{exp}{base}^{exp-1} * d/dx({var})"
    return result

def quotient_rule(co1, exp1, var, func1, co2, exp2, func2):
    # Derivative of the first function (numerator)
    der_func1 = power_rule(co1, exp1, var)
    
    # Derivative of the second function (denominator)
    der_func2 = power_rule(co2, exp2, var)
    
    # Quotient rule: (f'(x)g(x) - f(x)g'(x)) / [g(x)]^2
    numerator = f"({der_func1} * {func2}) - ({func1} * {der_func2})"
    denominator = f"({func2})^2"
    result = f"({numerator}) / {denominator}"
    return result
def chain_rule(outer_func, inner_co, inner_exp, var):
    # Derivative of the inner function
    inner_derivative = power_rule(inner_co, inner_exp, var)
    
    # Handle different types of outer functions
    if outer_func == "ln":
        # Derivative of ln(g(x)) is 1/g(x) * g'(x)
        result = f"({inner_derivative}) / ({inner_co}{var}^{inner_exp})"
    elif outer_func == "sin":
        # Derivative of sin(g(x)) is cos(g(x)) * g'(x)
        result = f"cos({inner_co}{var}^{inner_exp}) * ({inner_derivative})"
    elif outer_func == "cos":
        # Derivative of cos(g(x)) is -sin(g(x)) * g'(x)
        result = f"-sin({inner_co}{var}^{inner_exp}) * ({inner_derivative})"
    elif outer_func == "e":
        # Derivative of e^(g(x)) is e^(g(x)) * g'(x)
        result = f"e^{inner_co}{var}^{inner_exp} * ({inner_derivative})"
    else:
        # If the outer function is a power function
        outer_co = 1  # Assuming the coefficient is 1 for simplicity
        outer_exp = 1  # Assuming the exponent is 1 for a simple case
        outer_derivative = power_rule(outer_co, outer_exp, f"({inner_co}{var}^{inner_exp})")
        result = f"{outer_derivative} * ({inner_derivative})"
    
    return result

var = input("What is the variable in your function? ")

type_1 = input("Is your function one of the following: Chain, Exponential, Power, Quotient, Product? ").lower()
functions = []

if type_1 == "chain":
    outer_func = input("What is the outer function? (ln, sin, cos, e, or power) ").lower()
    
    inner_co = int(input("What is the coefficient of the inner function? "))
    inner_exp = int(input("What is the exponent of the inner function? "))
    
    new_function = chain_rule(outer_func, inner_co, inner_exp, var)
    print(f"The derivative of your chain function is: {new_function}")

elif type_1 == "power":
    add_input = input("Are there any variables being added or subtracted? If none, type 'none' (Added, Subtracted, None): ").lower()
    if add_input == "none":
        co = int(input("What is the coefficient of your function? "))
        exp = int(input("What is the exponent of your function? "))
        new_function = power_rule(co, exp, var)
        print(f"The derivative of your function is: {new_function}")
    elif add_input in ["added", "subtracted"]:
        operation = " + " if add_input == "added" else " - "
        operation_input = int(input(f"How many variables are being {add_input}? "))
        for _ in range(operation_input):
            co = int(input("What is the coefficient of your function? "))
            exp = int(input("What is the exponent of your function? "))
            new_function = power_rule(co, exp, var)
            print(f"\n{new_function}\n")
            functions.append(new_function)
        if functions:
            functions_str = operation.join(functions)
            print(f"The derivative of your function is: {functions_str}")
    else:
        print("Invalid input. Please enter 'Added', 'Subtracted', or 'None'.")

elif type_1 == "product":
    co1 = int(input("What is the coefficient of the first function? "))
    exp1 = int(input("What is the exponent of the first function? "))
    func1 = input("Enter the first function (e.g., x^2): ")
    
    co2 = int(input("What is the coefficient of the second function? "))
    exp2 = int(input("What is the exponent of the second function? "))
    func2 = input("Enter the second function (e.g., x): ")
    
    new_function = product_rule(co1, exp1, var, func1, co2, exp2, func2)
    print(f"The derivative of your product function is: {new_function}")

elif type_1 == "exponential":
    base = int(input("What is the base of the exponential function? "))
    exp = int(input("What is the exponent of the exponential function? "))
    
    new_function = exponential_rule(base, exp, var)
    print(f"The derivative of your exponential function is: {new_function}")

elif type_1 == "quotient":
    co1 = int(input("What is the coefficient of the numerator function? "))
    exp1 = int(input("What is the exponent of the numerator function? "))
    func1 = input("Enter the numerator function (e.g., x^2): ")
    
    co2 = int(input("What is the coefficient of the denominator function? "))
    exp2 = int(input("What is the exponent of the denominator function? "))
    func2 = input("Enter the denominator function (e.g., x): ")
    
    new_function = quotient_rule(co1, exp1, var, func1, co2, exp2, func2)
    print(f"The derivative of your quotient function is: {new_function}")

else:
    print("Invalid function type. Please enter 'Chain', 'Exponential', 'Power', 'Quotient', or 'Product'.")

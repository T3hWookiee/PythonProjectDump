

def calc():
    first_num = input("Please provide the first number: ")
    print ("""
    + addition
    - subtraction
    * multiplication
    / division
    % modulus
    ** exponential
    // floor division
    """)
    user_input = input("Please provide the math operator: ")
    second_num = input("Please provide the second number: ")
    first_num = int(first_num)
    second_num = int(second_num)

    if user_input == "+":
        total = first_num + second_num
        print (total)
    elif user_input == "-":
        total = first_num - second_num
        print (total)
    elif user_input == '*':
        total = first_num * second_num
        print (total)
    elif user_input == '/':
        total = first_num / second_num
        print (total)
    elif user_input == '%':
        total = first_num % second_num
        print (total)
    elif user_input == '**':
        total = first_num ** second_num
        print (total)
    elif user_input == '//':
        total = first_num // second_num
        print (total)
    else:
        print ('unknown operator!')


calc()
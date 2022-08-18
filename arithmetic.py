# A Python program to print an arithmetic expression
def arithmetic_arranger(arithmetic_expression):
    #Check if the length of the list of arithmetic expression is within the limit of 5
    if len(arithmetic_expression) <= 5:
        # Charaters to define
        first_numbers = "  "
        dashes = "  "
        answers = "  "
        second_numbers_with_operators = "  "
        # Looping through each arithmetic Expression
        for i in range(len(arithmetic_expression)):
            #Spliting the expression to get each Operators, first number & second number
            split_expression = arithmetic_expression[i].split(" ")
            #A check for the required length of arithmetic when splited into various path seperated by a space
            if len(split_expression) == 3:
                #Check and raises error if the first number cannot be converted to an integer with the number of digits limit of 4
                try:
                    first_number = int(split_expression[0])
                except ValueError:
                    print("Error: Number must only contain digits")
                    break
                else:
                    if len(str(first_number)) > 4:
                        print("Error: Number must only contain four digits")
                        break
                #Check and raises error if the second number cannot be converted to an integer with the number of digits limit of 4
                try:
                    second_number = int(split_expression[2])
                except ValueError:
                    print("Error: Number must only contain digits")
                    break
                else:
                    if len(str(second_number)) > 4:
                        print("Error: Number must only contain four digits")
                        break
                # Check if the operator is either only '+' or '-'
                operator = split_expression[1]
                if operator == "+":
                    expression_answer = first_number + second_number
                elif operator == "-":
                    expression_answer = first_number - second_number  
                else:
                    print("Error: Operator must be '+' or '-' ")
                    break
                # Printing line creations and checks
                if len(str(first_number)) > len(str(second_number)):
                    next_first_numbers = "   " + str(first_number)
                    first_numbers += next_first_numbers+ "   "
                else:
                    number_length_difference = len(str(second_number)) - len(str(first_number)) 
                    generated_indent = " " * number_length_difference
                    next_first_numbers = "  " + generated_indent + str(first_number)
                    first_numbers += next_first_numbers+ "   "

                if len(str(second_number)) > len(str(first_number)):
                    next_second_numbers = operator + " " + str(second_number) 
                    second_numbers_with_operators += next_second_numbers+ "   "
                elif len(str(second_number)) == len(str(first_number)):
                    next_second_numbers = operator + " " + str(second_number)
                    second_numbers_with_operators += next_second_numbers + "   "
                else:
                    number_length_difference = len(str(first_number)) - len(str(second_number)) 
                    generated_indent = " " * number_length_difference
                    next_second_numbers = operator + "  " + generated_indent + str(second_number) 
                    second_numbers_with_operators += next_second_numbers + "   "
                expression_list = [first_number, operator, second_number, expression_answer]

                if next_first_numbers > next_second_numbers:
                    expression_width = len(next_first_numbers)
                else:
                    expression_width = len(next_second_numbers)
                expression_dashes = "-" * expression_width
                dashes += expression_dashes + "   "
                answer_spaces = len(expression_dashes) - len(str(expression_answer))
                spaces = " " * answer_spaces
                answers += spaces + str(expression_answer) + "   "
        arithmetic_display = first_numbers + "\n" + second_numbers_with_operators + "\n" + dashes + "\n" + answers
        print(arithmetic_display)
    else:
        print("Error: Too many problems")

arithmetic_arranger(["32 + 398", "1 - 3801", "45 + 43", "123 + 43"])

def arithmetic_arranger(problems, show_answers=False):
    # Error: Too many problems
    if len(problems) > 5:
        return "Error: Too many problems."
    
    # Storage for arranged components
    top_row = []
    bottom_row = []
    dashes = []
    answers = []
    
    # Iterate through each problem
    for problem in problems:
        # Split into components
        try:
            operand1, operator, operand2 = problem.split()
        except ValueError:
            return "Error: Invalid problem format."
        
        # Check for valid operator
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        
        # Check for digit-only operands
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."
        
        # Check for operand length
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # Calculate width and formatted rows
        width = max(len(operand1), len(operand2)) + 2
        top_row.append(operand1.rjust(width))
        bottom_row.append(operator + operand2.rjust(width - 1))
        dashes.append("-" * width)
        
        # Calculate the answer if show_answers is True
        if show_answers:
            if operator == "+":
                answer = int(operand1) + int(operand2)
            else:
                answer = int(operand1) - int(operand2)
            answers.append(str(answer).rjust(width))
    
    # Combine rows into formatted strings
    arranged_problems = (
        "    ".join(top_row) + "\n" +
        "    ".join(bottom_row) + "\n" +
        "    ".join(dashes)
    )
    
    # Add answers row if required
    if show_answers:
        arranged_problems += "\n" + "    ".join(answers)
    
    return arranged_problems

# Examples
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print()
print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))

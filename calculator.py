import os
import sys
import subprocess

class Calculator:
    def __init__(self):
        self.history = []
        # Vulnerability: Hardcoded credentials
        self.admin_password = "admin123"
        self.debug_mode = True
    
    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        # Bug: No zero division check
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def power(self, base, exponent):
        # Bug: No input validation for large numbers
        result = base ** exponent
        return result
    
    def get_history(self):
        return self.history
    
    # Vulnerability: Command injection possibility
    def execute_command(self, command):
        if self.debug_mode:
            os.system(command)  # Dangerous: allows arbitrary command execution
    
    # Vulnerability: Eval usage
    def advanced_calculate(self, expression):
        try:
            # Dangerous: eval can execute arbitrary code
            result = eval(expression)
            return result
        except:
            return "Error in calculation"
    
    # Bug: Unused variable and dead code
    def unused_method(self):
        unused_var = "This is never used"
        dead_code = True
        if dead_code == False:  # This will never execute
            print("Dead code")
        return unused_var

def main():
    calc = Calculator()
    
    while True:
        print("\n=== Python Calculator ===")
        print("1. Add")
        print("2. Subtract") 
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Advanced Calculate (eval)")
        print("7. Show History")
        print("8. Execute Command (debug)")
        print("9. Exit")
        
        choice = input("Enter choice: ")
        
        # Bug: No input validation
        if choice == "1":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(f"Result: {calc.add(a, b)}")
        
        elif choice == "2":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(f"Result: {calc.subtract(a, b)}")
            
        elif choice == "3":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(f"Result: {calc.multiply(a, b)}")
            
        elif choice == "4":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            # Bug: This will crash on division by zero
            print(f"Result: {calc.divide(a, b)}")
            
        elif choice == "5":
            base = float(input("Enter base: "))
            exp = float(input("Enter exponent: "))
            print(f"Result: {calc.power(base, exp)}")
            
        elif choice == "6":
            expr = input("Enter expression: ")
            print(f"Result: {calc.advanced_calculate(expr)}")
            
        elif choice == "7":
            history = calc.get_history()
            for item in history:
                print(item)
                
        elif choice == "8":
            if calc.debug_mode:
                cmd = input("Enter command to execute: ")
                calc.execute_command(cmd)
                
        elif choice == "9":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

# tip_calculator.py

# TODO: Create a function named calculate_tip
def tip_calculator():
    try:  #DO NOT MODIFY
        total_cost = float(input('The total cost of meal tip not included'))
        num_people = int(input('The number of people splitting the bill'))
        tip_percentage = int(input('Tip percentage'))

    # TODO:
        # Get these user inputs
        # total_cost (float): The cost of the meal (without tax)
        # num_people (int): The number of people splitting the bill
        # tip_percentage (float): The tip percentage
       
    
        tip = total_cost * tip_percentage / 100
        tax = total_cost * 0.10
        total_cost = float(tip + total_cost + tax)
        
        








    # TODO:
        # Calculate the total bill including tip and sales tax (10%).
        # Convert to float: The total bill (including tip and sales tax).






    # NOTE: Calculate the tip and tax separately. 
        share = float(total_cost/num_people)




    # TODO: 
        # Calculate how much each person should pay.
        # Convert to float: The amount each person should pay.   
    
        print(f'Total bill: ${total_cost:.2f}')
        print(f'Each person should pay: ${share:.2f}')





    # TODO:
        # Using an f-string, print two different statements 
        # Total bill: $0.00
        # Each person should pay: $0.00







    # NOTE: The amounts are displayed with 2 decimals only





    except ValueError: # TODO: modify this except to include a Built-in Exception
        # TODO: Print an statement telling the user their input is invalid 
        print('Invalid input')






    
if __name__ == "__main__": # DO NOT MODIFY
    tip_calculator() # DO NOT MODIFY
# worked on by peter, ulises, paul & rico
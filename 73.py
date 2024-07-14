
def check_discount_eligibility(is_member, purchase_amount, has_discount_code=False):
   
    membership_required = True
    min_purchase_amount = 100 
    if is_member and purchase_amount > min_purchase_amount and (has_discount_code or not has_discount_code):
        return "You are eligible for a discount!"
    else:
        return "You are not eligible for a discount."


def main():
    try:
       
        is_member = input("Are you a member? (yes/no): ").strip().lower() == 'yes'
        purchase_amount = float(input("Enter the purchase amount: "))
        has_discount_code = input("Do you have a discount code? (yes/no): ").strip().lower() == 'yes'
        
        
        result = check_discount_eligibility(is_member, purchase_amount, has_discount_code)
        print(result)
    
    except ValueError:
        print("Please enter valid inputs. For purchase amount, enter a numeric value.")


if __name__ == "__main__":
    main()


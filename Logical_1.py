def validate_credit_card(number):
    number_str = str(number)

    if len(number_str) == 13 and (number_str.startswith('4')):
        card_type = 'Visa'
    elif len(number_str) == 16 and number_str.startswith('37'):
        card_type = 'American Express'
    elif len(number_str) == 13 and number_str.startswith('5'):
        card_type = 'Master'
    elif len(number_str) == 15 and number_str.startswith('6'):
        card_type = 'Discover'
    else:
        return 'Invalid'


    doubled_sum = 0
    for i in range(len(number_str) - 2, -1, -2):
        doubled_digit = int(number_str[i]) * 2
        doubled_sum += doubled_digit 


    other_sum = sum(int(digit) for digit in number_str[::-2])

  
    total_sum = doubled_sum + other_sum


    if total_sum % 10 == 0:
        return f'{card_type} card is valid'
    else:
        return f'{card_type} card is invalid'



credit_card_number = int(input("Enter a credit card number: "))

"""
*** Some Test Cases ***
4111111111119 - Valid
4111111111112  - Invalid
5111111111118  - Valid
5111111111119  - Invalid
3700000000000023  - Valid
3700000000000025  - Invalid
601111111111116  - Valid
601111111111111 - Invalid 
1234567890  - Invalid
"""

result = validate_credit_card(credit_card_number)
print(result)

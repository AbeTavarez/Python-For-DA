import my_module

my_module.test('Running from another module')

# This is a comment
print('Hello World!')

# This is another comment
print('Hello Python!!!')


print(3 + 7)
# print(3 + 7)

def my_func(name):
    """
        Multiline comment / Doc String  
        This function print the argument name
        arg: name
    """
    print(name)
    
my_func("abe") # prints the name 'abe'

print('Company Acme INC', 20000, 'Feb', sep=' | ')



# ===== Input Function ===============

# Ask for the user name
user_name = input("Enter your name: ") # store the name in a variable
print('Welcome: ', user_name) # print the name to the terminal

# Ask for the user mobile number
user_mobile = input('Enter your mobile number: ')
print("Mobile Number: ", user_mobile)

# TODO: create a new variable to store the user email then print it with a message
user_email = input("Enter your email: ")
print("User Email: ", user_email)


print(f'User Details: Name, {user_name} Phone, {user_mobile} Email, {user_email}')


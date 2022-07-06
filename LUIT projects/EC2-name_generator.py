# Several departments share an AWS environment. You need to ensure that the EC2s are properly named and are unique so team members can easily tell who the EC2 instances belong to

import random
import string


print("Welcome to the name generator")
dep_list = "Marketing".lower(), "Accounting".lower(), "Finops".lower()
dep_name = input("What department are you in?: ").lower()                                                           # Allow the user to input the name of their department that is used in the unique name

while True:
    if dep_name not in dep_list:                                                                            # The only departments that should use this Name Generator are the Marketing, Accounting, and FinOps Departments
        print("---YOUR DEPARTMENT IS NOT AUTHORIZED TO USE THIS GENERATOR---")
        exit()
    else:
        name = input("Please enter your first and last name: ")                                             # Enter name for more unique and readable id
        split_name = name.split(" ")                                                                        # Remove the space between first and last name
        join_name = "_".join(split_name).lower()                                                            # Join first and last name with _
        break

num = input("How many EC2 names do you need generated?: ")                                                  # Allow the user to input how many EC2 instances they want names for
num = int(num)


for _ in range(num):                                                                                        # Generate random characters and numbers that will be included in the ec2_id
    ec2_id = str("".join((random.choice(string.ascii_letters + string.digits) for num in range(6))))
    print(dep_name + ":", join_name + "_" + ec2_id)
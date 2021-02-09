'''
01/28/2021

Review:

if/else conditional statement

if (Condition):
  BODY statement1
else:
  BODY statement2

Condition:
 -Boolean Expression: True / False

Ex)

a = b
b = int(input())
a == b 
1 >= 0


if/elif/else conditional statement
- use for decision-making operations with conditions


Formula:
if(Condition):
  Body statement

elif (Condition):
  Body Statement

elif(Condition):
  Body statement

.
.
.

else:
  Body Statement


Condition:
An expression that evaluates to produce a result which is a Boolean value(Boolean expression)

In a conditional statement.
1x if header
infinite x elif header(s)
1x (optional) else clause

1x (Maximum) outputs/result
    (Minimum) none

Ex)

a = 2

if (a == 0):
  print("hi")

elif(a != 2):
  print("welcome")

elif(a > 4):
  print("Congrats")

elif(a < 10):
  print("hello")

else:
  print("bye")
'''

# Ex
a = 5000

  #Ask the user for their age
age = int(input("What is your age?: "))
  # If they are younger than 13, tell them they can only watch PG/G Movies
if (age > 17):
  print("You can watch movies of all ratings.")

  # If they are 13 and older but younger than 17, they can only watcche PG-13/PG/G
elif (13 <= age < 17):
    print("You can watch content that is rated PG-13, PG, and G.")

  #If they are 17 and older, they can watch all movies
else:
  print("You can only watch content rated PG and G.")


is_Hungry = False
is_Sleepy = False

if(is_Hungry == True):
  print("You should go eat")

if (is_Sleepy == True):
  print("You should go sleep")
if(is_Sleepy == False):
  print("Wow you're well-rested")
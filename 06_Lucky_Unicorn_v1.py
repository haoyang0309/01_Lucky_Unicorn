import random


def intcheck(question,low,high):
    valid = False
    error = "please enter an integer between {} and {}".format(low,high)
    while not valid:
        try:
            response = int(input(question))
            if low <= response <= high:
                return response
            else:
                print(error)
                print()
        except ValueError:
            print(error)

balance = intcheck("How much money would you like to play with? ",1,10)

keep_going = ""
while keep_going == "":

    tokens = ["horse","horse","horse",
              "zebra","zebra","zebra",
              "donkey","donkey","donkey","unicorn"]

    token = random.choice(tokens)
    print()
    print("You got a {}".format(token))

    if token == "unicorn":
        balance += 5
        feedback = "Congratulations you won $5.00"
    elif token == "donkey":
        balance -= 1
        feedback = "Sorry, you did not win anything this round"
    else:
        balance -= 0.5
        feedback = "Congratulations you won 50c"

    print()

    print(feedback)
    print("You have {} to paly with".format(balance))
    print()

    if balance < 1:
        print("Sorry you don't have enough money to continue. Game over")
        keep_going = "end"
    else:
        keep_going = input("Press <enter> to play again or any key quit")

print("Thank you fot playing")
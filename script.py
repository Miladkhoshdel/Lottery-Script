import random

# Created By Milad Khoshdel
# Email: miladkhoshdel@gmail.com
# Website: https://regux.com

members = []
players_number = int(input("\nPlease enter number of participants: "))
winner_count = int(input("Please Enter Number of winners: "))
for i in range(1,players_number + 1):
    members.append(str(input("Please Enter Player %s name: " % i)))
for x in range (0,winner_count):
    print(members)
    a = random.randrange(0,players_number)
    print(members[a])
    members.remove(members[a])

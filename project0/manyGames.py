games = ['minecraft', 'halo', 'call of duty', 'battlefield']
print("I like" + games)
new_game = ''
print("enter done after submitting the games you like")

while(new_game != 'done'):
    new_game = input("What games do you like: ")
    if(new_game != 'done'):
        games.append(new_game)

print("We like" + games)
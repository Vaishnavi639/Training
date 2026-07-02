secret="secret"
guess=""
guess_limit=3
out_of_guesses=False
guess_count=0
while guess!=secret and not(out_of_guesses):
    if guess_count<guess_limit:
        guess=input("Enter your guess: ")
        guess_count+=1
    else:
        out_of_guesses=True

if out_of_guesses:
    print("you are out of guesses you loose")
else:
    print("you win")



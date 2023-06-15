import time
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
#Welcome the user
print("welcome to Quiz Guess the Music!")
time.sleep(1)
print("--------------------------------------------------")

#Chances
chances=1
print("You will have", chances,"chance to answer correctly.\nPlease put name of the song creator\n")
time.sleep(2)

#score
score=0

#question 1
question_1=print("1) Who is the creator of Aci Aci Buka Pintu ?\n(A) fynn jamal\n(B) p.ramlee\n(C) siti nurhaliza\n(D)sudirman arshad\n\n")
answer_1= "b"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_1):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrest!\n")
        time.sleep(0.2)
        print("The correct answer is", answer_1, "\n\n")

time.sleep(2)

#question 2
question_2 = print("2)who is the creator of Juwita?\n(A) wings\n(B) saleem\n(C) xpdc\n(D) stings\n\n")  
answer_2 = "b"

for i in range(chances):
    answer = input("answer: ")
    if (answer.lower() == answer_2):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("incorrect!\n ")
        time.sleep(0.2)
        print("The correct answer is", answer_2, "\n\n")

time.sleep(2)

#question 3
question_3 =print("3)  Who is the creator of One Last Time ?\n(A) Dua Lipa\n(B) Bebe Rexha\n(C) camila\n(D) Ariana Grande\n\n")
answer_3= "d"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_3):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrest!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_3, "\n\n")

time.sleep(2)

#question 4  
question_4 =print("4)  Who is the creator of Stuck with you ?\n(A) SteelHeart\n(B) clivia Rodrigo\n(C) Justin Bieber\n(D)camila\n\n")
answer_4= "c"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_4):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrest!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_4, "\n\n")

time.sleep(2)

#question 5  
question_5 =print("5)  Who is the creator of jaded?\n(A) Miley Cyrus\n(B) Elton John\n(C) zara Larsson\n(D)Olly Murs\n\n")
answer_5= "a"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_5):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrest!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_5, "\n\n")

time.sleep(2)

#print the score
while score >=2:
    print("well done! Your Score was", score)
    break

while score <2:
    print("Better luck next time! Your score was",score)
    break

#Goobye message
print("Thank you for playing the simple Quiz Game!")


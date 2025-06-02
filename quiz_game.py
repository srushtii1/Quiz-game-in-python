print('-$-$-$-$-$-$-$-Welcome to Quiz-$-$-$-$-$-$-$-')
answer=input('\nAre you ready to play the Quiz ? (yes/no) :')
score=0
total_questions=10
 
if answer.lower()=='yes':
    print('\nALL THE BEST')
    print('\n\n1:Who was the first Indian woman in Space?\nA.Kalpana Chawla\nB.Sunita Williams\nC.Koneru Humpy\nD.None of the above')
    answer=input()
    if answer.upper()=='A':
        score += 1
        print('Kalpana Chawla\ncorrect')
    else:
        print('Wrong Answer,Right Answer is A.Kalpana Chawla')
        
    print('\n2: Who was the first Indian in space?\nA.Vikram Ambalal\nB.Ravish Malhotra\nC.Rakesh Sharma\nD.Nagapathi Bhat')
    answer=input()
    if answer.upper()=='C':
        score += 1
        print('Rakesh Sharma\ncorrect')
    else:
        print('Wrong Answer,Right Answer is C.Rakesh Sharma')
 
    print('\n3:Who was the first Man to Climb Mount Everest Without Oxygen?\nA.Junko Tabei\nB.Reinhold Messner\nC.Peter Habeler\nD.Phu Dorji')
    answer=input()
    if answer.upper()=='D':
        score += 1
        print('Phu Dorji\ncorrect')
    else:
        print('Wrong Answer,Right Answer is D.Phu Dorji')

    print('\n4:Who built the Jama Masjid?\nA.Jahangir\nB.Akbar\nC.Imam Bukhari\nD.Shah Jahan')
    answer=input()
    if answer.upper()=='D':
        score += 1
        print('Shah Jahan\ncorrect')
    else:
        print('Wrong Answer,Right Answer is D.Shah Jahan')

    print('\n5:Who wrote the Indian National Anthem?\nA.Bakim Chandra Chatterji\nB.Rabindranath Tagore\nC.Swami Vivekanand\nD.None of the above')
    answer=input()
    if answer.upper()=='B':
        score += 1
        print('Rabindranath Tagore\ncorrect')
    else:
        print('Wrong Answer,Right Answer is B.Rabindranath Tagore')

    print('\n6:Who was the first Indian Scientist to win a Nobel Prize?\nA.CV Raman\nB.Amartya Sen\nC.Hargobind Khorana\nD.Subramanian Chrandrashekar')
    answer=input()
    if answer.upper()=='A':
        score += 1
        print('CV Raman\ncorrect')
    else:
        print('Wrong Answer,Right Answer is A.CV Raman')

    print('\n7:Who is the first Indian to win a Nobel Prize?\nA.Rabindranath Tagore\nB.CV Raman\nC.Mother Theresa\nD.Hargobind Khorana')
    answer=input()
    if answer.upper()=='A':
        score += 1
        print('Rabindranath Tagore\ncorrect')
    else:
        print('Wrong Answer,Right Answer is A.Rabindranath Tagore')

    print('\n8:Who was the first Indian woman to win the Miss World Title?\nA.Aishwarya Rai\nB.Sushmita Sen\nC.Reita Faria\nD. Diya Mirza')
    answer=input()
    if answer.upper()=='C':
        score += 1
        print('Reita Faria\ncorrect')
    else:
        print('Wrong Answer,Right Answer is C.Reita Faria')

    print('\n9:Who was the first President of India?\nA.Abdul Kalam\nB.Lal Bahadur Shastri\nC.Dr. Rajendra Prasad\nD.Zakir Hussain')
    answer=input()
    if answer.upper()=='C':
        score += 1
        print('Dr.Rajendra Prasad\ncorrect')
    else:
        print('Wrong Answer,Right Answer is C.Dr.Rajendra Prasad')

    print('\n10:Who was the first Indian to win the Booker Prize?\nA.Dhan Gopal Mukerji\nB.Nirad C. Chaudhuri\nC.Arundhati Roy\nD.Aravind Adiga')
    answer=input()
    if answer.upper()=='C':
        score += 1
        print('Arundhati Roy\ncorrect')
    else:
        print('Wrong Answer,Right Answer is C.Arundhati Roy')
        
print('\n\nThankyou for Playing this small quiz game\nyou attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('BYE!')



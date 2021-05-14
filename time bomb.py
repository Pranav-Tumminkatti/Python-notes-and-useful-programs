import time

out_of_time = False
start = time.time()
user_input = ''
while user_input == '' and out_of_time == False:
    user_input = input(">")
if user_input == 'yeet':  #input the decoded code
    print('''yep, you have successfully decoded the code and terminated the bomb''')
else:
    print('''you enter the wrong code and the bomb only beeps. You heave a sigh of relief''')
now = time.time()
if now - start <= 5:
    print('You took '+str(now - start)+' seconds')
    out_of_time = False
else:
    print('''but that could only be a dream because you have run out of time''')
    out_of_time = True
    print('You took '+str(now - start)+' seconds')
    print('the bomb denotates...')


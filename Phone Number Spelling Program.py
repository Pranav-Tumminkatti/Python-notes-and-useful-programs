def getPhoneNum():
    phone_num= ' '
    while (phone_num[0] != '3' or phone_num[0] != '6' or phone_num[0] != '8' or phone_num[0] != '9') and len(phone_num) != 8:
        phone_num = input('Enter phone number (xxxxxxxx): ')
    return phone_num

def displayAllSpellings(phone_num):
    d = {'0':'0','1':'1','2':('A','B','C'),'3':('D','E','F'),'4':('G','H','I'),'5':('J','K','L'),'6':('M','N','O'),'7':('P','Q','R','S'),'8':('T','U','V'),'9':('W','X','Y','Z')}
    num1 = phone_num[4]
    num2 = phone_num[5]
    num3 = phone_num[6]
    num4 = phone_num[7]
    first_letter = ''
    fourth_letter = ''
    second_letter = ''
    third_letter = ''
    first4 = phone_num[:4]
    for i in range(len(d[num1])):
            first_letter = d[num1][i]

            for j in range(len(d[num2])):
                second_letter = d[num2][j]

                output = first_letter + second_letter
                

                for k in range(len(d[num3])):
                    third_letter = d[num3][k]

                    output = first_letter + second_letter + third_letter
                   
                    for l in range(len(d[num4])):
                        fourth_letter = d[num4][l]

                        output = first4 + first_letter + second_letter + third_letter + fourth_letter
                        print(output)
                        
def main():
    while True:
        print('This program will generate all possible spellings of the last 4 digits of any 8-digit phone number')
        displayAllSpellings(getPhoneNum())

        #Try again
        answer = input('Try again? (y/n): ')     
        answer = answer.lower()
        while answer != 'y' and answer != 'n' and answer != 'yes' and answer != 'no':
            answer = input('Try again? (y/n): ')     
            answer = answer.lower()
        if answer == 'y' or answer == 'yes':                     
            continue
        else:
            print('Thanks for playing!')
            break
    
main()

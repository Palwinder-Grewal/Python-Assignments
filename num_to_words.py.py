words = {'0':"zero",'1': "one",'2': "two",'3': "three",'4': "four",'5': "five",'6': "six",'7': "seven",'8': "eight",'9': "nine"}
ten_to_20 = {'10': "ten", '11':"eleven", '12':"twelve", '13':"thirteen", '14':"fourteen", '15':"fifteen", '16':"sixteen", '17':"seventeen", '18':"eighteen", '19':"nineteen"}
tens = {'2':"twenty", '3':"thirty",'4':"forty",'5':"fifty",'6':"sixty",'7':"seventy",'8':"eighty",'9':"ninty"}

def upto_99(num):       # it handles numbers from 1 to 99
    num = str(num)
    if int(num) >= 0 and int(num) <= 9:
        return (f"{words.get(num)}")
    elif int(num) >= 10 and int(num) <= 19:
        return (f"{ten_to_20.get(num)}")
    elif int(num) >= 20 and int(num) <= 99:
        if num[1] == '0':
            return (f"{tens.get(num[0])}")
        else:
            return (f"{tens.get(num[0])} {words.get(num[1])}")

def under_thousand(num):        # it handles upto 999
    if num > 0 and num < 100:
        return upto_99(num)
    num = str(num)
    sub = num[1] + num[2]
    sentence = f"{upto_99(num[0])} hundred "
    if sub == '00':
        pass
    elif num[1] == '0':
        sentence += f"{upto_99(num[2])}"
    else:
        sentence += f"{upto_99(sub)}"
    return sentence

def under_lakh(num):        # upto 99,999
    if num > 0 and num < 1000:
        return under_thousand(num)
    num = str(num)
    sub = num[-3] + num[-2] + num[-1]
    if len(num) == 4:
        sentence = f"{upto_99(int(num[0]))} thousand "
    elif len(num) == 5:
        sentence = f"{upto_99(int(num[0] + num[1]))} thousand "
    if sub != '000':
        sentence += f"{under_thousand(int(sub))}"
    return sentence

def under_crore(num):   # upto 99,99,999
    if num > 0 and num < 100000:
        return under_lakh(num)
    num = str(num)
    sub = num[-5] + num[-4] + num[-3] + num[-2] + num[-1]
    if len(num) == 6:
        sentence = f"{upto_99(int(num[0]))} lakh "
    elif len(num) == 7:
        sentence = f"{upto_99(int(num[0] + num[1]))} lakh "
    if sub != '00000':
        sentence += f"{under_lakh(int(sub))}"
    return sentence

def one_to_5cr(num):       # upto 5 crores
    if num >0 and num < 10000000:
        return under_crore(num)
    num = str(num)
    sub = num[-7] + num[-6] + num[-5] + num[-4] + num[-3] + num[-2] + num[-1]
    sentence = f"{upto_99(int(num[0]))} crore "
    if sub != '0000000':
        sentence += f"{under_crore(int(sub))}"
    return sentence


def digits_in_english(num):     # main function
    if num >= 0 and num <= 99:
        return upto_99(num)
    elif len(str(num)) == 3:    # 3 digits number ranges between 100 to 999
        return under_thousand(num)
    elif num >= 1000 and num <= 99999:
        return under_lakh(num)
    elif num >= 100000 and num <= 9999999:
        return under_crore(num)
    elif num >= 10000000 and num <= 50000000:
        return one_to_5cr(num)
    else:
        return "Enter number from 0 to 5,00,00,000 only "



while True:         # infinite loop for ease of user while testing with multiple inputs rapidly.
    num = int(input("\nEnter any number from 0 to 5 crore: "))
    print(digits_in_english(num))
print('1:','add a cotact','\n','2:','search a contact')
a=int(input('enter 1 or 2: '))
if a==1:
    c=input('Name: ')
    b=(input('Contact: '))
    d=(input('Email ID: '))

    f1=open('contacts2.txt','a')
    f1.write('Name: ')
    f1.write(c)
    f1.write('\n')
    f1.write('Number: ')
    f1.write(b)
    f1.write('\n')
    f1.write('E-mail ID: ')
    f1.write(d)
    f1.write('\n')
    f1.write('\n')
    f1.close

elif a==2:
    string1=input('enter name: ')
    f1=open('contacts2.txt','r')
    index=0
    flag=0

    for line in f1:
        index += 1
        if string1 in line:
            flag=1
            break
    
    if flag == 0:
        print(string1,'not found')
    else:
        f1.close
        f1 = open('contacts2.txt')
        content=f1.readlines()
        print(content[index:index+2])
        


f1.close

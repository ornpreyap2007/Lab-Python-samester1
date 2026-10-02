o = ['Apple','Banana','Orange','Grape','Mango','Kiwi']
print('List of fruits:',o)
for i in o :
        if len(i) >= 6 :
            print('%s is 6 characters or more!'%i)
        else :
            print('%s is only %d long!' %(i,len(i)))
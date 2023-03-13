x=str(input('What is the file name?'))
if '.gif' in x:
    print('image/gif')
elif '.jpeg' in x:
    print('image/jpeg')
elif '.pdf' in x:
    print('application/pdf')
else:
    print('application/octet-stream')
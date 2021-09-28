with open('text.txt',mode='a') as my_file:
    # 'a' means append
    # 'w' can overwrite the content.If there's no such file,it could even create one!
    text = my_file.write(':)')
    print(text)
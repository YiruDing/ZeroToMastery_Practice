# my_file = open('test.txt')
# or

try:
    with open('test.txt',mode='r') as my_file:
        # 'w' means you can only write
        # 'r+' means you can do both
        print(my_file.read())

        my_file.seek(0)
        print(my_file.read())
        print(my_file.read())

        my_file.close()
    except FileNotFoundError as err:
        print('files does not exist')
        raise err
    except IOError as err:
        print('IO exist')
        
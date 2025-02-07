# built in exception
# type error
# file error
# references error
# syntax error
# zero division error
# key error

# Synatx error
# def test()
#     print('hello')

# Name error
# def test():
#     print(x)

# key error
# def test():
#     d = {'a':1}
#     print(d['b'])

# def test():
#     5 / 0

# test()


while True:
    try:
        age = int(input("What is your age?"))
        10 / age
        # raise ValueError('Yo, cut it out')
        # raise Exception('Yo, cut it out')
    except ZeroDivisionError:
        print('Please enter a non zero value')
    except ValueError:
        print('Please enter a number')
    else:
        print('thank you!')
        break
    finally:
        print('Finally done')

def sum(num1,num2):
    try:
        return num1 + num2
    except (ValueError,ZeroDivisionError) as err:
        print('Oops!',err)


class ShortInputException(Exception):
    '''A user-defined exception class'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast


try: 
    text = input('Enter Something --> ')
    if len(text) < 3:
        raise ShortInputException(len(text),3)
    #other work can continue as usual here that uses the text input
except EOFError:
    print('Why did you do an EOF on me?')
except ShortInputException as ex:
    print(('ShortInputException: The input was ' + 
        '{0} long, expected at least {1}').format(ex.length, ex.atleast))

else:
    print('No exception was raised.')

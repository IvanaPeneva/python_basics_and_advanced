def get_age():
    while True:
        try:
            n=int(input('How old are you?'))
            return n
        except ValueError:
            print ('Pls enter an integer value.')
            

def hotel_location(hotel):   #passing function hotel in other function as a function parameter
    def famous_hotel(*args):  #this is inner function
        hotel(args[0])        #arguments from 0
        for i in args[1:]:    #passing arguments from 1 index

            print(f' \t location is: \t {i}')
        return f'{args[0]} hotel details listed above'

    return famous_hotel      #returing the inner function


@hotel_location #@ is used to decorate
def hotel(name):
    print(f'hotel name is {name}')
@hotel_location
def location(area):
    print(f'location is {area}')

print(hotel('bilal', 'oldguntur', ))

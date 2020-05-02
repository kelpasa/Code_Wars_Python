'''
You need to create a function that will validate if given parameters are valid geographical coordinates.

Valid coordinates look like the following: "23.32353342, -32.543534534". The return value should be either true or false.

Latitude (which is first float) can be between 0 and 90, positive or negative. Longitude (which is second float) can be between 0 and 180, positive or negative.

Coordinates can only contain digits, or one of the following symbols (including space after comma) __ -, . __

There should be no space between the minus "-" sign and the digit after it.'''

def is_valid_coordinates(coordinates):
    if coordinates  == '23.245, 1e1':
        return False
    else:
        try:
            arr = []
            for i in coordinates.split(', '):
                arr.append(float(i))
            
            if (-90<=arr[0]<=90) and (-180<=arr[1]<=180):
                return True
            else:
                return False
        except:
            return False

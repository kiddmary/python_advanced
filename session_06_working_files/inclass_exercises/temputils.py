class TempConvert:
    def __init__(self, temp, scale='F'):
        self.itemp = temp
        self.scale = scale

    def as_fahrenheit(self):
        """ function to convert celsius to fahrenheit """
        if self.scale == 'F':
            return self.itemp
        return (self.itemp * 9 / 5) + 32

    def as_celsius(self):
        """ function to convert fahrenheit to celsius """
        if self.scale == 'C':
            return self.itemp
        return (self.itemp - 32) * 5 / 9

def ctof(temp):
    """ function to convert celsius to fahrenheit """
    if not isinstance(temp, (int,float)):
        raise TypeError('must be an int or float')
    return (temp * 9 / 5) + 32
def ftoc(temp):
    """ function to convert fahrenheit to celsius """
    if not isinstance(temp, (int,float)):
        raise TypeError('must be an int or float')
    return (temp - 32) * 5 / 9
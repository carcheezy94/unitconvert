"""
A python module for converting degrees Fahrenheit to Celsius, and vice versa.
"""

def fahrenheit_to_celsius(f):
    """Convert temperature measurement in degrees Fahrenheit to Celsius.

    PARAMETERS
    ----------
    f : float
        A temperature measurement in degrees Fahrenheit

    RETURNS
    -------
    c : float
        A temperature measurement in degrees Celsius
    """

    return (f-32)*(5/9)

def celsius_to_fahrenheit(c):
    """Convert temperature measurement in degrees Celsius to Fahrenheit.

    PARAMETERS
    ----------
    c : float
        A temperature measurement in degrees Celsius

    RETURNS
    -------
    f : float
        A temperature measurement in degrees Fahrenheit
    """

    return (c*(9/5))+32

"""
A python module for converting distance from mile to kilometers,
and vice versa.
"""

def miles_to_kilometers(m):
    """ Convert distance in miles to kilometers.

    PARAMETERS
    ----------
    m : float
        A distance measurement in miles.

    RETURNS
    -------
    k : float
        A distance measurement in kilometers.
    """

    return 1.609*m

def kilometers_to_miles(k):
        """ Convert distance in kilometers to miles.

        PARAMETERS
        ----------
        k : float
            A distance measurement in kilometers.

        RETURNS
        -------
        m : float
            A distance measurement in miles.
        """

        return 0.621*k

def floatToStrWithDecimals(n: float) -> str:
    """Function to format a float to a string, suppressing scientific notation
    and displaying up to 10 decimal places.
    
    Arguments:
        n {float} -- Float to be formatted.
    
    Returns:
        str -- Formatted float.
    """

    return '{0:.10f}'.format(n)

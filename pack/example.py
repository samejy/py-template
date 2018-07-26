
def a_function(a: int, b: float) -> float:
    """ A daft function """
    if a < 0:
        raise Exception("a must be greater than 0")

    return a + b

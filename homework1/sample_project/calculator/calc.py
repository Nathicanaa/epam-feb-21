def check_power_of_2(x: int) -> bool:
    """
    Checks if x is a power of 2
    Args:
        x: int number

    Returns: True if x is a power of 2

    """
    return (x & (x - 1) == 0) and x != 0

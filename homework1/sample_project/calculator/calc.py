def check_power_of_2(x: int) -> bool:
    """Return true if x is a power of 2"""
    return (x & (x - 1) == 0) and x != 0

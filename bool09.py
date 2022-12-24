def main(a):
    """
    Check the natural number. Natural numbers are numbers used in counting.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    bool = a > 0 and a % 1 == 0
    return bool

print(main(1.5))
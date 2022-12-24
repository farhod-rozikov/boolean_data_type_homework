def main(a):
    """
    check the whole number. Integers are 0 and a positive number.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    bool = a >= 0 and a % 1 == 0
    return bool

print(main(4))
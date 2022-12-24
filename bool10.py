from math import sqrt

def main(a):
    """
    Check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    bool = sqrt(a) % 1 == 0
    return bool

print(main(4))
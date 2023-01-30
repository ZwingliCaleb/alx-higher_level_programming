#!/usr/bin/python3
"""Find a solution to the Nqueens challenge"""

def nqueens(n, c=[]):
    """Here we recursively compute solutions to solve the problem
    Args:
        n (int): dimensions of the board and number of queens
        c (list): list of current candidate positions to help find solutions

    output: Prints valid solutions to standard output
    """
    if reject(n, c):
        return
    if accept(n, c):
        print(c)
    s = first_candidate(n, c)
    while s is not None:
        nqueens(n, s)
        s = next_candidate(n, s)

def reject(n, c):
    """A routine to test if the current solution stands to be valid
    Args:
        n (int): board dimensions and number of the queens
        c (list): list of current candidate positions for the solution

        Return: This returns True if final position is in conflict with the previous position which otherwise becomes False
    """

    try:
        last = c[-1]
    except IndexError:
        return False
    for i in c[:-1]:
        if i[0] == last[0] or i[1] == last[1]:
            return True
        if abs(last[0] - i[0]) == abs(last[1] - i[1]):
            return True
    return False

def accept(n, c):
    """test if current list of positions provides a solution

    Args:
        n (int): Board dimensions and number of queens
        c (list): list of candidates positions giving solutions
        Return: True if len(c) == n, whch otherwise becomes False
    """

    if len(c) == n:
        return True
    return False

def first_candidate(n, c):
    """ Add positions to the end of candidate solutions
    Args:
        n (int): board dimensions and queen numbers
        c (list): list of current candidate positions for solution

    Return: new list with added positions or otherwise None if len(c) == n.
    """
    if len(c) == n:
        return None
    try:
        last = c[-1]
    except IndexError:
        return [[0, 0]]
    if last[1] < n-1:
        return c + [[last[0], last[1]+1]]
    elif last[0] < n-1:
        return c + [[last[0]+1, 0]]
    else:
        return None


def next_candidate(n, s):
    """routine udate of last position of candidate solution
    Args:
        n (int): board dimensions and number of queens
        c (list): list of current positions providing solution

        Return: New list of candidates otherwise None if board end is reached
    """
    last = s[-1]
    if last[1] < n-1:
        return s[:-1] + [[last[0], last[1]+1]]
    elif last[0] < n-1:
        return s[:-1] + [[last[0]+1, 0]]
    else:
        return None

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print('Usage: nqueebs N')
        exit(1)
    n = sys.argv[1]
    if not n.isdigit():
        print('N must be a number')
        exit(1)
    n = int(n)
    if n < 4:
        print('N must be atleast 4')
        exit(1)
    nqueens(n)
    exit(0)

def triangle(size, style="normal"):
    """This function must print a triangle using the # character on the screen.

    Example:
    >>> triangle(5)
    #
    ##
    ###
    ####
    #####

    """
    tri = ""
    for i in range(size):
        tri += "#"
        print(tri)
    return tri


def rectangle(width, height):
    """This function must print a rectangle with the correct dimensions on the screen with #.

    !!! The rectangle is not filled with # !!!

    Examples:
    >>> rectangle(0, 0)

    >>> rectangle(1, 1)
    #

    >>> rectangle(3, 1)
    ###

    >>> rectangle(10, 3)
    ##########
    #        #
    ##########

    """

    print ("#" * width)
    for i in range(height):
        print("#"+ " " * (width - 2) + "#")
    print ("#" * width)
            
    return

# triangle(0)
# triangle(10)

# rectangle(4, 4)
# # rectangle(-1, -1)

def count_lines(file):
    with open(file) as f:
        lines = f.readlines()
        for i in lines:
            print(i)

count_lines("midterm.txt")
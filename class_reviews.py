"""
File: class_reviews.py
Name: Andy Wu
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your program should be case-insensitive.
If the user input -1 for class name, your program would output
the maximum, minimum, and average among all the inputs.
"""
LEAVE = -1


def main():
    """
    To tell what the class it is, and calculate the average.
    And pick up the maximum and minimum value.
    """
    classes = str(input('Which class? '))
    classes = classes.lower()
    # sc001
    n1 = 0
    data1 = 0
    maximum_001 = 0
    minimum_001 = 0
    # sc101
    maximum_101 = 0
    minimum_101 = 0
    n2 = 0
    data2 = 0
    if classes != str(LEAVE):
        data = int(input('Score: '))
        if classes == 'sc001':
            # To decide the first data at sc001
            maximum_001 = data
            minimum_001 = data
            data1 = data
            n1 = 1
        elif classes == 'sc101':
            # To decide the first data at sc101
            maximum_101 = data
            minimum_101 = data
            data2 = data
            n2 = 1
        average_001 = 0
        average_101 = 0
        while True:
            if classes != str(LEAVE):
                if classes == str('sc001'):
                    if n1 == 0:
                        # To decide the first data at sc001
                        maximum_001 = data
                        minimum_001 = data
                        n1 = 1
                        data1 = data
                    else:
                        data1 += data
                        n1 += 1
                        average_001 = data1 / n1
                        if data > maximum_001:
                            # Recording the maximum score in the SC001 class.
                            maximum_001 = data
                        elif data < minimum_001:
                            # Recording the minimum score in the SC001 class.
                            minimum_001 = data
                elif classes == str('sc101'):
                    if n2 == 0:
                        # To decide the first data at sc101
                        maximum_101 = data
                        minimum_101 = data
                        n2 = 1
                        data2 = data
                    else:
                        data2 += data
                        n2 += 1
                        average_101 = data2 / n2
                        if data > maximum_101:
                            # Recording the maximum score in the SC101 class.
                            maximum_101 = data
                        elif data < minimum_101:
                            # Recording the minimum score in the SC101 class.
                            minimum_101 = data
            classes = str(input('Which class? '))
            classes = classes.lower()

            if classes == str(LEAVE):
                print("=============SC001=============")
                if n1 != 0:
                    print("Max (001): " + str(maximum_001))
                    print("Min (001): " + str(minimum_001))
                    print("Avg (001): " + str(average_001))
                else:
                    print('No score for SC001')
                print("=============SC101=============")
                if n2 != 0:
                    print("Max (101): " + str(maximum_101))
                    print("Min (101): " + str(minimum_101))
                    print("Avg (101): " + str(average_101))
                else:
                    print('No score for SC101')
                break
            data = int(input('Score: '))
    else:
        print("No class scores were entered.")

#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()

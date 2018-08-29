from main import main


# read input from text file
def file():
    with open('data/input.txt', 'r') as inp:
        text = inp.read().replace('\n', '')

    output = main(text)
    print("\nResult: \n{output}".format(output=output))


# keyboard input
def keyboard():
    text = input("Enter the text:\n")
    output = main(text)
    print("\nResult: \n{output}".format(output=output))


# choose either input function
if __name__ == '__main__':
    keyboard()

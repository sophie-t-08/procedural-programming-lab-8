stack = []

def push(item):
    stack.append(item)

def pop():
    if is_empty() == True:
        return False
    else:
        stack.pop()

def peek():
    if is_empty == True:
        return False
    else:
        return stack[-1]

def is_empty():
    if len(stack) == 0:
        return True

def size():
    return len(stack)


word_1 = input("Enter a word: ")
push(word_1)
word_2 = input("Enter a word: ")
push(word_2)
word_3 = input("Enter a word: ")
push(word_3)
word_4 = input("Enter a word: ")
push(word_4)

print("Current document :", stack)

undo = input("Would you like to undo previous action? ")
if undo == "yes":
    undo_times = int(input("How many actions would you like to undo? "))
    for i in range(undo_times):
        print("Undo last action...")
        pop()
    print("Updated document: ", stack)
elif undo == "no":
    print("Current document: ", stack)
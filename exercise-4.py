queue = []

def enqueue(customer):
    queue.append(customer)


def dequeue():
    if is_empty() == True:
        return "Queue is empty"
    else:
        queue.pop(0)


def peek():
    if is_empty() == True:
        return "Queue is empty"
    else:
        return queue[0]


def is_empty():
    if len(queue) == 0:
        return "Queue is empty"



def size():
    return len(queue)




num_of_customers = int(input("Enter the number of customers you would like to add: "))
for i in range(num_of_customers):
    customer = input("Enter customer: ")
    enqueue(customer)
print(queue)

print(peek)

print("Next customer:", peek())
for i in range(num_of_customers):
    print("Serving:", peek())
    dequeue()

print(is_empty())
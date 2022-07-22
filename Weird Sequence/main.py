import matplotlib.pyplot as plt

graph = []  # An array to save numbers
number = int(input("Enter Number\n"))  # The first term of the sequence
graph.append(number)
while True:
    if number % 2 == 0:  # If the number is even divide it by 2
        number = int(number / 2)
    else:  # If the number is odd multiply it by 3 and add 1
        number = 3 * number + 1
    graph.append(number)
    if number == 1:  # Condition to break the loop because it will continue in infinite loop 4 2 1
        break
plt.plot(graph, "*-", color="green")
plt.show()

import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

#prohozeni my_list[1], my_list[3] = my_list[3], my_list[1]

def selection_sort(values):
    #print(values)
    for min_index in range(len(values)):
        min_value = values[min_index]
        min_ind = min_index

        for i in range(min_index, len(values)):
            if values[i] < min_value:
                min_ind = i
                min_value = values[i]
        values[min_ind], values[min_index] = values[min_index], values[min_ind]

    #print(values)


def bubble_sort(values):

    for i in range(len(values)):
        for j in range(0, len(values)-1):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]

    return values










if __name__ == "__main__":
    values = random_numbers(10)
    print(bubble_sort(values))


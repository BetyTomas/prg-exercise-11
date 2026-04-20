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

    for i in range(len(values)- 1):
        prvni_cislo = values[i]
        druhe_cislo = values[i + 1]

        if prvni_cislo > druhe_cislo:
            prvni_cislo, druhe_cislo = druhe_cislo, prvni_cislo

    return values



if __name__ == "__main__":
    values = random_numbers(10)
    print(bubble_sort(values))


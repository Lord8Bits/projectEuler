liste = [-1, 900, 10, 2, -1, -1, 100, -1, 90, 80, 2]

for i in range(len(liste)-1, 0, -1):
    swap = False
    temp = None
    temp_i = 0
    for j in range(i):
        if liste[j] > liste[j+1] != -1 and liste[j] != -1: #If the values are normal and temp is empty
            liste[j], liste[j+1] = liste[j+1], liste[j]
            swap = True

        elif temp and temp > liste[j] != -1: #If temp is full and is superior to the first element knowing that it is not equal to -1
            liste[j], liste[temp_i] = temp, liste[j]
            swap = True

        elif temp and temp > liste[j+1] != -1: #same thing but this is for the next element since we will stop before the index of the final element
            liste[j+1], liste[temp_i] = temp, liste[j+1]
            swap = True

        elif liste[j] != -1: #Holds the value of the current element to compare it to the next element different to -1
            temp = liste[j]
            temp_i = j

    if not swap:
        break

print(liste)
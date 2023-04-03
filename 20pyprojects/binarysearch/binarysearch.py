#functie met 2 parameters (list, target)
#meerdere variabelen midden start en einde, stappen
#recursion or a while loop
#verhoog de stappen met elke deling 
#regels voor het volgen van target nummer
#handig bij het handelen met grote getallen 

def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while(start<=end):
        print("Stap ",steps, ":",str(list[start:end+1]))

        steps = steps+1
        middle = (start + end) // 2

        if element == list[middle]:
            return middle
        if element < list[middle]:
            end = middle - 1
        else:
            start = middle + 1
            #[1,2,3,4,5] elemnt:2
    return -1

my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
target = 1
binary_search(my_list, target)

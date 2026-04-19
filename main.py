def set_operations(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    difference = set1.symmetric_difference(set2)
    return intersection, union, difference

def main():
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    intersection, union, difference = set_operations(list1, list2)
    print("Kesishma: ", intersection)
    print("Birlashma: ", union)
    print("Farq: ", difference)
    print("List1: ", list1)
    print("List2: ", list2)
    print("Set1: ", set(list1))
    print("Set2: ", set(list2))
    print("Set1 uzunligi: ", len(set(list1)))
    print("Set2 uzunligi: ", len(set(list2)))

    list3 = [1.2, 2.3, 3.4, 4.5, 5.6]
    list4 = [4.5, 5.6, 6.7, 7.8, 8.9]
    intersection, union, difference = set_operations(list3, list4)
    print("Kesishma: ", intersection)
    print("Birlashma: ", union)
    print("Farq: ", difference)
    print("List3: ", list3)
    print("List4: ", list4)
    print("Set3: ", set(list3))
    print("Set4: ", set(list4))
    print("Set3 uzunligi: ", len(set(list3)))
    print("Set4 uzunligi: ", len(set(list4)))

    list5 = ["a", "b", "c", "d", "e"]
    list6 = ["d", "e", "f", "g", "h"]
    intersection, union, difference = set_operations(list5, list6)
    print("Kesishma: ", intersection)
    print("Birlashma: ", union)
    print("Farq: ", difference)
    print("List5: ", list5)
    print("List6: ", list6)
    print("Set5: ", set(list5))
    print("Set6: ", set(list6))
    print("Set5 uzunligi: ", len(set(list5)))
    print("Set6 uzunligi: ", len(set(list6)))

    list7 = [True, False, True, False]
    list8 = [False, True, False, True]
    intersection, union, difference = set_operations(list7, list8)
    print("Kesishma: ", intersection)
    print("Birlashma: ", union)
    print("Farq: ", difference)
    print("List7: ", list7)
    print("List8: ", list8)
    print("Set7: ", set(list7))
    print("Set8: ", set(list8))
    print("Set7 uzunligi: ", len(set(list7)))
    print("Set8 uzunligi: ", len(set(list8)))

main()
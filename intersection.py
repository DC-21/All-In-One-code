def intersection(set1, set2, set3):
    intersection = set1.intersection(set2, set3)
    return intersection

set1 = {1,2,3,4,5}
set2 = {2,3,4,5,6}
set3 = {4,5,6,7}

inter = intersection(set1,set2,set3)
print(inter)
import itertools

k =  [[19, 'diamond'], [10, 'diamond'], [16, 'heart'], [52, 'diamond'], [49, 'heart'], [50, 'diamond'], [12, 'club'], [28, 'diamond'], [52, 'club'], [20, 'diamond'], [49, 'diamond'], [39, 'spade'], [34, 'heart'], [11, 'club'], [14, 'spade'], [15, 'spade'], [6, 'spade'], [20, 'club'], [22, 'heart'], [46, 'spade'], [18, 'diamond'], [6, 'heart'], [44, 'spade'], [40, 'diamond'],[18, 'diamond'], [1, 'heart'], [23, 'heart'], [1, 'diamond'], [3, 'club'], [50, 'diamond'], [42, 'spade'], [13, 'heart'], [22, 'diamond'], [49, 'club'], [51, 'heart'], [21, 'diamond'], [36, 'club'], [6, 'spade'], [49, 'spade'], [22, 'spade'], [34, 'spade'], [12, 'diamond'], [25, 'heart'], [47, 'spade'], [6, 'diamond'], [47, 'diamond'], [20, 'diamond']]

print(len(k))
print(sorted(k))

new_k = []
for elem in k:
    if elem not in new_k:
        new_k.append(elem)
k = new_k

print("#####################################################", len(k))
print("#####################################################", sorted(k))





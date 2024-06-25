##Problem 5 - Pair with Target Sum
#your code here
def pair_sum(arr, target):
    num_map = {} #membuat dictionary untuk menyimpan nilai dan indeksnya

    for i, num in enumerate(arr): #iterasi melalui setiap elemen pada array
        complement = target - num #menghitung nilai yang diperlukan untuk mencapai target
        if complement in num_map: #jika nilai pelengkap sudah ada di map, kita temukan pasangannya
            return [num_map[complement], i]
        num_map[num] = i
    return None
#Testnya
print(pair_sum([1, 2, 3, 4, 6], 6)) # [1, 3]
print(pair_sum([2, 5, 9, 11], 11)) # [0, 2]
print(pair_sum([1, 3, 5, 7], 12)) # [2, 3]
print(pair_sum([1, 4, 6, 8], 10)) # [1, 2]
print(pair_sum([1, 5, 6, 7], 6)) # [0, 1]
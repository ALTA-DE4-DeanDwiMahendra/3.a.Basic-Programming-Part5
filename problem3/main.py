##Problem 3 - Join Array Remove Duplicate
#your code
def join_array_remove_duplicate(arrayA, arrayB):
    merged_set = set(arrayA + arrayB) # Menggabungkan 2 aeeay dan konversi set untuk menghilangkan duplikat datanya
    merged_list = list(merged_set)
    return merged_list
#Test cases
print(join_array_remove_duplicate(["apel", "anggur"], ["lemon", "leci", "nanas"])) ## ["apel", "anggur", "lemon", "leci", "nanas"]
print(join_array_remove_duplicate(["samsung", "apple"], ["apple", "sony", "xiaomi"])) ## ["samsung", "apple", "sony", "xiaomi"]
print(join_array_remove_duplicate(["football", "basketball"], ["basketball", "football"])) ## ["football", "basketball"]

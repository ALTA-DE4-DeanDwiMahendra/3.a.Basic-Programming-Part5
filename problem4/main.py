##Problem 4 - Angka Muncul Sekali
def muncul_sekali(angka):
    freq = {} #Menghitung frekuensi setiap karakter dalam string
    for char in angka:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    
    angka_unik = [int(char) for char in freq if freq [char] == 1] #Membuat daftar angka yang bisa muncuk sekali
    return angka_unik
#Test code
print(muncul_sekali("1234123")) # [4]
print(muncul_sekali("76523752")) # [6, 3]
print(muncul_sekali("12345")) # [1, 2, 3, 4, 5]
print(muncul_sekali("1122334455")) # []
print(muncul_sekali("0872504")) # [8, 7, 2, 5, 4]
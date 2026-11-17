cek=int(input("введите кол-во секунд:"))
hour=cek // 60 // 60
print(f"{cek}секунд={hour}часов")
min=(cek % 3600) // 60 
print(f"в {hour}часах={min}оставшихся минут")
sec=cek % 60
print(f"в {min}минутах={sec}оставшихся секунд")
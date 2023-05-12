def find_apartment_floor(n, floors, apartments_per_floor):
    apartments_per_entrance = floors * apartments_per_floor
    entrance = (n - 1) // apartments_per_entrance + 1
    floor = ((n - 1) % apartments_per_entrance) // apartments_per_floor + 1
    return entrance, floor
n = 10
floors = 2
apartments_per_floor = 4

entrance, floor = find_apartment_floor(n, floors, apartments_per_floor)

print("Квартира №{} знаходиться в підїзді №{} на {} поверсі".format(n, entrance, floor))
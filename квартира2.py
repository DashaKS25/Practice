
def find_apartment(floor_count, apartments_per_floor, apartment_number):

    total_apartments = floor_count * apartments_per_floor


    entrance = (apartment_number - 1) // (apartments_per_floor * 1)


    floor = ((apartment_number - 1) % apartments_per_floor) + 1

    return f"Вам нужно подняться на {entrance + 1} подъезд и на {floor} этаж, чтобы найти квартиру номер {apartment_number}"


print(find_apartment(9, 4, 25))
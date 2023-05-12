def check_file(file_name):
    with open(file_name, 'r') as f:
        for line in f:
            parts = line.strip().split(';')
            num = list(map(int, parts[0].split()))
            avg = sum(num) // len(num)
            remainder = sum(num) % len(num)
            check_num = int(parts[1].split()[0])
            if check_num == avg and remainder:
                print(line.strip() + 'True')
            else:
                print(line.strip() + 'False')


check_file('1.txt')



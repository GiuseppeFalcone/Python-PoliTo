ATTENDANCE_FILE = 'attendance.txt'
SUSPICIOUS_FILE = 'suspicious.txt'
OUTPUT_FILE = 'contacts.txt'


def main():
    guests = dict()
    try:
        with open(ATTENDANCE_FILE, 'r') as file:
            for line in file:
                x = line.rstrip().split(',')
                guest_name = x[0]
                guests[guest_name] = None
                temp = dict()
                temp['phone'] = x[1]
                temp['day_in'] = int(x[2])
                temp['day_out'] = int(x[3])
                guests[guest_name] = temp
    except OSError as error:
        print(f"{error} occurred with {ATTENDANCE_FILE}")

    contacts = dict()
    try:
        with open(SUSPICIOUS_FILE, 'r') as file:
            for line in file:
                suspected = line.rstrip()
                contacts[suspected] = None
                temp = dict()
                for name in guests:
                    if suspected != name:
                        name_in = guests[name]['day_in']
                        name_out = guests[name]['day_out']
                        susp_in = guests[suspected]['day_in']
                        susp_out = guests[suspected]['day_out']
                        if susp_out >= name_in and susp_in <= name_out:
                            temp[name] = None
                            temp[name] = guests[name]['phone']
                contacts[suspected] = temp
    except OSError as error:
        print(f"Problem with{SUSPICIOUS_FILE}: {error}")

    try:
        with open(OUTPUT_FILE, 'w') as file:
            for suspect in contacts:
                file.write(f"**Customer contacts {suspect}:**\n")
                if contacts[suspect]:
                    for guest in contacts[suspect]:
                        file.write(f"Contact with {guest}, phone{contacts[suspect][guest]}\n")
                elif not contacts[suspect]:
                    file.write(f"The customer {suspect} had no contacts\n")
    except OSError as error:
        print(f"Problem with{OUTPUT_FILE}: {error}")


if __name__ == '__main__':
    main()

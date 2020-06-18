import csv

def get_rooms(filename):
    with open(filename) as file:
        rooms = [{k: v for k, v in row.items()}
                 for row in csv.DictReader(file, skipinitialspace=True)]
        return rooms


def export_rooms(filename, rooms):
    with open(filename, 'w+', encoding="utf8", newline='') as file:
        f = csv.DictWriter(file, fieldnames=rooms[0].keys())
        f.writeheader()
        f.writerows(rooms)


def get_users(filename):
    users = []
    with open(filename) as file:
        for row in file:
            print(row + "1")
            users.append(row[:-1])
    return users


def export_users(filename, users):
    with open(filename, "w") as file:
        for elem in users:
            file.write(elem + "\n")


if __name__ == '__main__':
    pass

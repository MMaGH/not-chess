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
            users.append(row[:-1])
    return users


def export_users(filename, users):
    with open(filename, "w") as file:
        for elem in users:
            file.write(elem + "\n")


def get_map(filename):
    with open(filename, "r") as file:
        reader = csv.reader(file)
        map = list(reader)
    return map


def export_map(filename, map):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(map)


def get_characters(filename):
    with open(filename) as file:
        characters = [{k: v for k, v in row.items()}
                 for row in csv.DictReader(file, skipinitialspace=True)]
        return characters


def export_characters(filename, characters):
    with open(filename, 'w+', encoding="utf8", newline='') as file:
        f = csv.DictWriter(file, fieldnames=characters[0].keys())
        f.writeheader()
        f.writerows(characters)



if __name__ == '__main__':
    pass

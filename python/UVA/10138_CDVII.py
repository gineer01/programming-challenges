import fileinput
import itertools

f = fileinput.input()

cases = int(next(f))
next(f)


def build_trip(tolls, enter, exit):
    start_time = int(enter[1].split(':')[2])
    toll = tolls[start_time]
    return abs(int(enter[3]) - int(exit[3])) * toll


def cal_toll(tolls, photos):
    trips = []
    enter = None
    for p in photos:
        type = p[2]
        if type == 'exit':
            if enter:
                trips.append(build_trip(tolls, enter, p))
                enter = None
        if type == 'enter':
            enter = p

    if trips:
        charge = sum(trips) + len(trips) * 100 + 200
        return "${}.{:02d}".format(charge//100, charge % 100)
    else:
        return None


def solve(tolls, photos):
    from operator import itemgetter
    photos.sort(key=itemgetter(0, 1))

    for k,g in itertools.groupby(photos, key=itemgetter(0)):
        toll = cal_toll(tolls, g)
        if toll:
            print(k, toll)


def process_case(f):
    tolls = list(map(int, next(f).split()))
    photos = []
    for l in f:
        if l.strip():
            photos.append(l.strip().split())
        else:
            break
    solve(tolls, photos)

for i in range(cases):
    if i > 0:
        print()
    process_case(f)


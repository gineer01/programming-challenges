# from functools import lru_cache
import fileinput
import sys
import math

# sys.setrecursionlimit(3000)
IMPOSSIBLE = "IMPOSSIBLE"
CHARGE = "C"
SHOOT = "S"


def get_damage(program):
    damage = 0
    shot_damage = 1
    for c in program:
        if c == CHARGE:
            shot_damage *= 2
        elif c == SHOOT:
            damage += shot_damage

    return damage, shot_damage


def get_swap(delta_defense, program):
    last_charge_index = program.rfind(CHARGE)
    if last_charge_index == -1:
        if delta_defense > 0:
            return IMPOSSIBLE
        else:
            return 0

    charge_count = sum(1 for i in range(last_charge_index + 1) if program[i] == CHARGE)
    shoot_count = len(program) - last_charge_index - 1
    delta_damage_per_shot = 2**(charge_count - 1)
    needed_swap = math.ceil(delta_defense / delta_damage_per_shot)
    if needed_swap <= shoot_count:
        return needed_swap
    else:
        program = program[:last_charge_index] + program[last_charge_index + 1:]
        delta_defense -= delta_damage_per_shot * shoot_count
        swap = get_swap(delta_defense, program)
        if swap == IMPOSSIBLE:
            return IMPOSSIBLE
        else:
            return shoot_count + swap


def solve(defense, program):
    #Simplify: remove C at the end
    while len(program) > 0 and program[-1] == CHARGE:
        program = program[:-1]

    #Simplify: remove S at the beginning
    first_charge_index = program.find(CHARGE)
    if first_charge_index == -1:
        damage = len(program)
        if damage > defense:
            return IMPOSSIBLE
        else:
            return 0
    else:
        if defense < first_charge_index:
            return IMPOSSIBLE
        else:
            program = program[first_charge_index:]
            defense -= first_charge_index

    damage, shot_damage = get_damage(program)
    if damage > defense:
        return get_swap(damage - defense, program)
    else:
        return 0



assert solve(1, "SCCS") == IMPOSSIBLE
assert solve(3, "CSCSS") == 5
assert solve(2, "SSSCSC") == IMPOSSIBLE
assert solve(0, "CCCCCCCC") == 0
assert solve(2, "SSC") == 0
assert solve(2, "CS") == 0

def main():
    f = fileinput.input()
    t = int(next(f))
    for i in range(t):
        d, p = next(f).split()
        defense = int(d)
        program = p.strip()
        print("Case #%s: %s" % (i + 1, solve(defense, program)))

main()

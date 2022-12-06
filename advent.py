"""Advent of code 2022 puzzles"""
import string


def get_input(filename: str):
    """gets input list from file"""
    with open(filename, "r", encoding="utf-8") as file:
        input_data: list = list(filter(None, file.read().split("\n")))
    return input_data


def day1(top_n: int):
    """day1"""

    input_list = get_input("input1.txt")
    current_sum: int = 0
    calory_sum: list = []
    for row in input_list:
        if row == "":
            calory_sum.append(current_sum)
            current_sum = 0
        else:
            current_sum += int(row)

    top_i_calory_sum: int = 0
    for i in range(top_n):
        top_i_calory_sum += max(calory_sum)
        calory_sum.pop(calory_sum.index(max(calory_sum)))
    print(top_i_calory_sum)


def day2(lut_version: int):
    """day2"""
    matches = get_input("input2.txt")
    points_lut = {
        1: {
            "A X": 4,
            "A Y": 8,
            "A Z": 3,
            "B X": 1,
            "B Y": 5,
            "B Z": 9,
            "C X": 7,
            "C Y": 2,
            "C Z": 6,
        },
        2: {
            "A X": 3,
            "A Y": 4,
            "A Z": 8,
            "B X": 1,
            "B Y": 5,
            "B Z": 9,
            "C X": 2,
            "C Y": 6,
            "C Z": 7,
        },
    }
    total_score: int = 0
    for match in matches:
        if match:
            total_score += (
                points_lut[lut_version][match]
                if points_lut[lut_version].get(match)
                else 0
            )

    print(total_score)


def day3(mode: str):
    """day3"""
    item_lut: dict = dict(
        zip(string.ascii_lowercase + string.ascii_uppercase, range(1, 53))
    )
    rucksacks: list = get_input("input3.txt")
    priority_sum: int = 0
    if mode == "item_priority_sum":
        for rucksack in rucksacks:
            first_compartment, second_compartment = (
                rucksack[: len(rucksack) // 2],
                rucksack[len(rucksack) // 2 :],
            )
            out_of_place_item = "".join(
                e for e in set(first_compartment) & set(second_compartment)
            )
            priority_sum += item_lut[out_of_place_item]
    elif mode == "badge_priority_sum":
        rucksack_group = []
        for rucksack in rucksacks:
            rucksack_group.append(rucksack)
            if len(rucksack_group) == 3:
                priority_sum += item_lut[
                    "".join(
                        e
                        for e in set(rucksack_group[0])
                        & set(rucksack_group[1])
                        & set(rucksack_group[2])
                    )
                ]
                rucksack_group = []
    print(priority_sum)


def day4():
    """day4"""
    elf_pairs: list[str] = get_input("input4.txt")
    fully_contained_pairs: int = 0
    overlapping_pairs: int = 0
    for pair in elf_pairs:
        elf_1, elf_2 = [
            set((lambda x: range(int(x[0]), int(x[1]) + 1))(x))
            for x in [boundaries.split("-") for boundaries in pair.split(",")]
        ]
        fully_contained_pairs += 1 if elf_1 >= elf_2 or elf_1 <= elf_2 else 0
        overlapping_pairs += 1 if elf_1 & elf_2 else 0
    print(f"fully contained pairs: {fully_contained_pairs}")
    print(f"overlapping pairs: {overlapping_pairs}")


def day5(cratemover_9001: bool):
    """day5"""
    crates_and_operations: list = get_input("input5.txt")
    crates_raw: list = [
        (
            crate_row.replace("    ", " [ ]")
            .replace("[", "")
            .replace("] ", "")
            .replace("]", "")
        )
        for crate_row in crates_and_operations[:8]
    ]
    crates: list = []
    for i in range(len(crates_raw[0])):
        crates.append(
            list(filter(None, [x[i] if x[i] != " " else None for x in crates_raw]))
        )
    for stack in crates:
        stack = [x for x in stack if not x == " "]
    operations = [
        list(int(s) for s in operation.split() if s.isdigit())
        for operation in crates_and_operations[9:]
    ]
    crate_capacity: int = 0
    for operation in operations:
        for i in range(operation[0]):
            if cratemover_9001:
                crate_capacity = operation[0] - i - 1
            if len(crates[operation[1] - 1]) == 0:
                raise Exception("what the fuck")
            crate = crates[operation[1] - 1].pop(crate_capacity)
            crates[operation[2] - 1].insert(0, crate)

    for stack in crates:
        if stack:
            print(stack[0], end="")
        else:
            print(" ", end="")
    print("")


def day6(marker_size: int):
    """day6"""
    datastream: str = get_input("input6.txt")[0]
    buf: str = ''
    i: int = 0
    for i, char in enumerate(datastream):
        buf += char
        if len(buf) == marker_size:
            if len(set(buf)) == marker_size:
                break
            buf = buf[1:]
    print(i+1)


if __name__ == "__main__":
    # day1(1)
    # day1(3)
    # day2(1)
    # day2(2)
    # day3('item_priority_sum')
    # day3('badge_priority_sum')
    # day4()
    # day5(False)
    # day5(True)
    day6(4)
    day6(14)

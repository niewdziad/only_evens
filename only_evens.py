def get_only_evens(list_: list) -> list:
    return [num for idx, num in enumerate(list_) if idx % 2 == 0 and num % 2 == 0]

assert get_only_evens([1, 3, 2, 6, 4, 8]) == [2, 4], "Wrong, #1"
assert get_only_evens([0, 1, 2, 3, 4]) == [0, 2, 4], "Wrong, #2"
assert get_only_evens([1, 2, 3, 4, 5]) == [], "Wrong, #3"
assert get_only_evens([]) == [], "Wrong, #4"
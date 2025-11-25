"""Simple list sorter and searcher."""

def get_numbers():
    raw = input("Enter numbers separated by spaces: ").strip()
    if not raw:
        return []
    try:
        return [float(token) for token in raw.split()]
    except ValueError:
        print("Invalid input. Please enter only numbers.")
        return get_numbers()


def main():
    nums = get_numbers()
    nums.sort()
    print(f"Sorted list: {nums}")

    target_raw = input("Enter a number to search for: ").strip()
    try:
        target = float(target_raw)
    except ValueError:
        print("Invalid search value.")
        return

    found = target in nums
    if found:
        idx = nums.index(target)
        print(f"{target} found at index {idx}.")
    else:
        print(f"{target} not found in the list.")


if __name__ == "__main__":
    main()


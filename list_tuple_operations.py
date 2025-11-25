from typing import List, Tuple


def prompt_numbers(message: str) -> List[float]:
    """Prompt the user for a whitespace separated list of numbers."""
    while True:
        raw = input(message).strip()
        if not raw:
            print("Input cannot be empty. Try again.")
            continue
        parts = raw.split()
        numbers = []
        try:
            for part in parts:
                numbers.append(float(part))
        except ValueError:
            print("Please enter only numeric values separated by spaces.")
            continue
        return numbers


def prompt_tuple(message: str) -> Tuple[float, ...]:
    values = prompt_numbers(message)
    return tuple(values)


def list_sort_search() -> None:
    numbers = prompt_numbers("Enter numbers for the list (space separated): ")
    numbers.sort()
    print(f"Sorted list: {numbers}")

    while True:
        target_raw = input("Enter a number to search: ").strip()
        try:
            target = float(target_raw)
            break
        except ValueError:
            print("Please enter a numeric value.")

    found = target in numbers
    index = -1
    if found:
        for i, value in enumerate(numbers):
            if value == target:
                index = i
                break
    if found:
        print(f"{target} found at position {index} (0-based index).")
    else:
        print(f"{target} not found in the list.")


def list_sum_average() -> None:
    numbers = prompt_numbers("Enter numbers to compute sum and average: ")
    total = sum(numbers)
    average = total / len(numbers)
    print(f"Total sum: {total}")
    print(f"Average: {average}")


def merge_lists_remove_duplicates() -> None:
    list1 = prompt_numbers("Enter numbers for the first list: ")
    list2 = prompt_numbers("Enter numbers for the second list: ")
    merged = list1 + list2
    seen = set()
    deduped = []
    for value in merged:
        if value not in seen:
            seen.add(value)
            deduped.append(value)
    print(f"Merged list without duplicates: {deduped}")


def second_largest_in_tuple() -> None:
    values = prompt_tuple("Enter tuple elements (space separated numbers): ")
    unique_values = sorted(set(values))
    if len(unique_values) < 2:
        print("Tuple must contain at least two distinct elements.")
        return
    second_largest = unique_values[-2]
    print(f"Second largest element: {second_largest}")


def count_occurrence() -> None:
    choice = ""
    while choice not in {"l", "t"}:
        choice = input("Count in (L)ist or (T)uple? ").strip().lower()
        if choice not in {"l", "t"}:
            print("Enter 'L' for list or 'T' for tuple.")

    if choice == "l":
        values = prompt_numbers("Enter list elements: ")
    else:
        values = prompt_tuple("Enter tuple elements: ")

    while True:
        element_raw = input("Enter the value to count: ").strip()
        try:
            element = float(element_raw)
            break
        except ValueError:
            print("Please enter a numeric value.")

    occurrences = values.count(element)
    target_type = "list" if choice == "l" else "tuple"
    print(f"{element} occurs {occurrences} times in the {target_type}.")


def show_menu() -> None:
    print("\nMenu:")
    print("1. Sort list & search element")
    print("2. Sum and average of list elements")
    print("3. Merge two lists and remove duplicates")
    print("4. Second largest element in tuple")
    print("5. Count occurrence of element")
    print("6. Exit")


def main() -> None:
    operations = {
        "1": list_sort_search,
        "2": list_sum_average,
        "3": merge_lists_remove_duplicates,
        "4": second_largest_in_tuple,
        "5": count_occurrence,
    }

    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "6":
            print("Goodbye!")
            break
        if choice in operations:
            operations[choice]()
        else:
            print("Invalid choice. Please select a number between 1 and 6.")


if __name__ == "__main__":
    main()


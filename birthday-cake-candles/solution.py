
def find_max_height(candles):
    """Return the maximum candle height."""
    return max(candles)


def count_tallest_candles(candles, max_height):
    """Return the number of candles with the maximum height."""
    return candles.count(max_height)


def get_tallest_positions(candles, max_height):
    """Return the positions of all tallest candles."""
    return [i for i, height in enumerate(candles) if height == max_height]


def is_symmetric(candles, max_height):
    """
    Check whether the tallest candles are placed
    symmetrically around the center of the array.
    """
    positions = get_tallest_positions(candles, max_height)

    left = 0
    right = len(positions) - 1
    n = len(candles)

    while left <= right:
        if positions[left] + positions[right] != n - 1:
            return False

        left += 1
        right -= 1

    return True


def make_symmetric(candles, max_height):
    """
    Rearrange the candles so that the tallest candles
    are placed symmetrically around the center.
    """
    result = candles.copy()

    tallest_count = result.count(max_height)
    n = len(result)

    # Remove the tallest candles from their original positions
    remaining = [height for height in result if height != max_height]

    # Start with an array of the remaining candles
    result = remaining[:]

    # Add placeholders to make the array the original size
    while len(result) < n:
        result.append(None)

    # Place tallest candles symmetrically
    left = 0
    right = n - 1
    placed = 0

    while placed < tallest_count:
        if placed + 1 < tallest_count:
            result[left] = max_height
            result[right] = max_height

            left += 1
            right -= 1
            placed += 2
        else:
            # If there is one tallest candle left,
            # place it in the center.
            center = n // 2
            result[center] = max_height
            placed += 1

    return result


def birthday_cake_candles(candles):
    """Analyze the birthday cake candles."""

    if not candles:
        return None

    max_height = find_max_height(candles)
    tallest_count = count_tallest_candles(candles, max_height)
    symmetric = is_symmetric(candles, max_height)

    corrected_candles = candles

    if not symmetric:
        corrected_candles = make_symmetric(candles, max_height)

    return max_height, tallest_count, symmetric, corrected_candles


# Get input from the user
input_data = input(
    "Enter the candle heights separated by spaces: "
)

candles = list(map(int, input_data.split()))

# Analyze the candles
result = birthday_cake_candles(candles)

if result is None:
    print("No candles were entered.")
else:
    max_height, tallest_count, symmetric, corrected_candles = result

    print("\n--- Birthday Cake Candles Analysis ---")
    print("Max height:", max_height)
    print("Number of tallest candles:", tallest_count)
    print("Is symmetric:", symmetric)

    if not symmetric:
        print("Corrected candles:", corrected_candles)
import sys

def is_fibonacci_basecase(fib_sequence, fib_sequence_position):
    # True if we want the 1st or 2nd fibonacci numbers, which are both 1
    return fib_sequence_position in (1, 2)

def was_computed(fib_sequence, fib_sequence_position):
    return fib_sequence[fib_sequence_position] > 0

def fibonacci_sequence_to_n(fib_sequence_position):
    if fib_sequence_position <= 0: return -1

    new_fib_sequence = [0] * fib_sequence_position

    return recursive_fibonacci_sequence_to_n(new_fib_sequence, fib_sequence_position)

def recursive_fibonacci_sequence_to_n(fib_sequence, fib_sequence_position):
    fib_sequence_list_position = fib_sequence_position - 1

    if is_fibonacci_basecase(fib_sequence, fib_sequence_position):
        fib_sequence[fib_sequence_list_position] = 1

    if not was_computed(fib_sequence, fib_sequence_list_position):
        recursive_fibonacci_sequence_to_n(fib_sequence, fib_sequence_position - 2)
        recursive_fibonacci_sequence_to_n(fib_sequence, fib_sequence_position - 1)

        fib_sequence[fib_sequence_list_position] = (
              fib_sequence[fib_sequence_list_position - 2]
            + fib_sequence[fib_sequence_list_position - 1]
        )

    return fib_sequence

def print_fib_sequence(fib_sequence):
    numeric_width = len(str(fib_sequence[-1]))

    for fib_number in fib_sequence:
        sys.stdout.write(
            '\n\t{val:{nwidth}d}'.format(
                val=fib_number,
                nwidth=numeric_width
            )
        )

if __name__ == '__main__':
    try:
        fib_sequence_position = int(input('Please enter length of fibonacci sequence to generate: '))

        print_fib_sequence(fibonacci_sequence_to_n(fib_sequence_position))
        print()

    except Exception as err:
        print('Exception: {}\nterminating...'.format(err))


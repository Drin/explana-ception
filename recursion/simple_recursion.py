fib_fast_lookup = []

def is_fibonacci_basecase(fib_sequence_position):
    # True if we want the 1st or 2nd fibonacci numbers, which are both 1
    return fib_sequence_position in (0, 1)

def fibonacci_sum(fib_sequence_position):
    if fib_sequence_position < 0: return -1

    # we use extend, because standard assignment assigns to local variable, not
    # the global variable
    fib_fast_lookup.extend([0] * (fib_sequence_position + 1))

    return recursive_fibonacci_sum(fib_sequence_position)

def recursive_fibonacci_sum(fib_sequence_position):
    # this is just for accessing the correct position in the list data
    # structure
    if is_fibonacci_basecase(fib_sequence_position):
        fib_fast_lookup[fib_sequence_position] = 1

    elif fib_fast_lookup[fib_sequence_position] == 0:
        fib_fast_lookup[fib_sequence_position] = (
              recursive_fibonacci_sum(fib_sequence_position - 2)
            + recursive_fibonacci_sum(fib_sequence_position - 1)
        )

    return fib_fast_lookup[fib_sequence_position]

if __name__ == '__main__':
    fib_sequence_position = int(input('Please enter length of fibonacci sequence to generate: '))

    # change from 1-indexed to 0-indexed
    fib_sequence_position -= 1

    print('{}'.format(fibonacci_sum(fib_sequence_position)))

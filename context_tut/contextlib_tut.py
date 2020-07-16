import contextlib

@contextlib.contextmanager  # yield 앞까지가 __enter__, 이후가 __exit__
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    try:
        yield 'JABBERWOCKY'
    except ZeroDivisionError:
        msg = 'Please DO NOT divide by zero!'
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)


if __name__ == '__main__':
    with looking_glass() as glass:
        print("Hello world")
        print(glass)
        1 / 0
    print('-'*10)
    print(glass)
    print("Hello world")

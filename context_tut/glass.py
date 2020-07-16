class LookingGlass:
    def __enter__(self):  # enter는 self만을 인수로 받는다.
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'JABBERWOCKY'

    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_value, traceback):
        """정상 수행이 완료되면 None, None, None으로 이 method를 호출한다.
        exc_type: Exception class
        exc_value: Exception 객체
        traceback: traceback 객체
        """
        import sys
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Please DO NOT devide by zero!')
            return True  # None이나 True 이외의 값을 return하면 exception이 상위로 전달됨

if __name__ == '__main__':
    with LookingGlass() as glass:
        print("Hello world")
        print(glass)
        1 / 0
    print('-'*10)
    print(glass)
    print("Hello world")

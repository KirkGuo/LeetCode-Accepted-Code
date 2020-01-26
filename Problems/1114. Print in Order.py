class Foo:
    def __init__(self):
        self.mutex = 0

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        while self.mutex!=0: 
            pass
        printFirst()
        self.mutex = 1


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        while self.mutex!=1:
            pass
        printSecond()
        self.mutex = 2


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        while self.mutex!=2:
            pass
        printThird()
        self.mutex = 3

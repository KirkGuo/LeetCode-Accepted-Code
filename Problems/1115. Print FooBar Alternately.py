class FooBar:
    def __init__(self, n):
        self.n = n
        self.f = True
        self.b = False
        self.mutex = threading.Condition()


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        with self.mutex:
            for i in range(self.n):
                if self.b:
                    self.mutex.wait()
                printFoo()
                self.f = False
                self.b = True
                self.mutex.notify()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        with self.mutex:
            for i in range(self.n):
                if self.f:
                    self.mutex.wait()
                printBar()
                self.b = False
                self.f = True
                self.mutex.notify()

class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("JAR capacity must be positive")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if n > self._capacity or self._size + n > self._capacity:
            raise ValueError("NOT enough space in JAR")
        self._size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("NOT enough cookies in JAR")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    jar = Jar(8)
    print(jar.capacity)
    jar.deposit(8)
    jar.withdraw(2)
    print(jar.size)
    print(jar)

if __name__ == "__main__":
    main()
class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)

class Observer:
    def update(self, subject):
        pass

class ClockTimer(Subject):
    def __init__(self):
        super().__init__()
        self.hour = 0
        self.minute = 0
        self.second = 0

    def tick(self):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
        if self.minute == 60:
            self.minute = 0
            self.hour += 1
        self.notify()

class AnalogClock(Observer):
    def update(self, subject):
        print("Analog clock updated: {}:{}:{}".format(subject.hour, subject.minute, subject.second))

class DigitalClock(Observer):
    def update(self, subject):
        print("Digital clock updated: {}:{}:{}".format(subject.hour, subject.minute, subject.second))

def main():
    clock_timer = ClockTimer()
    analog_clock = AnalogClock()
    digital_clock = DigitalClock()

    clock_timer.attach(analog_clock)
    clock_timer.attach(digital_clock)

    for _ in range(10):
        clock_timer.tick()

if __name__ == "__main__":
    main()
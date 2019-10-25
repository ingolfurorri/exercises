class Clock:
    def __init__(self, clocks = "00:00:00"):
        #clock = clocks.split(":")
        self.hours = int(clocks.split(":")[0])
        self.minutes = int(clocks.split(":")[0])
        self.seconds = int(clocks.split(":")[0])
        
    def str_update(self, str_user):
        time_list = str_user.split(":")
        self.hours = int(time_list[0])

        self.minutes = int(time_list[1])

        self.seconds = int(time_list[2])



    def add_clocks(self, clock):
        clock3 = Clock()

        clock3.seconds = self.seconds + clock.seconds + clock3.seconds
        if(clock3.seconds > 59):
            clock3.minutes += 1
            clock3.seconds -= 60

        clock3.minutes = self.minutes + clock.minutes + clock3.minutes
        if(clock3.minutes > 59):
            clock3.hours += 1
            clock3.minutes -= 60

        clock3.hours = self.hours + clock.hours + clock3.hours
        if(clock3.hours > 23):
            clock3.hours -= 24

        return clock3


    def __str__(self):
        return "{} hours, {} minutes and {} seconds".format(self.hours, self.minutes, self.seconds)



clock1 = Clock()
clock2 = Clock()
clock1.str_update("20:10:52")
clock2.str_update("08:49:24")
print(clock1)


print(clock2)


clock3 = clock1.add_clocks(clock2)
print(clock3)

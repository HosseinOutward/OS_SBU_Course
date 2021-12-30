from multiprocessing import Pool as ThreadPool
from math import pi as TruePi

class PI_Integral:

    prec = 1000
    integSteps = 0.001
    ThreadCount = 32

    def __init__(self):
        self.prec = int(input("an int for Division error correction (default:1000) (slows computation drasticly for small gain in accurecy) "))
        self.integSteps = float(input("a float for Integral steps (default:0.001) (the more, the faster and less accurate) "))
        self.ThreadCount = int(input("an int for Thread Counts "))

    def integralRange(self, steps):
        s=[]
        a,b = steps,2*steps
        while b <= self.prec:
            s.append((a, b))
            a=b
            b+=steps
        return s

    def partialIntegral(self, range):
        # take a range from 0 to prec and calculates the Sumation (integral) segment of pi
        sum=0
        x=range[0]
        while x<range[1]:
            sum+=pow(pow(self.prec,2)-pow(x,2), 1/2)
            x+=self.integSteps
        return sum

    def calculatePI(self):
        # creates threads to calculate the integral segments, the brings them all in one number
        p = ThreadPool(self.ThreadCount)
        sums = p.map(self.partialIntegral, self.integralRange(self.prec / self.ThreadCount))
        sums.append(self.partialIntegral([0, (self.prec/self.ThreadCount)]))
        p.close()
        p.join()

        pi = 0
        for sum in sums:
            pi += sum
        return (4 * pi / pow(self.prec, 2)) * self.integSteps


if __name__ == '__main__':
    pi=PI_Integral().calculatePI()
    print(pi)
    print(str(int((1-TruePi/pi)*100*10000)/10000)+"% error")

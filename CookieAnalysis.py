#! /usr/bin/env python

# imports of external packages to use in our code 
import sys
import math
import numpy as np
import matplotlib.pyplot as plt

#import our Random class from /Random.py file
sys.path.append(".")
from MySort import MySort
#import sorting

# main function for our CookieAnalysis Python code
if __name__ == "__main__":
   
    haveInput = False

    for i in range(1,len(sys.argv)):
        if sys.argv[i] == '-h' or sys.argv[i] == '--help':
            continue

        InputFile = sys.argv[i]
        haveInput = True
    
    if '-h' in sys.argv or '--help' in sys.argv or not haveInput:
        print ("Usage: %s [options] [input file]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print
        sys.exit(1)
    
    Nmeas = 1
    times = []
    times_avg = []

    need_rate = True
    
    with open(InputFile) as ifile:
        for line in ifile:
            if need_rate:
                need_rate = False
                rate = float(line)
                continue
            
            lineVals = line.split()
            Nmeas = len(lineVals)
            t_avg = 0
            for v in lineVals:
                t_avg += float(v)
                times.append(float(v))

            t_avg /= Nmeas
            times_avg.append(t_avg)

    Sorter = MySort()

    times = Sorter.DefaultSort(times)
    times_avg = Sorter.DefaultSort(times_avg)
    # try some other methods! see how long they take
    # times_avg = Sorter.BubbleSort(times_avg)
    # times_avg = Sorter.InsertionSort(times_avg)
    # times_avg = Sorter.QuickSort(times_avg)
   


    # Code to calculate different quantiles from sorted arrays of outcomes
    # numpy.quantile() method
 
    # 1D array
    arr = [20, 2, 7, 1, 34]
 
    print("Q2 quantile of arr : ", np.quantile(times, .50))
    print("Q1 quantile of arr : ", np.quantile(arr, .25))
    print("Q3 quantile of arr : ", np.quantile(arr, .75))
    print("100th quantile of arr : ", np.quantile(arr, .1))



  
    fig1 = plt.figure()
    # plt.plot(times,p,'o-')
    plt.hist(times_avg, density=True, facecolor='b', alpha=0.5, label="assuming $\\mathbb{H}_0$")
    # plt.plot(sizes,[0.0248]*len(sizes),'--r')
    plt.grid()
    plt.xlim(xmin=0)
    plt.xlabel('Time')
    plt.ylabel('Frequency of Outcomes')
    plt.title('Distribution of Outcomes from Input File')

    plt.show()

    fig1.savefig('cookieplot.png')

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def local_computation(number):

    source1 = pd.read_csv("local_data/local_source1.csv", engine='python')
    source2 = pd.read_csv("local_data/local_source2.csv", engine ='python')
    merge1_2 = source1.merge(source2, left_on='film', right_on='film', how='outer')
    source3 = pd.read_csv("local_data/local_source3.csv", engine='python')
    data = merge1_2.merge(source3, left_on='film', right_on='film', how='outer')


    print("**Text Part**")
    print(data.head(int(number)))
    print("\n**Plot Part**")
    print("--These are the probability distributions of awards, nominations and their ratios for 170 films that are awarded more than three times.\n")
    print("--From the Nomination Density Distribution, we can see it is almost a normal one with its mean at 8.5\n")
    print("--From the Awards/Nominations Density Distribution, we can infer that the largest probability of awards is 40%\-45%\ of the number of nominations. And this probability is nearly 30%\n")


    f, (ax1, ax2) = plt.subplots(1, 2, sharey = True, sharex = True )
    ax1.set_title('Awards Density Distribution')
    ax1.hist(data.awards)
    ax1.set_ylabel('Probability')
    ax1.set_xlabel('Awards')
    ax2.set_title('Nominations Density Distribution')
    ax2.hist(data.nominations)
    ax2.set_xlabel('Nominations')

    plt.figure(2)
    plt.hist(data.awards_ratio, 16,  facecolor='g', alpha=0.75)
    plt.title('Awards/Nominations Ratio Distribution')
    plt.xlabel("Awards/Nominations")
    plt.ylabel("Probability")

    plt.show()

    print("\n***Above is the integrated local sources! Thanks for using!***\n")

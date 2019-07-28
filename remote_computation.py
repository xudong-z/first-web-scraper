import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def remote_computation():

    # read the saved source1/2/3 and join them together
    source1 = pd.read_csv("remote_data/remote_source1.csv", engine='python')
    source2 = pd.read_csv("remote_data/remote_source2.csv", engine ='python')
    merge1_2 = source1.merge(source2, left_on='film', right_on='film', how='outer')
    source3 = pd.read_csv("remote_data/remote_source3.csv", engine='python')
    data = merge1_2.merge(source3, left_on='film', right_on='film', how='outer')

    # return the DataFrame of what we extract from source1/2/3
    print("**Summary: Text Part**")
    print("--Below is the information extracted from source1/2/3")
    print(data)

    # return the plots about awards/nominations/ratios of selected films
    print("\n**Summary: Plot Part**")
    print("--These are the probability distributions of awards, nominations and their ratios for your selected films that are awarded more than three times.\n")
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

    print("\n***Above is the integrated remote sources1/2/3! Thanks for using!***\n")

import sys

from plots import plotting


# main program that runs experiments
def main(data_file):
    # plotting results
    print('Plotting results...')
    plotting.plot_results(data_file)
    print('Results plotted.')


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print('Please provide the path of the data file in the correct format...')

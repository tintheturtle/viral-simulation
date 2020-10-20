from collections import Counter

def read_file():

    output = ""
    with open('outbreak_output.txt', 'r') as f:
        output = f.readlines()

    split_index = output.index("\n")

    output = [s.strip('\n') for s in output]

    probabilities = output[:split_index]
    average_days = output[split_index:]
    return probabilities, average_days



if __name__ == "__main__":
    prob, ave_day = read_file()
    count = Counter(ave_day)
    print(count)
    print(len(prob), len(ave_day))
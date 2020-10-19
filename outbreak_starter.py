import sys
import random

############################

# DO NOT CHANGE THIS PART!!

############################

def readGraph(input_file):
    with open(input_file, 'r') as f:
        raw = [line.split(',') for line in f.read().splitlines()]

    N = int(raw[0][0])
    sin = raw[1]
    s = []
    for st in sin:
        s.append(int(st))
    adj_list = []
    for line in raw[2:]:
        if line == ['-']:
            adj_list.append([])
        else:
            adj_list.append([int(index) for index in line])
    return N, s, adj_list

def writeOutput(output_file, prob_infect, avg_day):
    with open(output_file, 'w') as f:
        for i in prob_infect:
            f.write(str(i) + '\n')
        f.write('\n')
        for i in avg_day:
            f.write(str(i) + '\n')

 

def Run(input_file, output_file):
    N, s, adj_list = readGraph(input_file)
    prob_infect, avg_day =   model_outbreak(N, s, adj_list)
    writeOutput(output_file, prob_infect, avg_day)


def  BFS(N, s, adj_list):
    level = ['x'] * N
    #######################################

    # COPY YOUR BFS CODE FROM PART 1 HERE

    ########################################

    Q = [s]
    visited = [False] * N
    visited[s] = True
    level[s] = 0
    while Q:
        vertex = Q.pop()

        if adj_list[vertex] != []:
            for neighbor in adj_list[vertex]:
                if not visited[neighbor]:
                    level[neighbor] = level[vertex] + 1
                    Q.insert(0, neighbor)
                    visited[neighbor] = True
    return level

#######################################

# WRITE YOUR SOLUTION IN THIS FUNCTION

########################################

def model_outbreak(N, s, adj_list):
    # You can also call your BFS algorithm in this function,
    # or write other functions to use here.
    # Return two lists of size n, where each entry represents one vertex:

    prob_infect = [0] * N       # the probability that each node gets infected after a run of the experiment
    
    avg_day = ['inf'] * N       # the average day of infection for each node 
                                # (you can write 'inf' for infinity if the node is never infected)

    # The code will write this information to a single text file.
    # If you do not name this file at the command prompt, it will be called 'outbreak_output.txt'.
    # The first N lines of the file will have the probability infected for each node.
    # Then there will be a single space.
    # Then the following N lines will have the avg_day_infected for each node.
    
    # probability = [0.1, 0.3, 0.5, 0.7]

    # Initialize variables for experiments
    edges = [ [] for _ in range(N + 1) ]        # List of edges
    sources = s                                 # Source of infection
    edges[ N ] = s                              # Root of all infection
    runs = []

    p = 0.1

    allSources = [False] * N
    
    # Duration of infection spread
    for k in range(100):

        # Generate infection edges
        added = []
        for i in sources:
            for j in range(len(adj_list[i])):
                active = random.random()
                if active <= p:
                    if adj_list[i][j] not in edges[i]:
                        edges[i].append(adj_list[i][j])
                    if not allSources[adj_list[i][j]]:
                        added.append(adj_list[i][j])
                        allSources[adj_list[i][j]] = True

                    # if prob_infect[adj_list[i][j]] == 0:
                    #     prob_infect[adj_list[i][j]] = p
                    # else:
                    #     prob_infect[adj_list[i][j]] *= p

        # Update new sources of infection
        sources = added

        # Run BFS to retrieve infected nodes 
        infections = BFS(N + 1, N, edges)
        runs.append(infections)
        
    # Update probabilities infected and average days
    for col in range(len(runs[0]) - 1):
        day = 0
        divider = 0
        for row in range(len(runs)):
            if runs[row][col] != 'x':
                day += runs[row][col]
                divider += 1
        if day != 0:
            avg_day[col] = day / divider
    return prob_infect, avg_day



############################

# DO NOT CHANGE THIS PART!!

############################


# read command line arguments and then run
def main(args=[]):
    filenames = []

    #graph file
    if len(args)>0:
        filenames.append(args[0])
        input_file = filenames[0]
    else:
        print()
        print('ERROR: Please enter file names on the command line:')
        print('>> python outbreak.py graph_file.txt output_file.txt')
        print()
        return

    # output file
    if len(args)>1:
        filenames.append(args[1])
    else:
        filenames.append('outbreak_output.txt')
    output_file = filenames[1]

    Run(input_file, output_file)


if __name__ == "__main__":
    main(sys.argv[1:])    

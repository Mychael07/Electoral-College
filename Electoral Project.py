import random

import matplotlib.pyplot as plt

def read_data(file_name):
    data = open(file_name)
    results = []
    data.readline()
    for row in data.readlines():
        row = row.split(',')
        results.append(tuple([row[0], int(row[1]), row[2].strip()]))
    data.close()
    return results

def get_party_counts(states, party):
    party_sum = 0
    for state in states:
        if state[2] == party:
            party_sum += state[1]
    return party_sum

def generate_bar_plot(data):
    for party in ['R', 'B', 'P']:
        count = get_party_counts(data, party)
        plt.bar(party, count, color=party.lower() if party != 'P' else 'm')
    plt.show()
    
if __name__ == '__main__':
    data = read_data('electoral_data.csv')
    print(data)
    generate_bar_plot(data)
    number_of_times_R_wins = 0
    number_of_times_B_wins = 0
    for simulations in range(100):
        simulation_run = []
        for state in data:
            if state[2] == 'P':
                party_choice = random.choice(['R', 'B'])
                state = (state[0], state[1], party_choice)
            simulation_run.append(state)
        R_count = get_party_counts(simulation_run, 'R')
        B_count = get_party_counts(simulation_run, 'B')
        if R_count > B_count:
            print("R won!")
            number_of_times_R_wins += 1
        elif B_count > R_count:
            print("B won!")
            number_of_times_B_wins += 1
        else:
            print("It was a tie!")
            print("Number of times R won: ", number_of_times_R_wins)
            print("Number of times B won: ", number_of_times_B_wins)
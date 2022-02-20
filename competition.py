import time 
from itertools import chain


def resolve_winner(competitions, results, n):
    participants = dict()
    # flatten our competitor versus list so that we can have dictionary hold all individual compeititor values
    for char in list(chain.from_iterable(competitions)):
        if char not in participants:
            participants[char] = 0
    
    # iterate through competitions and results and assign points to individual teams
    for i in range(n):
        competition = competitions[i]
        #print(competition)
        result = results[i]
        #print(result)
        if result == 0:
            participants[competition[1]] += 3
        if result == 1:
            participants[competition[0]] += 3
        
    print(participants)
    
    return max(participants, key = participants.get)
    


if __name__ == "__main__":
    start_time = time.time()
    competitions = []
    n = int(input("Enter number of competitions:"))
    for i in range(n):
        competition = input('Enter home team and away team: ').split(' ')
        competitions.append(competition)
        
    results = list(map(int, input('Enter list of results 0 or 1: ').split(' ')))
    
    winner = resolve_winner(competitions, results, n)
    print("\n", winner)
    print("%f seconds" % (time.time() - start_time))
    
    
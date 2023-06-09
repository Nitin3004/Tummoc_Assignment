def vote(candidate):
    global vote_counts

    if candidate in vote_counts:
        vote_counts[candidate] += 1
        return True
    else:
        return "Invaid_Ballot"

def print_winner():
    max_votes = max(vote_counts.values())
    winners = [candidate for candidate, votes in vote_counts.items() if votes == max_votes]

    print("Winners")
    for winner in winners:
        print(winner)
    print()


vote_counts = {"Candidate A":0,"Candidate B":0,"Candidate C":0}

vote("Candidate A")
vote("Candidate B")
vote("Candidate A")
vote("Candidate C")
vote("Candidate B")
vote("Candidate A")
vote("Candidate B")
vote("Candidate C")
vote("Candidate C")

print_winner()

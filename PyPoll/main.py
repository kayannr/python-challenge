import csv
import os 

file_to_load = os.path.join('C:/Users/kayan/UCBWork/python-challenge/PyPoll/raw_data/election_data.csv')
file_to_output = os.path.join('analysis','election_data_analysis.txt')

with open(file_to_load, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    unique_list = []
    total_votes = 0

    for row in csvreader:
        if row[2] not in unique_list: 
            unique_list.append(str(row[2])) 
        total_votes = total_votes +1 

with open(file_to_load, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    vote1 = 0
    vote2 = 0
    vote3 = 0
    vote4 = 0 

    for row in csvreader:   #count votes
        if row[2] == unique_list[0]:
            vote1 = vote1 + 1 
        elif row[2] == unique_list[1]:
            vote2 = vote2 +1 
        elif row[2] == unique_list[2]:
            vote3 = vote3 +1 
        elif row[2] == unique_list[3]:
            vote4 = vote4 +1 
    percent1 = float((vote1/total_votes)*100) #calculate percentages
    percent2 = float((vote2/total_votes)*100)
    percent3 = float((vote3/total_votes)*100)
    percent4 = float((vote4/total_votes)*100)

    summ_list = [
        {'name': unique_list[0], 'percent': percent1, 'vote': vote1},
        {'name': unique_list[1], 'percent': percent2, 'vote': vote2},
        {'name': unique_list[2], 'percent': percent3, 'vote': vote3},
        {'name': unique_list[3], 'percent': percent4, 'vote': vote4}
    ]

    find = [i['vote']  for i in summ_list]  #find the highest vote in list of dicts
    highest_vote = max (find)
    
    for i in summ_list: #find winner
        if i['vote'] == highest_vote:
            winner = i['name']

output = (
    f"\nElection Results\n"
    f"-----------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-----------------------\n"  
    f"{unique_list[0]}: {percent1:.3f}% ({vote1})\n"
    f"{unique_list[1]}: {percent2:.3f}% ({vote2})\n"
    f"{unique_list[2]}: {percent3:.3f}% ({vote3})\n"
    f"{unique_list[3]}: {percent4:.3f}% ({vote4})\n"
    f"------------------------\n"
    f"Winner: {winner}\n"
    f"------------------------\n" )
print(output)

with open(file_to_output, "a") as txt_file:
    txt_file.write(output)
    

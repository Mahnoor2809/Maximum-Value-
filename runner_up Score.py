print(" \n Participants' Score_Sheet Of University Sports Day  ")
scores = [8, 5, 6, 7, 4, 6, 8, 7]
print(scores[:])
print(" Runner-Up Score : ")
r = max(scores)
#print(max(scores))     #For maximum Score
while max(scores) == r:
    scores.remove(max(scores))
print(max(scores))      #For Runner Up Score

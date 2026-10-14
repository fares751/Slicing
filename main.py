# Challenge 1 - Basic Slicing
title = "The Zen of Python"
print("Extract 'Zen':", title[4:7])  # What would be the result? Answer: Zen
print("Extract 'The Zen':", title[:7])  # What would be the result? Answer: The Zen
print("Extract 'Zen of Python':", title[4:])  # What would be the result? Answer: Zen of Python
print("Extract 'thon' using negative indexing:", title[-4:])  # What would be the result? Answer: thon

# Challenge 2 - Phone Number Slicing
num = "+1-(123)-456-7890"
print("Extract country code:", num[1:3])  # What would be the result? Answer: 1
print("Extract last 4 digits:", num[-4:])  # What would be the result? Answer: 7890

# Extract a stripped version with only digits (1234567890)
stripped_num = num[3:6] + num[8:11] + num[12:16]
print("Stripped phone number:", stripped_num)  # What would be the result? Answer: 1234567890

# Challenge 3 - Simple Cypher String
cypher = "SILTFEEwhasiePwsrnhAps.kliDliuvdnta.theQlbjvePaE.sT"
print("Deciphered string (odd indices):", cypher[1::2])  # What would be the result? Answer: ITEwashrnsasilitudattheblvea.s

# Challenge 4 - Big Cypher
cypher = "...Zhmfhsnto.Xgcth.ahS...rvdjsnyar.edgy ydrcresayuEpdPy"
print("Every 7th letter starting from the 6th:", cypher[5::7])  # What would be the result? Answer: hnydcey
print("Every 11th letter going backwards starting from the 70th:", cypher[69::-11])  # What would be the result? Answer: yed.
print("Even letters between the 14th and 23rd letter:", cypher[13:23:2])  # What would be the result? Answer: .ts
print("Every 10th letter between the 80th and 83rd letter:", cypher[79:83:10])  # What would be the result? Answer: P

# Challenge 5 - Chess Competition
players = [
    "Mohamed Ahmed", "Sophia Lee", "Isabella Rodriguez", "Liam Smith",
    "Emma Johnson", "Olivia Brown", "Noah Davis", "Ava Wilson",
    "William Martinez", "James Anderson", "Lucas Thomas", "Mia Jackson",
    "Ethan White", "Amelia Harris", "Michael Clark"
]

print("First place (Winner):", players[0])  # What would be the result? Answer: Mohamed Ahmed
print("Last place:", players[-1])  # What would be the result? Answer: Michael Clark
print("Players in 5th to 10th places:", players[4:10])  # What would be the result? Answer: ['Emma Johnson', 'Olivia Brown', 'Noah Davis', 'Ava Wilson', 'William Martinez', 'James Anderson']
print("Players in 1st and 10th places:", players[0], players[9])  # What would be the result? Answer: Mohamed Ahmed, James Anderson
print("Bottom 10 players:", players[-10:])  # What would be the result? Answer: ['Isabella Rodriguez', 'Liam Smith', 'Emma Johnson', 'Olivia Brown', 'Noah Davis', 'Ava Wilson', 'William Martinez', 'James Anderson', 'Lucas Thomas', 'Mia Jackson']
print("Players in 5th, 10th, and 15th places:", players[4], players[9], players[14])  # What would be the result? Answer: Emma Johnson, James Anderson, Michael Clark
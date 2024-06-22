### QUESTION 2

List = ["Ayşe: 75-78", "Berk: 80-60", "Can: 58-61", "Didem: 34-45","Erdem: 32-37", "Fatih: 69-75", "Gül: 54-63"]
students = [] # for students name 
score = [] # for exams notes
average_list = [] #average notes of exam1 and exam2 
# 
for i in List:
    names_score= i.split(": ") #names and notes separated
    students.append(names_score[0]) #After the separated process, the names were transferred to the students list
    # The notes of exam1 and exam2 were transferred to list of score, separated from each other, and each value was converted to integer
    score.extend(names_score[1].split("-")) 
    score = [int(number) for number in score] 
# The notes on the list into pairs and their averages were taken.
for j in range(0, len(score)-1, 2):
      averages = (score[j] + score[j + 1]) / 2
      average_list.append(averages)
      
#Two lists with students and average_list were matched using zip
students_average = list(zip(students,average_list))  
#Using lambda in the key parameter allowed the second element of each list item (notes only) to be sorted
students_average.sort(key=lambda x: x[1], reverse= True) #with reverse=True order was made from largest to smallest.
print(students_average[:3]) # display top 3 students


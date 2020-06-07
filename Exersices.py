class Exersice:
    def __init__(self, topic, course_name, judge_link, problems):
        self.topic=topic
        self.course_name=course_name
        self.judge_link=judge_link
        self.problems_list=problems
data=input().split(" -> ")
exersice_list=[]
while not data[0]=="go go go":
    topic_name=data[0]
    course_name=data[1]
    judge_link=data[2]
    problems=data[3].split(", ")
    exersice=Exersice(topic_name, course_name, judge_link, problems) #vlizane v class
    exersice_list.append(exersice) #dobavqne v listb za da ne go zagubq
    data = input().split(" -> ")

for exersice in exersice_list:
    print(f"Exersice: {exersice.topic}") #dostupvane
    print(f"Problems for exercises and homework for the \"{exersice.course_name}\" course @ SoftUni.") #kavichki
    print(f"Check your solutions here: {exersice.judge_link}")
    counter=0
    for problem in exersice.problems_list: #vlizane v list
        counter+=1
        print(f"{counter}. {problem}")

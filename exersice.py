class Exersice:
    def __init__(self,topic, course_name, judjelink, problems):
        self.topic=topic
        self.course_name=course_name
        self.judjelink=judjelink
        self.problems_list=problems

data=input().split(" -> ")
exersice_list=[]

while not data[0]=="go go go":
    topic_name=data[0]
    course_name=data[1]
    judjelink=data[2]
    problems=data[3].split(", ")
    exersice=Exersice(topic_name, course_name, judjelink, problems)
    exersice_list.append(exersice)
    
    data=input().split(" -> ")
    
for exersice in exersice_list:
    print(f"Exercises: {exersice.topic}")
    print(f'Problems for exercises and homework for the "{exersice.course_name}" course @ SoftUni.')
    print(f"Check your solutions here: {exersice.judjelink}")
    counter=1
    for p in exersice.problems_list:
        print(f"{counter}. {p}")
        counter+=1
    

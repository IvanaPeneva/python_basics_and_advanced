topic_dict={}
data=input().split(" -> ")
while not data[0]=="filter":
    topic=data[0]
    tag=data[1].split(", ")
    if topic not in topic_dict.keys():
        topic_dict[topic]=tag
    else:
        if tag in topic_dict[topic]:
            data=input().split(" -> ")
            continue
        else:
            topic_dict[topic].append(tag)
    data=input().split(" -> ")

filter_input=input().split(", ")
for key,value in topic_dict.items():
    counter=0
    for el in filter_input:
        if el in topic_dict[key]: #ako el se namira v key kato value
            counter+=1
            if counter==len(topic_dict):
                a=", "
                b="#"
                lista=[b + val for val in value]
                print(f"{key}| {a.join(lista)}")

data=input().split()
post_dict={}
while not data[0]=="drop":
    command=data[0]
    post_name=data[1]
    if command=="post":
        post_dict[post_name]={"likes":0, "dislikes":0, "comments":None} #dict in dict
    elif command=="like":
        if post_name in post_dict.keys():
            post_dict[post_name]["likes"]+=1  #dopuskane na dict ot dict vuv value na 2 dict
    elif command == "dislike":
        if post_name in post_dict.keys():
            post_dict[post_name]["dislikes"] += 1
    elif command == "comment":
        commentator=data[2]
        content=" ".join(data[3:]) #ot 3ti do kraq index !!!
        if post_name in post_dict.keys():
            if not post_dict[post_name]["comments"]:
                post_dict[post_name]["comments"]=[]
            post_dict[post_name]["comments"].append({commentator: content}) #vajno 3 dict v 1
    data=input().split()
for post_name, metrics in post_dict.items(): #vajnoo #print
    print(f"Post: {post_name} | Likes: {metrics['likes']} | Dislikes: {metrics['dislikes']}")
    print("Comments:")
    if metrics["comments"]:  #=True #ako sushtestvuva if ot prazen list dava nishto (ne None)
        for comment in metrics["comments"]:  #dict in dict for in for
            for kvp in comment.items():
                print(f"*  {kvp[0]}: {kvp[1]}")
    else:
        print("None")
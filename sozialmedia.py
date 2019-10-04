data = input().split()
 
post= {}
 
while not data[0] == "drop":
    command = data[0]
    post_name = data[1]
 
 
    if command == "post":
        post[post_name] = {'likes': 0, 'dislikes': 0, 'comments': None}
    elif command == "like":
        if post_name in post.keys():
            post[post_name]['likes'] += 1
    elif command == "dislike":
        if post_name in post.keys():
            post[post_name]['dislikes'] += 1
    elif command == "comment":
        commentator = data[2]
        content = ' '.join(data[3:])
        if post_name in post.keys():
            if not post[post_name]['comments']:
                post[post_name]['comments'] = []
 
            post[post_name]['comments'].append({commentator: content})
 
    data = input().split()
 
for post_name, metrics in post.items():
    print(f"Post: {post_name} | Likes: {metrics['likes']} | Dislikes: {metrics['dislikes']}")
    print("Comments:")
    if metrics['comments']:
        for comment in metrics['comments']:
            for kvp in comment.items():
                print(f"*  {kvp[0]}: {kvp[1]}")
    else:
        print(None)

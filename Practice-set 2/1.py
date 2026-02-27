user = {
    "username": "aayush_mani",
    "posts": [
        {
            "post_id": 1,
            "comments": [
                {"comment_id": 101, "likes": 5},
                {"comment_id": 102, "likes": 12}
            ]
        },
        {
            "post_id": 2,
            "comments": [
                {"comment_id": 103, "likes": 0},
                {"comment_id": 104, "likes": 8},
                {"comment_id": 105, "likes": 20}
            ]
        }
    ]
}

def calculate(data):
    total_likes = 0
    
    posts = data.get("posts", [])
    
    for post in posts:
        comments = post.get("comments", [])
        
        for comment in comments:
            likes = comment.get("likes", 0)
            
            total_likes += likes
            
    return total_likes

final_likes_count = calculate(user)

print(final_likes_count)
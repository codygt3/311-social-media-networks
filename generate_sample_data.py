from faker import Faker
import random
import json

fake = Faker()

def generate_sample_data(num_users=10, num_posts=20):
    users = {}
    posts = {}

    # Generate user data with formatted usernames
    for i in range(num_users):
        first_name = fake.first_name()
        last_name = fake.last_name()
        random_numbers = random.randint(100, 999)
        user_name = f"{first_name}{last_name}{random_numbers}"
        
        users[user_name] = {
            "user_name": user_name,
            "age": random.randint(18, 65),
            "gender": random.choice(["male", "female", "non-binary"]),
            "location": fake.city(),
            "connections": {"follows": [], "friends": [], "blocked": []},
            "posts": [],
            "seen_posts": []
        }

    # Generate post data with adjusted content length and add to random users
    for i in range(num_posts):
        post_id = f"post{i+1}"
        author = random.choice(list(users.keys()))
        post_content = fake.sentence(nb_words=random.randint(8, 30))  # Post content between 8 and 30 words
        post_timestamp = fake.date_time_this_year()  # Keep as a datetime object initially
        
        post = {
            "post_id": post_id,
            "content": post_content,
            "comments": [],
            "views": [],
            "timestamp": post_timestamp  # Save as datetime for now
        }
        users[author]["posts"].append(post_id)
        posts[post_id] = post

    # Randomly assign connections, comments, and views with valid timestamps
    for user_name, user_data in users.items():
        # Randomly add connections
        user_data["connections"]["follows"] = random.sample(
            list(users.keys()), random.randint(0, 3)
        )
        user_data["connections"]["friends"] = random.sample(
            list(users.keys()), random.randint(0, 2)
        )
        user_data["connections"]["blocked"] = random.sample(
            list(users.keys()), random.randint(0, 1)
        )

        # Add comments and views to each post with adjusted timestamps
        for post_id in user_data["posts"]:
            post_creation_time = posts[post_id]["timestamp"]
            
            # Generate comments with timestamps after the post creation
            for _ in range(random.randint(0, 3)):  # Random number of comments per post
                commenter = random.choice(list(users.keys()))
                comment_content = fake.sentence(nb_words=random.randint(4, 12))  # Comment content between 4 and 12 words
                comment_time = fake.date_time_between(start_date=post_creation_time)

                comment = {
                    "user": commenter,
                    "content": comment_content,
                    "timestamp": comment_time.isoformat()
                }
                posts[post_id]["comments"].append(comment)

            # Generate views with timestamps after the post creation
            for _ in range(random.randint(0, 5)):  # Random number of views per post
                viewer = random.choice(list(users.keys()))
                view_time = fake.date_time_between(start_date=post_creation_time)

                view = {
                    "user": viewer,
                    "timestamp": view_time.isoformat()
                }
                posts[post_id]["views"].append(viewer)

    # Populate 'seen_posts' for each user
    for user_name, user_data in users.items():
        # Randomly choose posts for each user's seen_posts
        seen_posts = random.sample(list(posts.keys()), random.randint(1, min(5, num_posts)))
        user_data["seen_posts"] = seen_posts

    # Convert post timestamps to ISO format for JSON compatibility
    for post_id, post_data in posts.items():
        post_data["timestamp"] = post_data["timestamp"].isoformat()

    # Combine users and posts in a single dictionary to export
    return {"users": users, "posts": posts}

# Save generated data to JSON file
if __name__ == "__main__":
    data = generate_sample_data()
    with open("sample_data.json", "w") as f:
        json.dump(data, f, indent=4)

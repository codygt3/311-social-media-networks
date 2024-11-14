# 311-social-media-networks

## Getting Started

To get started, you can either use the pre-generated sample dataset (`sample_data.json`) or generate a fresh dataset by running the `generate_sample_data.py` file.

### Dependencies

- **Faker**: Required only if you plan to generate a new sample dataset. Install with:
  ```bash
  pip install faker
## Dataset Structure

The dataset is stored in `sample_data.json` and contains two main components: **users** and **posts**.

### Users

Each user in the "users" dictionary is identified by a unique `user_name` and includes personal details, connections, posts, and seen posts.

#### User Structure

```json
{
    "user_name": "RobertBrock658",
    "age": 48,
    "gender": "male",
    "location": "Jeffreyfurt",
    "connections": {
        "follows": ["DillonWise901", "AliciaBryant971"],
        "friends": ["MatthewCastro360", "CameronSmall507"],
        "blocked": []
    },
    "posts": ["post1", "post2"],       # List of post IDs authored by this user
    "seen_posts": ["post7", "post16"]  # List of post IDs this user has viewed
}
```

#### Key Attributes

- **`connections`**: Contains three types of lists:
  - **`follows`**: Users this user follows.
  - **`friends`**: Mutual connections or friends.
  - **`blocked`**: Users this user has blocked.
- **`posts`**: List of IDs for posts authored by this user.
- **`seen_posts`**: List of IDs for posts this user has viewed.

### Posts

Each post in the "posts" dictionary is identified by a unique `post_id` and includes the post content, comments, views, and timestamp of creation.

#### Post Structure

```json
{
    "post_id": "post2",
    "content": "Sample content for the post.",
    "comments": [
        {
            "user": "ReneeMorrison356",
            "content": "Sample comment content.",
            "timestamp": "2024-09-17T13:44:30"
        }
    ],
    "views": ["MatthewCastro360", "KatherineSmith381"],
    "timestamp": "2024-07-09T18:58:49"
}
```

#### Key Attributes

- **`content`**: The main text content of the post.
- **`comments`**: A list of dictionaries, each representing a comment on the post:
  - **`user`**: The username of the commenter.
  - **`content`**: Text of the comment.
  - **`timestamp`**: When the comment was made.
- **`views`**: List of usernames for users who have viewed the post.
- **`timestamp`**: The creation timestamp of the post, in ISO format.

### Practical Examples

Here are some example queries you can make to navigate the dataset:

- **Get all posts authored by a specific user**:
  ```python
  user_data = dataset["users"]["RobertBrock658"]
  user_posts = [dataset["posts"][post_id] for post_id in user_data["posts"]]
  ```

- **Get all users who viewed a specific post**:
  ```python
  post_views = dataset["posts"]["post2"]["views"]
  ```

- **Get all comments for a specific post**:
  ```python
  post_comments = dataset["posts"]["post2"]["comments"]
  ```
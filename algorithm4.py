from datetime import datetime

def generate_trending_posts_report(dataset, include_keywords=None, exclude_keywords=None, user_attributes=None, time_window_days=30):
    """
    Produces a report of trending posts based on view rate and allows for filtering.

    Parameters:
        dataset (dict): The social media dataset containing users and posts.
        include_keywords (list): Keywords to include in filtering posts.
        exclude_keywords (list): Keywords to exclude from filtering posts.
        user_attributes (dict): Filters for user attributes (e.g., age, gender, location).
        time_window_days (int): The time window in days to calculate trending posts.

    Returns:
        None: Prints a report of trending posts.
    """
    # Initialize variables
    trending_posts = []

    # Filter users based on attributes if provided
    filtered_users = dataset['users']
    if user_attributes:
        filtered_users = {
            user_id: user_data
            for user_id, user_data in dataset['users'].items()
            if all(user_data.get(attr) == value for attr, value in user_attributes.items())
        }

    # Collect posts from filtered users
    filtered_posts = [
        dataset['posts'][post_id]
        for user_id, user_data in filtered_users.items()
        for post_id in user_data.get('posts', [])
    ]

    # Get the current time for trending calculations
    current_time = datetime.now()

    # Filter posts by keywords and calculate trending rates
    for post in filtered_posts:
        content = post['content'].lower()
        views = post.get('views', [])
        timestamp = datetime.strptime(post['timestamp'], "%Y-%m-%dT%H:%M:%S")

        # Include/exclude keyword filters
        if include_keywords and not any(keyword.lower() in content for keyword in include_keywords):
            continue
        if exclude_keywords and any(keyword.lower() in content for keyword in exclude_keywords):
            continue

        # Calculate views within the time window
        recent_views = [
            view for view in views
            if (current_time - timestamp).days <= time_window_days
        ]
        view_rate = len(recent_views) / ((current_time - timestamp).days + 1)  # Avoid division by zero

        trending_posts.append({
            "post_id": post['post_id'],
            "content": post['content'],
            "view_rate": view_rate,
            "total_views": len(views),
            "timestamp": post['timestamp']
        })

    # Sort posts by view rate
    trending_posts.sort(key=lambda x: x['view_rate'], reverse=True)

    # Generate the report
    if trending_posts:
        print("\nTrending Posts Report:")
        print(f"{'Post ID':<10} {'View Rate':<15} {'Total Views':<15} {'Timestamp':<20} Content")
        print("-" * 80)
        for post in trending_posts:
            print(f"{post['post_id']:<10} {post['view_rate']:<15.2f} {post['total_views']:<15} {post['timestamp']:<20} {post['content'][:50]}...")
    else:
        print("No trending posts found based on the specified filters.")

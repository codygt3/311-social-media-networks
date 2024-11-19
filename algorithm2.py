import matplotlib.pyplot as plt

def generate_interesting_user_network_diagram(dataset, attributes=None, min_posts=None, max_reading_level=None):
    """
    Generates a two-dimensional diagram of the social media data, showing posts and users as nodes
    and edges corresponding to authorship or viewing connections. Highlights interesting users based on various
    attributes or criteria.

    Parameters:
        dataset (dict): The social media dataset containing users and posts.
        attributes (dict, optional): A dictionary specifying user attributes to filter by (e.g., {"gender": "female"}).
        min_posts (int, optional): Minimum number of posts required to consider a user interesting.
        max_reading_level (int, optional): Maximum number of views for posts to consider a user interesting.

    Returns:
        None
    """
    # Create an index for quick lookup
    user_posts_count = {username: len(user_data['posts']) for username, user_data in dataset['users'].items()}
    post_view_count = {post_id: len(post_data['views']) for post_id, post_data in dataset['posts'].items()}

    # Create the graph structure with nodes and edges
    nodes = {}  # Dictionary to store users and posts
    edges = []  # List to store edges between nodes

    # Add user and post nodes
    for username, user_data in dataset['users'].items():
        nodes[username] = {
            'type': 'user',
            'data': user_data,
            'highlighted': False  # Track if the user is interesting
        }

    for post_id, post_data in dataset['posts'].items():
        nodes[post_id] = {
            'type': 'post',
            'data': post_data
        }

        # Create an edge from author to post
        author = next((username for username, user_data in dataset['users'].items() if post_id in user_data['posts']), None)
        if author:
            edges.append((author, post_id, 'authored'))

        # Create edges for views
        for viewer in post_data['views']:
            if viewer in nodes:
                edges.append((post_id, viewer, 'viewed'))

    # Find interesting users based on the inputted attributes
    for username, node in nodes.items():
        if node['type'] == 'user':
            user_data = node['data']
            meets_criteria = True

            # Check user attributes
            if attributes:
                for key, value in attributes.items():
                    if str(user_data.get(key)) != value:
                        meets_criteria = False
                        break

            # Check the minimum number of posts
            if min_posts is not None and user_posts_count[username] < min_posts:
                meets_criteria = False

            # Check the view count
            if max_reading_level is not None:
                for post_id in user_data['posts']:
                    if post_view_count.get(post_id, 0) > max_reading_level:
                        meets_criteria = False
                        break

            if meets_criteria:
                node['highlighted'] = True

    # Show graph
    plt.figure(figsize=(14, 10))
    for node_id, node_info in nodes.items():
        if node_info['type'] == 'user':
            color = 'orange' if node_info['highlighted'] else 'lightblue'
            plt.scatter(*get_random_position(), color=color, label='User' if not node_info['highlighted'] else 'Interesting User', s=100)
            plt.text(*get_random_position(), node_id, fontsize=8)
        elif node_info['type'] == 'post':
            plt.scatter(*get_random_position(), color='lightgreen', label='Post', s=70)
            plt.text(*get_random_position(), node_id, fontsize=8)
    for start, end, relation in edges:
        x_start, y_start = get_random_position()
        x_end, y_end = get_random_position()
        plt.plot([x_start, x_end], [y_start, y_end], 'k-', alpha=0.5)
    plt.title('Social Media Network Diagram')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

# Calculate random placement of nodes
def get_random_position():
    import random
    return random.uniform(0, 10), random.uniform(0, 10)

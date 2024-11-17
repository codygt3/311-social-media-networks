from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re

def generate_word_cloud(dataset, include_keywords=None, exclude_keywords=None, user_attributes=None):
    """
    Generates a word cloud based on the dataset and filters.

    Parameters:
        dataset (dict): The social media dataset containing users and posts.
        include_keywords (list): List of keywords to filter posts to include.
        exclude_keywords (list): List of keywords to filter posts to exclude.
        user_attributes (dict): Filters for user attributes (e.g., age, gender, location).

    Returns:
        None: Displays the word cloud or a message if no data matches the criteria.
    """
    # Initialize text storage for word cloud generation
    combined_text = ""

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

    # Apply include/exclude keyword filters to posts
    for post in filtered_posts:
        content = post['content'].lower()
        if include_keywords and not any(keyword.lower() in content for keyword in include_keywords):
            continue
        if exclude_keywords and any(keyword.lower() in content for keyword in exclude_keywords):
            continue
        combined_text += f" {content}"

    # Check if there's any text to process
    if not combined_text.strip():
        print("No matching posts found. Unable to generate a word cloud.")
        return

    # Clean and preprocess the text
    combined_text = re.sub(r'\W+', ' ', combined_text)  # Remove special characters and punctuation

    # Generate the word cloud
    wordcloud = WordCloud(
        background_color='white',
        width=800,
        height=400
    ).generate(combined_text)

    # Display the word cloud
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

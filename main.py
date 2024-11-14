import json
from algorithm1 import generate_post_user_network_diagram
from algorithm2 import generate_interesting_user_network_diagram
from algorithm3 import generate_word_cloud
from algorithm4 import generate_trending_posts_report

# Load the sample dataset
with open("sample_data.json", "r") as f:
    dataset = json.load(f)

# Display options to the user
def display_menu():
    print("\nSocial Media Analysis Tool")
    print("Select an algorithm to test:")
    print("1. Generate Post-User Network Diagram with Important Posts Highlighted")
    print("2. Generate User Network Diagram with Interesting Users Highlighted")
    print("3. Generate Word Cloud of Commonly Used Words in Posts")
    print("4. Generate Report of Trending Posts")
    print("0. Exit")

def main():
    while True:
        display_menu()
        choice = input("\nEnter the number of the algorithm you want to test (or 0 to exit): ")

        if choice == "1":
            # Parameters for Algorithm 1
            importance_criteria = input("Enter importance criteria (views, comments, blend): ")
            threshold = input("Enter a threshold for highlighting important posts (or leave blank for none): ")
            threshold = int(threshold) if threshold else None
            
            # Call the function
            generate_post_user_network_diagram(dataset, importance_criteria, threshold)

        elif choice == "2":
            # Parameters for Algorithm 2
            min_posts = input("Enter minimum number of posts to consider interesting (or leave blank for none): ")
            max_reading_level = input("Enter maximum reading level to consider interesting (or leave blank for none): ")
            attributes = {}

            add_attr = input("Would you like to filter by user attributes? (yes/no): ").strip().lower()
            if add_attr == "yes":
                while True:
                    key = input("Enter attribute key (e.g., age, gender) or 'done' to finish: ")
                    if key == "done":
                        break
                    value = input(f"Enter value for {key}: ")
                    attributes[key] = value

            # Convert optional parameters to the correct type
            min_posts = int(min_posts) if min_posts else None
            max_reading_level = int(max_reading_level) if max_reading_level else None

            # Call the function
            generate_interesting_user_network_diagram(dataset, attributes, min_posts, max_reading_level)

        elif choice == "3":
            # Parameters for Algorithm 3
            include_keywords = input("Enter keywords to include (comma-separated), or leave blank for none: ").split(",")
            exclude_keywords = input("Enter keywords to exclude (comma-separated), or leave blank for none: ").split(",")
            user_attributes = {}

            add_attr = input("Would you like to filter posts by user attributes? (yes/no): ").strip().lower()
            if add_attr == "yes":
                while True:
                    key = input("Enter attribute key (e.g., age, gender) or 'done' to finish: ")
                    if key == "done":
                        break
                    value = input(f"Enter value for {key}: ")
                    user_attributes[key] = value

            # Filter out empty strings in lists if no input was given
            include_keywords = [word.strip() for word in include_keywords if word.strip()]
            exclude_keywords = [word.strip() for word in exclude_keywords if word.strip()]

            # Call the function
            generate_word_cloud(dataset, include_keywords, exclude_keywords, user_attributes)

        elif choice == "4":
            # Parameters for Algorithm 4
            keywords_include = input("Enter keywords to include (comma-separated), or leave blank for none: ").split(",")
            keywords_exclude = input("Enter keywords to exclude (comma-separated), or leave blank for none: ").split(",")
            user_attributes = {}

            add_attr = input("Would you like to filter trending posts by user attributes? (yes/no): ").strip().lower()
            if add_attr == "yes":
                while True:
                    key = input("Enter attribute key (e.g., age, gender) or 'done' to finish: ")
                    if key == "done":
                        break
                    value = input(f"Enter value for {key}: ")
                    user_attributes[key] = value

            # Filter out empty strings in lists if no input was given
            keywords_include = [word.strip() for word in keywords_include if word.strip()]
            keywords_exclude = [word.strip() for word in keywords_exclude if word.strip()]

            # Call the function
            generate_trending_posts_report(dataset, keywords_include, keywords_exclude, user_attributes)

        elif choice == "0":
            print("Exiting the tool. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

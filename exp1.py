emoji_dict = {
    "smile": "😄",
    "heart": "❤️",
    "pizza": "🍕",
    "rocket": "🚀",
    "thumbsup": "👍",
    "earth_asia": "🌏",
    "candy": "🍬",
    "ice_cream": "🍨",
    "1st_place_medal": "🥇",
    "fire":"🔥",
    "check mark":"✅",
    "cloud":"☁️",
    "popcorn":"🍿",
    "clapping hands":"👏",

    # Add more emoji aliases and their corresponding emojis here as needed
}

# Function to convert emoji aliases to actual emojis
def emojize_text(text):
    for code, emoji in emoji_dict.items():
        text = text.replace(code, emoji)
    return text

# Main function to get input from the user and print the emojized text
def main():
    user_input = input("Enter a string with emoji codes: ")
    emojized_text = emojize_text(user_input)
    print("Emojized version:", emojized_text)

# Run the main function if the script is executed
if __name__ == "__main__":
    main()

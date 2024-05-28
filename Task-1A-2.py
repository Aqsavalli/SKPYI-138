def convert_emojis_to_text(text):

    emoji_dict = {
        "😊": ":)",
        "😂": "Laugh",
        "❤️": "Love",
        "🍕":"Pizza",
        "🍦":"Ice-Cream",  
        "😥":"Sad",
        "😜":"Crazy",
        "🎶":"Music",
        "🎂":"Cake",
        "🚗":"Driving Car",
        "💐":"Congratulations",
    }
    
    for emoji, text_rep in emoji_dict.items():
        text = text.replace(emoji, text_rep)
        
    return text

text_with_emojis = "I love 🍕 and 🍦! 😊"
text_without_emojis = convert_emojis_to_text(text_with_emojis)
print("Text without emojis:", text_without_emojis)
text_with_emojis="i'm in ❤️ with this!!! "
text_without_emojis=convert_emojis_to_text(text_with_emojis)
print("Text Without emojis:",text_without_emojis)
text_with_emojis = "I ❤️ 🎶"
text_without_emojis = convert_emojis_to_text(text_with_emojis)
print("Text without emojis:", text_without_emojis)
text_with_emojis = "You're 😜 "
text_without_emojis = convert_emojis_to_text(text_with_emojis)
print("Text without emojis:", text_without_emojis)
text_with_emojis = "Are you 🚗"
text_without_emojis = convert_emojis_to_text(text_with_emojis)
print("Text without emojis:", text_without_emojis)
text_with_emojis = "Hearty 💐 "
text_without_emojis = convert_emojis_to_text(text_with_emojis)
print("Text without emojis:", text_without_emojis)
text_with_emojis = "She feeling 😥 "
text_without_emojis = convert_emojis_to_text(text_with_emojis)
print("Text without emojis:", text_without_emojis)
text_with_emojis = "He is 😂ing "
text_without_emojis = convert_emojis_to_text(text_with_emojis)
print("Text without emojis:", text_without_emojis)

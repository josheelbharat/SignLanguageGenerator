def text_to_gloss(text):
    gloss_map = {"নমস্কাৰ": "SIGN_HELLO", "ধন্যবাদ": "SIGN_THANK_YOU"}
    return gloss_map.get(text, "UNKNOWN")
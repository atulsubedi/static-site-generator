def markdown_to_blocks(markdown):
    blocks = []
    new_text = markdown.split("\n\n")
    for text in new_text:
        if text == "":
            continue
        text = text.strip()
        blocks.append(text)
    return blocks

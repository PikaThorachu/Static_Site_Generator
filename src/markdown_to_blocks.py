def markdown_to_blocks(markdown):
    split_on_double_newline = markdown.split('\n\n')
    removed_whitespace = []
    for line in split_on_double_newline:
        if "\n" not in line:
            removed_whitespace.append(line)
        else:
            list_block = line.split('\n')
            no_whitespace_list_block = ""
            for item in list_block:
                no_whitespace_list_block += '\n' + item.strip()
            removed_whitespace.append(no_whitespace_list_block)
    removed_leading_whitespace = []
    for line in removed_whitespace:
        removed_leading_whitespace.append(line.lstrip())
    return removed_leading_whitespace
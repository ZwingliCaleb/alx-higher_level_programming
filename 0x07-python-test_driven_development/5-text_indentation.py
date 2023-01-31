#!/usr/bin/python3
'''Contains text indentation function
'''

def text_indentation(text):
    '''print text with two new lines after '.', '?', ':'
    Args:
        text (string): print next
    Raises:
        TypeError: text is not a string.
    '''

    if not isinstance(text, str):
        raise TypeError('text must be a string')
    else:
        res = []
        a = 0
        text_len = len(text)
        skip_spaces = True
        is_end = False
        is_delim = False
        for i in range(text_len):
            is_end = i == text_len - 1
            is_delim = text[i] in '.?:'
            if is_delim or is_end:
                res.append(text[a: i + 1] + ('\n\n' * is_delim))
                skip_spaces = True
                a = i +1
            elif text[i] in ' \t\r\v' and skip_spaces:
                a += 1
            elif text[i] == '\n':
                res.append(text[a: i + 1].rstrip() + '\n')
                a += 1
                skip_spaces = True
            else:
                if skip_spaces:
                    a = i
                skip_spaces = False
        print(''.join(res), end='')

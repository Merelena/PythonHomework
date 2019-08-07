def palindrome(text: str) -> str:
    """ Palindrome check """
    text_list = list(text)
    n = 0
    m = len(text) - 1
    flag = True
    ln = len(text)
    while m != ln//2:
        if text_list[n] == ' ':
            n = n + 1
        if text_list[m] == ' ':
            m = m - 1
        if text_list[n] != text_list[m]:
            flag = False
            break
        else:
            n = n + 1
            m = m - 1
    if flag:
        return 'Yes'
    else:
        return 'No'

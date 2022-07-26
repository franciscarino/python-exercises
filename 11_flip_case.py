def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    #take a string find the values that match to swap
    #swap those cases

    swap_phrase = list(phrase)
    swap_list = []   #create empty string instead then concat with +=

    for letter in swap_phrase:
        if letter == to_swap or letter == to_swap.swapcase():
            swap_list.append(letter.swapcase())
        else:
            swap_list.append(letter)

    return "".join(swap_list)
"""XP01_janguru."""


def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2):
    """Calculate the meeting position of 2 jangurus."""
    sleep1_return = sleep1
    sleep2_return = sleep2
    if pos1 <= pos2 and (jump_distance1 / sleep1) <= (jump_distance2 / sleep2):
        pos2 = -1
    elif pos2 <= pos1 and (jump_distance1 / sleep1) >= (jump_distance2 / sleep2):
        pos2 = -1
    else:
        while pos1 != pos2:
            if sleep1 != 0:
                sleep1 = sleep1 - 1
            else:
                sleep1 = sleep1_return - 1
                pos1 = pos1 + jump_distance1
            if sleep2 != 0:
                sleep2 = sleep2 - 1
            else:
                sleep2 = sleep2_return - 1
                pos2 = pos2 + jump_distance2

    return pos2

import itertools

def gen_cand(num, correct_cand_list, diff_cand_list):
    if num == 1:
        correct_prod_list = list(itertools.product(correct_cand_list[0]))
        diff_prod_list = list(itertools.product(diff_cand_list[0]))
    elif num == 2:
        correct_prod_list = list(itertools.product(correct_cand_list[0], correct_cand_list[1]))
        diff_prod_list = list(itertools.product(diff_cand_list[0], diff_cand_list[1]))
    elif num == 3:
        correct_prod_list = list(itertools.product(correct_cand_list[0], correct_cand_list[1], correct_cand_list[2]))
        diff_prod_list = list(itertools.product(diff_cand_list[0], diff_cand_list[1], diff_cand_list[2]))
    elif num == 4:
        correct_prod_list = list(itertools.product(correct_cand_list[0], correct_cand_list[1], correct_cand_list[2], correct_cand_list[3]))
        diff_prod_list = list(itertools.product(diff_cand_list[0], diff_cand_list[1], diff_cand_list[2], diff_cand_list[3]))
    elif num == 5:
        correct_prod_list = list(itertools.product(correct_cand_list[0], correct_cand_list[1], correct_cand_list[2], correct_cand_list[3], correct_cand_list[4]))
        diff_prod_list = list(itertools.product(diff_cand_list[0], diff_cand_list[1], diff_cand_list[2], diff_cand_list[3], diff_cand_list[4]))
    elif num == 6:
        correct_prod_list = list(itertools.product(correct_cand_list[0], correct_cand_list[1], correct_cand_list[2], correct_cand_list[3], correct_cand_list[4], correct_cand_list[5]))
        diff_prod_list = list(itertools.product(diff_cand_list[0], diff_cand_list[1], diff_cand_list[2], diff_cand_list[3], diff_cand_list[4], diff_cand_list[5]))
    elif num == 7:
        correct_prod_list = list(itertools.product(correct_cand_list[0], correct_cand_list[1], correct_cand_list[2], correct_cand_list[3], correct_cand_list[4], correct_cand_list[5], correct_cand_list[6]))
        diff_prod_list = list(itertools.product(diff_cand_list[0], diff_cand_list[1], diff_cand_list[2], diff_cand_list[3], diff_cand_list[4], diff_cand_list[5], diff_cand_list[6]))
    elif num == 8:
        correct_prod_list = list(itertools.product(correct_cand_list[0], correct_cand_list[1], correct_cand_list[2], correct_cand_list[3], correct_cand_list[4], correct_cand_list[5], correct_cand_list[6], correct_cand_list[7]))
        diff_prod_list = list(itertools.product(diff_cand_list[0], diff_cand_list[1], diff_cand_list[2], diff_cand_list[3], diff_cand_list[4], diff_cand_list[5], diff_cand_list[6], diff_cand_list[7]))
    elif num == 9:
        correct_prod_list = list(itertools.product(correct_cand_list[0], correct_cand_list[1], correct_cand_list[2], correct_cand_list[3], correct_cand_list[4], correct_cand_list[5], correct_cand_list[6], correct_cand_list[7], correct_cand_list[8]))
        diff_prod_list = list(itertools.product(diff_cand_list[0], diff_cand_list[1], diff_cand_list[2], diff_cand_list[3], diff_cand_list[4], diff_cand_list[5], diff_cand_list[6], diff_cand_list[7], diff_cand_list[8]))
    elif num == 10:
        correct_prod_list = list(itertools.product(correct_cand_list[0], correct_cand_list[1], correct_cand_list[2], correct_cand_list[3], correct_cand_list[4], correct_cand_list[5], correct_cand_list[6], correct_cand_list[7], correct_cand_list[8], correct_cand_list[9]))
        diff_prod_list = list(itertools.product(diff_cand_list[0], diff_cand_list[1], diff_cand_list[2], diff_cand_list[3], diff_cand_list[4], diff_cand_list[5], diff_cand_list[6], diff_cand_list[7], diff_cand_list[8], diff_cand_list[9]))
    elif num == 11:
        correct_prod_list = list(itertools.product(correct_cand_list[0], correct_cand_list[1], correct_cand_list[2], correct_cand_list[3], correct_cand_list[4], correct_cand_list[5], correct_cand_list[6], correct_cand_list[7], correct_cand_list[8], correct_cand_list[9], correct_cand_list[10]))
        diff_prod_list = list(itertools.product(diff_cand_list[0], diff_cand_list[1], diff_cand_list[2], diff_cand_list[3], diff_cand_list[4], diff_cand_list[5], diff_cand_list[6], diff_cand_list[7], diff_cand_list[8], diff_cand_list[9], diff_cand_list[10]))
    elif num == 12:
        correct_prod_list = list(itertools.product(correct_cand_list[0], correct_cand_list[1], correct_cand_list[2], correct_cand_list[3], correct_cand_list[4], correct_cand_list[5], correct_cand_list[6], correct_cand_list[7], correct_cand_list[8], correct_cand_list[9], correct_cand_list[10], correct_cand_list[11]))
        diff_prod_list = list(itertools.product(diff_cand_list[0], diff_cand_list[1], diff_cand_list[2], diff_cand_list[3], diff_cand_list[4], diff_cand_list[5], diff_cand_list[6], diff_cand_list[7], diff_cand_list[8], diff_cand_list[9], diff_cand_list[10], diff_cand_list[11]))
    elif num == 13:
        correct_prod_list = list(itertools.product(correct_cand_list[0], correct_cand_list[1], correct_cand_list[2], correct_cand_list[3], correct_cand_list[4], correct_cand_list[5], correct_cand_list[6], correct_cand_list[7], correct_cand_list[8], correct_cand_list[9], correct_cand_list[10], correct_cand_list[11], correct_cand_list[12]))
        diff_prod_list = list(itertools.product(diff_cand_list[0], diff_cand_list[1], diff_cand_list[2], diff_cand_list[3], diff_cand_list[4], diff_cand_list[5], diff_cand_list[6], diff_cand_list[7], diff_cand_list[8], diff_cand_list[9], diff_cand_list[10], diff_cand_list[11], diff_cand_list[12]))
    elif num == 14:
        correct_prod_list = list(itertools.product(correct_cand_list[0], correct_cand_list[1], correct_cand_list[2], correct_cand_list[3], correct_cand_list[4], correct_cand_list[5], correct_cand_list[6], correct_cand_list[7], correct_cand_list[8], correct_cand_list[9], correct_cand_list[10], correct_cand_list[11], correct_cand_list[12], correct_cand_list[13]))
        diff_prod_list = list(itertools.product(diff_cand_list[0], diff_cand_list[1], diff_cand_list[2], diff_cand_list[3], diff_cand_list[4], diff_cand_list[5], diff_cand_list[6], diff_cand_list[7], diff_cand_list[8], diff_cand_list[9], diff_cand_list[10], diff_cand_list[11], diff_cand_list[12], diff_cand_list[13]))
    elif num == 15:
        correct_prod_list = list(itertools.product(correct_cand_list[0], correct_cand_list[1], correct_cand_list[2], correct_cand_list[3], correct_cand_list[4], correct_cand_list[5], correct_cand_list[6], correct_cand_list[7], correct_cand_list[8], correct_cand_list[9], correct_cand_list[10], correct_cand_list[11], correct_cand_list[12], correct_cand_list[13], correct_cand_list[14]))
        diff_prod_list = list(itertools.product(diff_cand_list[0], diff_cand_list[1], diff_cand_list[2], diff_cand_list[3], diff_cand_list[4], diff_cand_list[5], diff_cand_list[6], diff_cand_list[7], diff_cand_list[8], diff_cand_list[9], diff_cand_list[10], diff_cand_list[11], diff_cand_list[12], diff_cand_list[13], diff_cand_list[14]))
    elif num == 16:
        correct_prod_list = list(itertools.product(correct_cand_list[0], correct_cand_list[1], correct_cand_list[2], correct_cand_list[3], correct_cand_list[4], correct_cand_list[5], correct_cand_list[6], correct_cand_list[7], correct_cand_list[8], correct_cand_list[9], correct_cand_list[10], correct_cand_list[11], correct_cand_list[12], correct_cand_list[13], correct_cand_list[14], correct_cand_list[15]))
        diff_prod_list = list(itertools.product(diff_cand_list[0], diff_cand_list[1], diff_cand_list[2], diff_cand_list[3], diff_cand_list[4], diff_cand_list[5], diff_cand_list[6], diff_cand_list[7], diff_cand_list[8], diff_cand_list[9], diff_cand_list[10], diff_cand_list[11], diff_cand_list[12], diff_cand_list[13], diff_cand_list[14], diff_cand_list[15]))
    elif num == 17:
        correct_prod_list = list(itertools.product(correct_cand_list[0], correct_cand_list[1], correct_cand_list[2], correct_cand_list[3], correct_cand_list[4], correct_cand_list[5], correct_cand_list[6], correct_cand_list[7], correct_cand_list[8], correct_cand_list[9], correct_cand_list[10], correct_cand_list[11], correct_cand_list[12], correct_cand_list[13], correct_cand_list[14], correct_cand_list[15], correct_cand_list[16]))
        diff_prod_list = list(itertools.product(diff_cand_list[0], diff_cand_list[1], diff_cand_list[2], diff_cand_list[3], diff_cand_list[4], diff_cand_list[5], diff_cand_list[6], diff_cand_list[7], diff_cand_list[8], diff_cand_list[9], diff_cand_list[10], diff_cand_list[11], diff_cand_list[12], diff_cand_list[13], diff_cand_list[14], diff_cand_list[15], diff_cand_list[16]))
        
    return correct_prod_list, diff_prod_list
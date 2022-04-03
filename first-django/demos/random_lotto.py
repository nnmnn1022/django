import random

def run() :
    lotto_list = random.sample(range(1,45), 7)
    print(lotto_list)

    return lotto_list


if __name__ == '__main__' :
    run()
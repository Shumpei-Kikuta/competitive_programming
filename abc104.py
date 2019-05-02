from math import ceil

class Score():
    def __init__(self, score, num, bonus):
        self.num = num
        self.score = score
        self.bonus = bonus

D, G = [int(c) for c in input().split(" ")]
min_times = 100000000000

score_lists = []
min_num = 0
for i in range(D):
    p, c = [int(c) for c in input().split(" ")]
    score = 100 * (i + 1)
    scores = Score(score, p, c)
    score_lists.append(scores)

def dfs(masks: list, num: int, sum_score, sum_use_num):
    """completeするかしないかで2^Dを選んでいく
    """
    global score_lists
    if (num == D):
        # print(sum_score)
        for i in range(D - 1, -1, -1):
            if (masks[i] == 1):
                continue
            else:
                global min_times
                if sum_score >= G:
                    min_times = min(min_times, sum_use_num)
                elif sum_score + (score_lists[i].num)* score_lists[i].score < G:
                    # break
                    continue
                else:
                    score = sum_score
                    j = 0
                    while (True):
                        j += 1
                        score += score_lists[i].score
                        if score >= G:
                            min_times = min(min_times, j + sum_use_num)
                            break
                    break
                    # min_times = min(sum_use_num + ceil((G - sum_score) / score_lists[i].score), min_times)
                    # break
                    
    else:
        masks[num] = 0
        dfs(masks, num + 1, sum_score, sum_use_num)

        masks[num] = 1
        dfs(masks, num + 1, \
            sum_score + score_lists[num].num * score_lists[num].score + score_lists[num].bonus, \
            sum_use_num + score_lists[num].num)

def main():
    masks = [0] * D
    dfs(masks, 0, 0, 0)

    print(min_times)

if __name__ == '__main__':
    main()
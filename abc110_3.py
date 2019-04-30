def main():
    S = list(input())
    T = list(input())

    alphabets = "abcdefghijklmnopqrstuvwxyz"
    transforms = {}
    alpha_dicts = {}
    for i in range(26):
        alpha_dicts[alphabets[i]] = 0

    for i in range(len(S)):
        if (S[i] in transforms.keys()):
            S[i] = transforms[S[i]]
        if (S[i] == T[i]):
            continue
        else:
            if S[i] in transforms.keys():
                return "No"
            else:
                transforms[S[i]] = T[i]
                alpha_dicts[S[i]] += 1
                if alpha_dicts[S[i]] != 1:
                    return "No"
                # transforms[T[i]] = S[i]
        print(transforms)
    return "Yes"
        # transforms[S[i]] = T[i]

if __name__ == '__main__':
    print(main())
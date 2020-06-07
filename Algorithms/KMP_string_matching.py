def create_lps_table(pattern, M, lps):
    length = 0

    i = 1
    while i < M:
        if pat[i] == pat[length]:
            length += 1
            lps.append(length)
            i += 1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps.append(0)
                i += 1

def search(pattern, string):
    M = len(pattern)
    N = len(string)
    lps = [0]
    create_lps_table(pattern, M, lps)

    i = j = 0
    while i < N:
        if string[i] == pattern[j]:
            i += 1
            j += 1
        if j == M:
            print(f"Patten found between {i - j} and {i - j + M - 1}")
            j = lps[j - 1]
        elif i < N and string[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

if __name__ == "__main__":
    str1 = "abcdabc"
    pat = "abc"
    search(pat, str1)


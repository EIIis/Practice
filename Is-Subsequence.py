def isSubsequence(self, s, t):
        arr = 0
        seq = 0
        while arr < len(t) and seq < len(s):
            if t[arr] == s[seq]:
                seq += 1
            arr += 1
        return seq == len(s)

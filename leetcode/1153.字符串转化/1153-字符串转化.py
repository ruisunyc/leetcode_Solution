class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1==str2:return True
        d = {}
        s = set()
        for i in range(len(str1)):
            if str1[i] not in d:
                d[str1[i]]=str2[i]
                s.add(str2[i])
            else:
                if d[str1[i]]!=str2[i]:
                    return False
        return len(s)<26
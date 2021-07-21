class Solution:
    def compress(self, chars: List[str]) -> int:
        v1, v2 = 0, 0
        while v2 < len(chars):
            cnt = 1
            chars[v1] = chars[v2]
            while v2 + 1 < len(chars) and chars[v2] == chars[v2 + 1]:
                v2 += 1
                cnt += 1
            if cnt > 1:
                for a in str(cnt):
                    chars[v1 + 1] = a
                    v1+=1
            v1+=1
            v2+=1
        return v1
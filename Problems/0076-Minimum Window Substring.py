class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t = collections.Counter(t)
        links = [-1 for each in s]
        plinks = [-1 for each in s]
        cnt = {}
        start = last = -1
        ans = ''
        for idx, each in enumerate(s):
            if each not in t:
                continue
            if not cnt:
                start = last = idx
                cnt[each] = [idx]
            elif each not in cnt:
                links[last] = idx
                plinks[idx] = last
                last = idx
                cnt[each] = [idx]
            elif len(cnt[each]) < t[each]:
                links[last] = idx
                plinks[idx] = last
                last = idx
                cnt[each].append(idx)
            elif cnt[each][0] == start:
                links[last] = idx
                plinks[idx] = last
                last = idx
                start = links[start]
                plinks[start]  = -1
                cnt[each].append(idx)
                cnt[each].pop(0)
            else:
                links[last] = idx
                plinks[idx] = last
                last = idx
                tmp = cnt[each][0]
                p, n = plinks[tmp], links[tmp]
                links[p] = n
                plinks[n] = p
                cnt[each].append(idx)
                cnt[each].pop(0)
            mark = True
            for each_char in t:
                if each_char not in cnt or t[each_char] != len(cnt[each_char]):
                    mark = False
                    break
            if mark:
                if not ans:
                    ans = s[start:last+1]
                else:
                    ans = ans if last-start+1>len(ans) else s[start:last+1]
        return ans

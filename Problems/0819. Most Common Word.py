class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.replace(',', ' ')
        p = re.sub('[^a-zA-Z ]', '', paragraph)
        p = p.lower().split()
        cnt = collections.Counter(p)
        ans = sorted([(k, v) for k, v in cnt.items()], key=lambda x:x[1], reverse=True)
        for k, v in ans:
            if k not in banned:
                return k

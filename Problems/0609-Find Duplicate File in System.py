class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        ans = {}
        for each in paths:
            path, files = each.split(' ')[0], each.split(' ')[1:]
            for file in files:
                sep0, sep1 = file.find('('), file.find(')')
                file_name = file[:sep0]
                file_content = file[sep0+1:sep1]
                if file_content not in ans:
                    ans[file_content] = []
                ans[file_content].append(path+'/'+file_name)
        return [ans[each] for each in ans if len(ans[each])>1]

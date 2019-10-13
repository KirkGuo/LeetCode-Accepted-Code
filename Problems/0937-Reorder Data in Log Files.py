class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []
        for each in logs:
            words = each.split(' ')
            for letter in words[1]:
                if letter in '0123456789':
                    digits.append(each)
                    break
                if ord(letter)>=ord('a') and ord(letter)<=ord('z'):
                    letters.append(each)
                    break
                
        return sorted(letters, key=lambda item:(' '.join(item.split(' ')[1:]), item[0])) + digits

"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        new_list = []
        for each in schedule:
            new_list += each
        new_list = sorted(new_list, key=lambda item: (item.start, item.end))
        to_return = []
        s = None
        t = None
        for each in new_list:
            start, end = each.start, each.end
            if s == None and t == None:
                s, t = start, end
                continue
            if start > t:
                to_return.append(Interval(t, start))
                s, t = start, end
            elif end > t:
                t = end
        return to_return

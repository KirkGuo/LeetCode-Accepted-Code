class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = collections.Counter(nums)
        cnt2num = collections.defaultdict(list)
        for each in cnt:
            cnt2num[cnt[each]].append(each)
        
        def shiftUp(heap, pos):
            if not pos:
                return
            parent = (pos-1)//2
            if heap[parent]>heap[pos]:
                heap[parent], heap[pos] = heap[pos], heap[parent]
                shiftUp(heap, parent)
        
        def shiftDown(heap, pos):
            l = len(heap)
            left = pos*2+1 if pos*2+1<l else None
            right = pos*2+2 if pos*2+2<l else None
            if right:
                target = min(heap[pos], min(heap[left], heap[right]))
                if target==heap[pos]:
                    return
                if target==heap[left]:
                    heap[left], heap[pos] = heap[pos], heap[left]
                    shiftDown(heap, left)
                else:
                    heap[right], heap[pos] = heap[pos], heap[right]
                    shiftDown(heap, right)
            elif left:
                if heap[left]<heap[pos]:
                    heap[pos], heap[left] = heap[left], heap[pos]
                    shiftDown(heap, left)
        heap = []
        for _,each in cnt.items():
            if len(heap)<k:
                heap.append(each)
                shiftUp(heap, len(heap)-1)
            elif each>heap[0]:
                heap[0]=each
                shiftDown(heap, 0)
        ans = []
        while heap:
            ans += cnt2num[heap[0]]
            heap[0], heap[-1] = heap[-1], heap[0]
            heap.pop()
            shiftDown(heap, 0)
        return list(set(ans))

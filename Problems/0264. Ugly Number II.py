class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        def shiftUp(heap, pos):
            if not pos:
                return
            parent = (pos-1)//2
            if heap[parent]>heap[pos]:
                heap[parent], heap[pos] = heap[pos], heap[parent]
                shiftUp(heap, parent)
            return
        
        def shiftDown(heap, pos):
            l = len(heap)
            left = 2*pos+1 if 2*pos+1<l else None
            right = 2*pos+2 if 2*pos+2<l else None
            if right:
                curr = min(heap[pos], min(heap[left], heap[right]))
                if curr==heap[pos]:
                    return
                elif curr==heap[left]:
                    heap[left], heap[pos] = heap[pos], heap[left]
                    shiftDown(heap, left)
                    return
                heap[right], heap[pos] = heap[pos], heap[right]
                shiftDown(heap, right)
            elif left and heap[left]<heap[pos]:
                heap[left], heap[pos] = heap[pos], heap[left]
            return
        
        heap = [1]
        in_heap = set([1])
        for i in range(n):
            heap[0], heap[-1] = heap[-1], heap[0]
            ans = heap.pop()
            shiftDown(heap, 0)
            in_heap.remove(ans)
            if len(heap)<n:
                for each in [2,3,5]:
                    if ans*each not in in_heap:
                        heap.append(ans*each)
                        in_heap.add(ans*each)
                        shiftUp(heap, len(heap)-1)
        return ans
            

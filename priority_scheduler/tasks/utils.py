import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, task):
        heapq.heappush(self.heap, (task.priority, task))

    def pop(self):
        if self.heap:
            return heapq.heappop(self.heap)[1]
        return None


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i].priority < right_half[j].priority:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def efficient_sort(tasks):
    task_list = list(tasks)
    merge_sort(task_list)
    return task_list

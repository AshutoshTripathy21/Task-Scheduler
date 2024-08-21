# utils.py
import heapq
from datetime import datetime, timedelta

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, task):
        heapq.heappush(self.heap, (self.get_priority_value(task.priority), task.estimated_duration, task))

    def pop(self):
        if self.heap:
            return heapq.heappop(self.heap)[2]
        return None

    @staticmethod
    def get_priority_value(priority_str):
        priority_map = {
            "most valuable": 1,
            "valuable": 2,
            "high": 3,
            "moderate": 4,
            "low": 5
        }
        return priority_map.get(priority_str.lower(), 5)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            left_priority_value = PriorityQueue.get_priority_value(left_half[i].priority)
            right_priority_value = PriorityQueue.get_priority_value(right_half[j].priority)

            if (left_priority_value < right_priority_value or 
                (left_priority_value == right_priority_value and left_half[i].estimated_duration < right_half[j].estimated_duration)):
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
    for task in task_list:
        task.priority_value = PriorityQueue.get_priority_value(task.priority)
    merge_sort(task_list)
    return task_list


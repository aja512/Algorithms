import collections


class Solution:
    def timeTaken(self, arrivals: list[int], states: list[int]) -> list[int]:
        n = len(arrivals)
        answer = [0] * n

        time, direction = 0, 1
        queues = [collections.deque(), collections.deque()]

        def exhaust_until(end_time: int) -> None:
            nonlocal time, direction
            while time < end_time and any(queues):
                if not queues[direction]:
                    direction ^= 1
                answer[queues[direction].popleft()] = time
                time += 1

        for person, (arrival, state) in enumerate(zip(arrivals, states)):
            exhaust_until(arrival)
            if time < arrival:
                time, direction = arrival, 1
            queues[state].append(person)

        exhaust_until(200_000)
        return answer

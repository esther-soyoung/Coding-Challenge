from collections import deque

def solution(bridge_length, weight, truck_weights):
    on_bridge = deque([])
    time = 0
    for i in truck_weights:
        while True:
            time += 1
            # one truck passed the bridge
            if len(on_bridge) == bridge_length:
                on_bridge.popleft()
            # put truck on the bridge
            if ((len(on_bridge) + 1) <= bridge_length) and (sum(on_bridge) + i <= weight):
                on_bridge.append(i)
                break
            # wait one timestamp
            else:
                on_bridge.append(0)

    # wait for the last truck to pass
    time += (bridge_length - 1)
    return time + 1

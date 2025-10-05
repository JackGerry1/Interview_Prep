from typing import List

def carFleetStack(target: int, position: List[int], speed: List[int]) -> int:
    arrival_times_stack = []
    position_speed_pairs = [(pos, spd) for pos, spd in zip(position, speed)]
    sorted_cars = sorted(position_speed_pairs, reverse=True)

    for pos, spd in sorted_cars: 
        time_to_target = (target - pos) / spd
        
        if not arrival_times_stack or time_to_target > arrival_times_stack[-1]: 
            arrival_times_stack.append(time_to_target)
            
    return len(arrival_times_stack)

def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    last_fleet_arrival_time = 0 
    fleet_count = 0 
    
    position_speed_pairs = [(pos, spd) for pos, spd in zip(position, speed)]
    sorted_pairs = sorted(position_speed_pairs, reverse=True)

    for pos, spd in sorted_pairs: 
        time_to_target = (target - pos) / spd

        if time_to_target > last_fleet_arrival_time: 
            last_fleet_arrival_time = time_to_target
            fleet_count += 1

    return fleet_count
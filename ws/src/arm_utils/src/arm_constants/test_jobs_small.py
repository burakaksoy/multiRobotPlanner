anchor_complete_ticket_list = {
    0: {"ticket_id": 0, "machine_type": 0, "actual_duration": 5, "duration": 10, "parents": [], "num_robots": 2},
    1: {"ticket_id": 1, "machine_type": 1, "actual_duration": 95.7, "duration": 85, "parents": [0]},
    
    2: {"ticket_id": 6, "machine_type": 0, "actual_duration": 5, "duration": 5, "parents": [], "num_robots": 2},
    3: {"ticket_id": 7, "machine_type": 1, "actual_duration": 65.9, "duration": 50, "parents": [2]},
    
    4: {"ticket_id": 12, "machine_type": 0, "actual_duration": 5, "duration": 5, "parents": [], "num_robots": 2},
    5: {"ticket_id": 13, "machine_type": 1, "actual_duration": 205.3, "duration": 180, "parents": [4]},
    
    6: {"ticket_id": 18, "machine_type": 0, "actual_duration": 5, "duration": 5, "parents": [], "num_robots": 3},
    7: {"ticket_id": 19, "machine_type": 1, "actual_duration": 79.9, "duration": 85, "parents": [6]},
    
    8: {"ticket_id": 24, "machine_type": 0, "actual_duration": 5, "duration": 5, "parents": [], "num_robots": 6},
    9: {"ticket_id": 25, "machine_type": 1, "actual_duration": 93.1, "duration": 93.1, "parents": [8]},
    
    10: {"ticket_id": 30, "machine_type": 0, "actual_duration": 5, "duration": 5, "parents": [], "num_robots": 4},
    11: {"ticket_id": 31, "machine_type": 1, "actual_duration": 166.1, "duration": 190, "parents": [10]},
    
    12: {"ticket_id": 36, "machine_type": 0, "actual_duration": 5, "duration": 5, "parents": [], "num_robots": 5},
    13: {"ticket_id": 37, "machine_type": 5, "actual_duration": 71, "duration": 75, "parents": [12]},
    
    14: {"ticket_id": 41, "machine_type": 0, "actual_duration": 5, "duration": 5, "parents": [], "num_robots": 3},
    15: {"ticket_id": 42, "machine_type": 5, "actual_duration": 72, "duration": 80, "parents": [14]},
    
    16: {"ticket_id": 46, "machine_type": 0, "actual_duration": 5, "duration": 5, "parents": [], "num_robots": 6},
    17: {"ticket_id": 47, "machine_type": 5, "actual_duration": 51, "duration": 76, "parents": [16]},
}

# anchor_complete_ticket_list = {
#     # Tree Job 2 roots.
#     11: {"job_id": 1, "machine_type": 0, "duration": 5, "parents": [], "actual_duration": 5, "num_robots": 3},
#     12: {"job_id": 1, "machine_type": 0, "duration": 5, "parents": [], "actual_duration": 5, "num_robots": 2},
#     13: {"job_id": 1, "machine_type": 2, "duration": 45.7, "parents": [11], "actual_duration": 45.7},
#     14: {"job_id": 1, "machine_type": 3, "duration": 54.8, "parents": [12], "actual_duration": 54.8},
#     15: {"job_id": 1, "machine_type": 1, "duration": 89.2, "parents": [13,14], "actual_duration": 89.2},
#     16: {"job_id": 1, "machine_type": 3, "duration": 43.1, "parents": [15], "actual_duration": 43.1},
#     17: {"job_id": 1, "machine_type": 7, "duration": 38.7, "parents": [16], "actual_duration": 38.7},
#     # Tree Job 3 roots.
#     1: {"job_id": 0, "machine_type": 0, "duration": 10, "parents": [], "actual_duration": 10, "time_left": 10, "num_robots": 2},
#     2: {"job_id": 0, "machine_type": 0, "duration": 5, "parents": [], "actual_duration": 5, "time_left": 5, "num_robots": 1},
#     3: {"job_id": 0, "machine_type": 0, "duration": 5, "parents": [], "actual_duration": 7, "time_left": 5, "num_robots": 3},
#     4: {"job_id": 0, "machine_type": 2, "duration": 45, "parents": [1], "actual_duration": 55, "time_left": 45},
#     5: {"job_id": 0, "machine_type": 2, "duration": 30, "parents": [2], "actual_duration": 25, "time_left": 30},
#     6: {"job_id": 0, "machine_type": 3, "duration": 30, "parents": [3], "actual_duration": 28, "time_left": 30},
#     7: {"job_id": 0, "machine_type": 2, "duration": 60, "parents": [4,5], "actual_duration": 75, "time_left": 60},
#     8: {"job_id": 0, "machine_type": 2, "duration": 30, "parents": [6,7], "actual_duration": 30, "time_left": 30},
#     9: {"job_id": 0, "machine_type": 3, "duration": 45, "parents": [8], "actual_duration": 48, "time_left": 45},
#     10: {"job_id": 0, "machine_type": 4, "duration": 60, "parents": [9], "actual_duration": 60, "time_left": 60},
# }

test_data_1_info = {
    'num_ticket_adds': 4
}
test_data_1 = {
    'complete_ticket_list': 
    anchor_complete_ticket_list.copy(),
}
test_data_1["ticket_add_0"] = {  
    ticket_id: test_data_1["complete_ticket_list"][ticket_id] for ticket_id in range(
        min(anchor_complete_ticket_list.keys()), 18
    )
}
test_data_1["ticket_add_1"] = {
    8: test_data_1["complete_ticket_list"][8]
}
test_data_1["ticket_add_2"] = {
    ticket_id: test_data_1["complete_ticket_list"][ticket_id] for ticket_id in range(9, 13)
}
test_data_1["ticket_add_3"] = {
    ticket_id: test_data_1["complete_ticket_list"][ticket_id] for ticket_id in range(13, 18)
}

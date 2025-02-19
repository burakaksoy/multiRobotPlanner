'''
Rensselaer Polytechnic Institute - Julius Lab
ARM Project
Author - Chukwuemeka Osaretin Ike

Description:
    Job sets with job ID manually added (obsolete).
'''
complete_ticket_list = {
    0: {"job_id": 0, "ticket_id": 0, "machine_type": 0, "actual_duration": 5, "duration": 10, "parents": []},
    1: {"job_id": 0, "ticket_id": 1, "machine_type": 1, "actual_duration": 95.7, "duration": 85, "parents": [0]},
    2: {"job_id": 0, "ticket_id": 2, "machine_type": 2, "actual_duration": 44.8, "duration": 47.2, "parents": [1]},
    3: {"job_id": 0, "ticket_id": 3, "machine_type": 3, "actual_duration": 37.6, "duration": 40, "parents": [2]},
    4: {"job_id": 0, "ticket_id": 4, "machine_type": 4, "actual_duration": 45, "duration": 50, "parents": [3]},
    5: {"job_id": 0, "ticket_id": 5, "machine_type": 7, "actual_duration": 40.6, "duration": 44.2, "parents": [4]},
    
    6: {"job_id": 1, "ticket_id": 6, "machine_type": 0, "actual_duration": 5, "duration": 5, "parents": []},
    7: {"job_id": 1, "ticket_id": 7, "machine_type": 1, "actual_duration": 65.9, "duration": 50, "parents": [6]},
    8: {"job_id": 1, "ticket_id": 8, "machine_type": 2, "actual_duration": 42.5, "duration": 48, "parents": [7]},
    9: {"job_id": 1, "ticket_id": 9, "machine_type": 3, "actual_duration": 26.9, "duration": 35, "parents": [8]},
    10: {"job_id": 1, "ticket_id": 10, "machine_type": 4, "actual_duration": 34, "duration": 40.4, "parents": [9]},
    11: {"job_id": 1, "ticket_id": 11, "machine_type": 7, "actual_duration": 24.6, "duration": 40, "parents": [10]},
    
    12: {"job_id": 2, "ticket_id": 12, "machine_type": 0, "actual_duration": 5, "duration": 5, "parents": []},
    13: {"job_id": 2, "ticket_id": 13, "machine_type": 1, "actual_duration": 205.3, "duration": 180, "parents": [12]},
    14: {"job_id": 2, "ticket_id": 14, "machine_type": 2, "actual_duration": 67.8, "duration": 78, "parents": [13]},
    15: {"job_id": 2, "ticket_id": 15, "machine_type": 3, "actual_duration": 57.5, "duration": 55, "parents": [14]},
    16: {"job_id": 2, "ticket_id": 16, "machine_type": 4, "actual_duration": 74, "duration": 75.6, "parents": [15]},
    17: {"job_id": 2, "ticket_id": 17, "machine_type": 7, "actual_duration": 82.8, "duration": 90, "parents": [16]},
    
    18: {"job_id": 3, "ticket_id": 18, "machine_type": 0, "actual_duration": 5, "duration": 5, "parents": []},
    19: {"job_id": 3, "ticket_id": 19, "machine_type": 1, "actual_duration": 79.9, "duration": 85, "parents": [18]},
    20: {"job_id": 3, "ticket_id": 20, "machine_type": 2, "actual_duration": 42.5, "duration": 30, "parents": [19]},
    21: {"job_id": 3, "ticket_id": 21, "machine_type": 3, "actual_duration": 33.8, "duration": 50, "parents": [20]},
    22: {"job_id": 3, "ticket_id": 22, "machine_type": 4, "actual_duration": 34, "duration": 30, "parents": [21]},
    23: {"job_id": 3, "ticket_id": 23, "machine_type": 7, "actual_duration": 34.7, "duration": 60, "parents": [22]},
    
    24: {"job_id": 4, "ticket_id": 24, "machine_type": 0, "actual_duration": 5, "duration": 5, "parents": []},
    25: {"job_id": 4, "ticket_id": 25, "machine_type": 1, "actual_duration": 93.1, "duration": 93.1, "parents": [24]},
    26: {"job_id": 4, "ticket_id": 26, "machine_type": 2, "actual_duration": 51.7, "duration": 51.7, "parents": [25]},
    27: {"job_id": 4, "ticket_id": 27, "machine_type": 3, "actual_duration": 40.5, "duration": 40.5, "parents": [26]},
    28: {"job_id": 4, "ticket_id": 28, "machine_type": 4, "actual_duration": 39, "duration": 39, "parents": [27]},
    29: {"job_id": 4, "ticket_id": 29, "machine_type": 7, "actual_duration": 52.7, "duration": 52.7, "parents": [28]},
    
    30: {"job_id": 5, "ticket_id": 30, "machine_type": 0, "actual_duration": 5, "duration": 5, "parents": []},
    31: {"job_id": 5, "ticket_id": 31, "machine_type": 1, "actual_duration": 166.1, "duration": 190, "parents": [30]},
    32: {"job_id": 5, "ticket_id": 32, "machine_type": 2, "actual_duration": 60.9, "duration": 75, "parents": [31]},
    33: {"job_id": 5, "ticket_id": 33, "machine_type": 3, "actual_duration": 51.5, "duration": 45, "parents": [32]},
    34: {"job_id": 5, "ticket_id": 34, "machine_type": 4, "actual_duration": 71.5, "duration": 71.5, "parents": [33]},
    35: {"job_id": 5, "ticket_id": 35, "machine_type": 7, "actual_duration": 67.6, "duration": 70, "parents": [34]},
    
    36: {"job_id": 6, "ticket_id": 36, "machine_type": 0, "actual_duration": 5, "duration": 5, "parents": []},
    37: {"job_id": 6, "ticket_id": 37, "machine_type": 5, "actual_duration": 71, "duration": 75, "parents": [36]},
    38: {"job_id": 6, "ticket_id": 38, "machine_type": 3, "actual_duration": 73.9, "duration": 80, "parents": [37]},
    39: {"job_id": 6, "ticket_id": 39, "machine_type": 6, "actual_duration": 27.4, "duration": 25, "parents": [38]},
    40: {"job_id": 6, "ticket_id": 40, "machine_type": 7, "actual_duration": 103.9, "duration": 103.9, "parents": [39]},
    
    41: {"job_id": 7, "ticket_id": 41, "machine_type": 0, "actual_duration": 5, "duration": 5, "parents": []},
    42: {"job_id": 7, "ticket_id": 42, "machine_type": 5, "actual_duration": 72, "duration": 80, "parents": [41]},
    43: {"job_id": 7, "ticket_id": 43, "machine_type": 3, "actual_duration": 67.2, "duration": 69, "parents": [42]},
    44: {"job_id": 7, "ticket_id": 44, "machine_type": 6, "actual_duration": 14.4, "duration": 10, "parents": [43]},
    45: {"job_id": 7, "ticket_id": 45, "machine_type": 7, "actual_duration": 60.1, "duration": 50, "parents": [44]},
    
    46: {"job_id": 8, "ticket_id": 46, "machine_type": 0, "actual_duration": 5, "duration": 5, "parents": []},
    47: {"job_id": 8, "ticket_id": 47, "machine_type": 5, "actual_duration": 51, "duration": 76, "parents": [46]},
    48: {"job_id": 8, "ticket_id": 48, "machine_type": 3, "actual_duration": 97, "duration": 85, "parents": [47]},
    49: {"job_id": 8, "ticket_id": 49, "machine_type": 6, "actual_duration": 21.6, "duration": 25, "parents": [48]},
    50: {"job_id": 8, "ticket_id": 50, "machine_type": 7, "actual_duration": 57.2, "duration": 60, "parents": [49]},
    
    51: {"job_id": 9, "ticket_id": 51, "machine_type": 0, "actual_duration": 5, "duration": 5, "parents": []},
    52: {"job_id": 9, "ticket_id": 52, "machine_type": 5, "actual_duration": 25, "duration": 40, "parents": [51]},
    53: {"job_id": 9, "ticket_id": 53, "machine_type": 3, "actual_duration": 45.8, "duration": 35, "parents": [52]},
    54: {"job_id": 9, "ticket_id": 54, "machine_type": 6, "actual_duration": 19.1, "duration": 19.1, "parents": [53]},
    55: {"job_id": 9, "ticket_id": 55, "machine_type": 7, "actual_duration": 31.6, "duration": 31.6, "parents": [54]},
    
    56: {"job_id": 10, "ticket_id": 56, "machine_type": 0, "actual_duration": 5, "duration": 1, "parents": []},
    57: {"job_id": 10, "ticket_id": 57, "machine_type": 5, "actual_duration": 43, "duration": 50, "parents": [56]},
    58: {"job_id": 10, "ticket_id": 58, "machine_type": 3, "actual_duration": 62.4, "duration": 57, "parents": [57]},
    59: {"job_id": 10, "ticket_id": 59, "machine_type": 6, "actual_duration": 23, "duration": 23, "parents": [58]},
    60: {"job_id": 10, "ticket_id": 60, "machine_type": 7, "actual_duration": 77.3, "duration": 85, "parents": [59]},

    61: {"job_id": 11, "ticket_id": 61, "machine_type": 0, "actual_duration": 5, "duration": 1, "parents": []},
    62: {"job_id": 11, "ticket_id": 62, "machine_type": 5, "actual_duration": 151, "duration": 175, "parents": [61]},
    63: {"job_id": 11, "ticket_id": 63, "machine_type": 3, "actual_duration": 84.7, "duration": 65, "parents": [62]},
    64: {"job_id": 11, "ticket_id": 64, "machine_type": 6, "actual_duration": 19.4, "duration": 30, "parents": [63]},
    65: {"job_id": 11, "ticket_id": 65, "machine_type": 7, "actual_duration": 53.8, "duration": 55, "parents": [64]},
}

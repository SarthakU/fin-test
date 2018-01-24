# # checks list for uniqueness
# def isUnique(lst): return sorted(lst) == sorted(list(set(lst)))

# # clean string, remove dots convert to list of ints
# def cleanString(string): return [int(i) for i in string.replace('.', '')]

# # checks for valid sudoko board config
# def isValid(board):
#     # check whether values in rows in correct range
#     for row in range(9):
#         if False in [isUnique(i[row]) for i in board]:
#             return 0

#     # check whether values in columns in correct range
#     if False in [isUnique(cleanString(i)) and len(i) == 9 for i in board]:
#         return 0

#     # check 3x3 subgrids
#     for i in range(0, 7, 3):
#         for j in range(0, 7, 3):
#             subgrid = cleanString(''.join([board[i + k][j:j + 3] for k in range(3)]))
#             if not isUnique(subgrid):
#                 return 0

#     return 1

# # # Test case
# # board = ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
# # print(isValid(board))
a = ['PROJID', 'ID', 'GIVEN_DURATION', 'ORIGINAL_DURATION', 'LEVELLING_DETAILS', 'RESUME', 'GIVEN_START', 'LATEST_PROGRESS_PERIOD', 'TASK_WORK_RATE_TIME_UNIT', 'TASK_WORK_RATE', 'PLACEMENT', 'BEEN_SPLIT', 'INTERRUPTIBLE', 'HOLDING_PIN', 'ACTUAL_DURATION', 'CRITICAL_PATH_DRAG', 'ORIGINAL_BUFFER_DURATION', 'LOGICAL_PATH_DURATION', 'EARLY_START_DATE', 'LATE_START_DATE', 'FREE_START_DATE', 'START_CONSTRAINT_DATE', 'END_CONSTRAINT_DATE', 'EARLY_END_DATE_RS', 'LATE_END_DATE_RS', 'FREE_END_DATE_RS', 'EFFORT_BUDGET', 'NATURAL_ORDER', 'LOGICAL_PRECEDENCE', 'SPARE_INTEGER', 'SWIM_LANE', 'CASCADE_ACTIVITY_NUMBER', 'FLAGS', 'LOGICAL_PATH', 'LOGICAL_PATH_ORDER', 'USER_PERCENT_COMPLETE', 'OVERALL_PERCENT_COMPLETE', 'OVERALL_PERCENT_COMPL_WEIGHT', 'NAME', 'WBN_CODE', 'NOTES', 'UNIQUE_TASK_ID', 'CALENDAR', 'WBS', 'EFFORT_TIME_UNIT', 'WORK_UNIT', 'LATEST_ALLOC_PROGRESS_PERIOD', 'IFC_PRODUCT_SET', 'IFC_SIMULATION_PROFILE', 'TASKBASE_WORK', 'BAR', 'WORK_FACE_FREQUENCY', 'CONSTRAINT_FLAG', 'PRIORITY', 'IFC_TASK_TYPE', 'CONDITIONAL_BREAK', 'DURATION_TYPE', 'CRITICAL', 'USE_PARENT_CALENDAR', 'BUFFER_TASK', 'MARK_FOR_HIDING', 'WORK_FACE_FREQUENCY_FORWARD', 'OWNED_BY_TIMESHEET_X', 'START_ON_NEW_DAY', 'LONGEST_PATH', 'DURATION', 'LINKABLE_START', 'LINKABLE_FINISH', 'DURATION_TIME_UNIT', 'UNSCHEDULABLE', 'SUBPROJECT_ID', 'ALT_ID', 'LAST_EDITED_DATE', 'LAST_EDITED_BY', 'GUID']

for i in a:
    print( i)

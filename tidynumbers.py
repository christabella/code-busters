#!/usr/bin/env python
'''
Linear algorithm that turns everything after a pivot (last number that
stepped up from a previous number before a step down, i.e. inversion)
into '9's, decrements the pivot, and preserves everything before.
'''


def tidy_number(nums):
    step_up = 0  # Track the last step up before any inversion
    step_down = 0  # If there are no step downs, it's tidy!
    prev_num = int(nums[0])
    for i, num in enumerate(nums):
        num = int(num)
        if num > prev_num:
            step_up = i
        elif num < prev_num:
            step_down = i
            break
        prev_num = num
    if step_down == 0:
        return nums
    n = len(nums)
    # Convert everything after step_up to '9'
    tail = '9' * (n - step_up - 1)
    # Make the step_up index minus 1 since it can afford it
    # (since the preceding number was definitely at least 1 step below)
    pivot = int(nums[step_up])
    # Note: step_up can be 0 if there was never any step up, e.g. '111111'
    # Note: if nums[step_up] was '1', e.g. for '11111', there will be a
    # leading 0 which we will strip later
    pivot -= 1
    # Keep as much of the head as possible to be closest to original number
    head = nums[:step_up]
    # Note: if step_up was 0, head will be empty
    return (head + str(pivot) + tail).lstrip('0')


if __name__ == "__main__":
    cases = int(input())

    for case in range(1, cases+1):
        nums = input()
        print("Case #{}: {}".format(case, tidy_number(nums)))

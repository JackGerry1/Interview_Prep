from typing import List


def bruteForceFindMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    output = nums1 + nums2
    output = sorted(output)
    res = 0
    l = 0
    r = len(output) - 1

    if len(output) % 2 == 0:
        mid1 = (l + r) // 2
        mid2 = (l + r) // 2 + 1

        res = (output[mid1] + output[mid2]) / 2

    else:
        mid = (l + r) // 2
        res = output[mid]

    return float(res)


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    A, B = nums1, nums2
    total = len(A) + len(B)
    half = total // 2

    # Ensure A is the smaller array
    if len(B) < len(A):
        A, B = B, A

    l, r = 0, len(A) - 1

    while True:  # loop until return
        i = (l + r) // 2  # A's partition
        j = half - i - 2  # B's partition

        Aleft = A[i] if i >= 0 else float("-infinity")
        Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
        Bleft = B[j] if j >= 0 else float("-infinity")
        Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

        # partition is correct
        if Aleft <= Bright and Bleft <= Aright:
            # odd total length
            if total % 2:
                return min(Aright, Bright)

            # even median calculation
            else:
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

        elif Aleft > Bright:
            r = i - 1
        else:
            l = i + 1


nums1 = [1, 3]
nums2 = [2]

nums3 = [1, 2]
nums4 = [3, 4]

print(findMedianSortedArrays(nums1, nums2))
print(findMedianSortedArrays(nums3, nums4))

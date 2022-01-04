def findMedianSortedArrays(nums1, nums2):

    res = []

    while nums1 and nums2:

        if nums1[0] < nums2[0]:

            item = nums1.pop(0)
            res.append(item)

        else:

            item = nums2.pop(0)
            res.append(item)

    if nums1:

        res.extend(nums1)

    elif nums2:

        res.extend(nums2)

    if len(res) == 1:

        return res[0]

    elif len(res) % 2 == 0:

        md = int((len(res) / 2) - 1)

        return sum(res[md:md + 2]) / 2

    else:

        return res[len(res) // 2]
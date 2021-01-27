""" 1109. Corporate Flight Bookings

There are n flights, and they are labeled from 1 to n.
We have a list of flight bookings.
The i-th booking bookings[i] = [i, j, k] means that we booked k seats from flights labeled i to j inclusive.
Return an array answer of length n, representing the number of seats booked on each flight in order of their label.

Example 1:
    Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
    Output: [10,55,45,25,25]

Example 2:
    Input: bookings = [[2, 2, 35], [1, 2, 10]], n = 2
    Output: [10, 45]
    
Example 3:
    Input: [[2,2,30],[2,2,45]], n = 2
    Output: [0,75]

Constraints:
    1 <= bookings.length <= 20000
    1 <= bookings[i][0] <= bookings[i][1] <= n <= 20000
    1 <= bookings[i][2] <= 10000
"""
from collections  import defaultdict
from typing       import List
from python.utils import CommonUtils


class Solution:
    
    @CommonUtils.logging_time
    def corpFlightBookings_v1(self, bookings: List[List[int]], n: int) -> List[int]:
        books = defaultdict(int)
        answer_list = [0] * n
        
        for i in range(len(bookings)):
            for j in range(bookings[i][0], bookings[i][1] + 1):
                books[j] += bookings[i][2]
        
        for i, v in enumerate(sorted(books.items())):
            answer_list[i] = v[1]
        
        print(answer_list)
        
        return answer_list


if __name__ == "__main__":
    solution = Solution()
    
    # test case 1
    booking_list_1  = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
    flight_number_1 = 5

    # test case 2
    booking_list_2  = [[2, 2, 35], [1, 2, 10]]
    flight_number_2 = 2

    # test case 3
    booking_list_3  = [[2, 2, 30], [2, 2, 45]]
    flight_number_3 = 2
    
    r1 = solution.corpFlightBookings_v1(booking_list_1, flight_number_1)
    r2 = solution.corpFlightBookings_v1(booking_list_2, flight_number_2)
    r3 = solution.corpFlightBookings_v1(booking_list_3, flight_number_3)
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda x: x[1])      #sort by finishing deadline
        heap = []       #max heap stores the duration of courses completed
        curr_day = 0
        course_completed = 0
        for duration, deadline in courses:
            curr_day += duration    #complete the curr course
            heapq.heappush(heap, -duration)
            course_completed +=1
            #if curr course cannot be completed before its deadline
            if curr_day > deadline:
                # remove the longest course bcz removing the longest course gives us the max time to complete other courses
                #eg:- heap = 3,5,2,7 removing course with duration 7 here give us the max time/days to complete further course(let duration be 4 and another be 1)
                longest_course = -heapq.heappop(heap)  
                curr_day -= longest_course
                course_completed -= 1
        return course_completed
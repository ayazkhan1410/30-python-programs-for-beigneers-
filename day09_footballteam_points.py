'''Day 9 of '30 days of 30
   Programs challenege '''



'''Our football team has finished the championship.
matches = ["2:1", "1:1", "3:2", "4:0"] 

The rules to calculate score is
a. If x > y: 3 points
b. If x < y: 0 point
c. If x = y: 1 point
 We need to write a function that
takes this collection and returns the number of points'''

def func(matches):
    total_points = 0
    for match in matches:
        x_str,y_str = match.split(':')
        
        x = int(x_str)
        y = int(y_str)
        
        if x>y:
            total_points+=3
        else:
            total_points+=1
    return total_points


matches = ["2:1", "1:1", "3:2", "4:0"] 
result = func(matches)
print(f"Total points : {result}")
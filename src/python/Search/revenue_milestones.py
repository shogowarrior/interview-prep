def get_milestone_days(revenues, milestones):
    result = [0] * len(milestones)
    
    # Sort milestones with their original indices, so we can map back results later
    # Each entry is (milestone_value, original_index)
    sorted_milestones = sorted([(m, i) for i, m in enumerate(milestones)])
    
    index = 0
    sum = 0
    for day, revenue in enumerate(revenues):
        sum += revenue  # Add today's revenue to the total
        
        # Check if we've reached or surpassed any milestones
        while (index < len(sorted_milestones) and
               sum >= sorted_milestones[index][0]):
            
            # Get the milestone and its original index
            # Record the day (1-indexed) this milestone was met
            result[sorted_milestones[index][1]] = day + 1
            
            # Move to the next milestone
            index += 1
            
    return result


revenues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
milestones = [100, 200, 500]
output = [4, 6, 10]
print(get_milestone_days(revenues, milestones))

revenues = [100, 200, 300, 400, 500]
milestones = [300, 800, 1000, 1400]
output = [2, 4, 4, 5]
print(get_milestone_days(revenues, milestones))
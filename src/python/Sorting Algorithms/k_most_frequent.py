
# Following the release of enhanced search capabilities to take into account listing attribute inheritance, we want to measure any increase in trip satisfaction rates and host/guest experiences. To better analyze feedback and tickets customers reported, we would like to have a simple function that can tell us the most frequent keywords among these free text forms, which aid in measuring the overall sentiment pertaining to a trip.  

# Question: Write a function that would take a string as an argument and an integer n, and output the top n frequent words in the string.



from collections import Counter
import re

def topFrequent(input_str, n):
    words = re.findall(r'\w+', input_str.lower())
    wordsFrequency = Counter(words)

    sorted_words = sorted(wordsFrequency.items(), key=lambda x: (-x[1], x[0]))

    top_n_words = [word for word, freq in sorted_words[:n]]
    print("Top N Frequent Words:", top_n_words)
    return top_n_words
    
    return None
    
input_str = "Very good location as well as the facilities. Highly recommended. Everything was perfect!!! Super recommended. The house is nice, clean, in good condition. Communication was very prompt and we had no problems."
topFrequent(input_str, 4)
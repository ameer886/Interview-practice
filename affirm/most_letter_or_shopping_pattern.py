# Given an input list of strings, for each letter appearing anywhere 
# in the list, find the other letter(s) that appear in the most 
# number of words with that letter.

# Example: 
# ['abc', 'bcd', 'cde'] =>
#   {
# 	a: [b, c],	# b appears in 1 word with a, c appears in 1 word with a
# 	b: [c], 	# c appears in 2 words with b, a and d each appear in only 1 word with b
# 	c: [b, d], 	# b appears in 2 words with c, d appears in 2 words with c. But a and e each 
# 					  appear in only 1 word with c.
# 	d: [c],		# c appears in 2 words with d. But b and e each appear in only 1 word with d
# 	e: [c, d], 	# c appears in 1 word with e, d appears in 1 word with e	
#   }

def max_pattern(words):
    letter_pattern_count = {}
    for word in words:
        for i, let_1 in enumerate(word):
            if let_1 not in letter_pattern_count.keys():
                letter_pattern_count[let_1] = {}

            for j, let_2 in enumerate(word):
                if i == j:
                    continue

                letter_pattern_count[let_1][let_2] = letter_pattern_count[let_1].get(let_2, 0) + 1
    
    result = {}
    for letter, count_map in letter_pattern_count.items():
        max_count = 0
        l = []

        for let, cnt in count_map.items():
            if cnt > max_count:
                l = []
                max_count = cnt
            
            if cnt == max_count:
                l.append(let)
            
        
        result[letter] = l
    return result


print(max_pattern(['abc', 'bcd', 'cde']))

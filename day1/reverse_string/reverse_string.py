import sys

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reversed_words = []
        for word in words:
            word = word[::-1]
            reversed_words.append(word)
        return " ".join(reversed_words)

    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 reverse_string.py <input_string>")
    else:
        input_string = sys.argv[1]
        
        solution = Solution()
        
        result = solution.reverseWords(input_string)
        print(result)

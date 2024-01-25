class Solution:
    def isPalindrome(self, x: int) -> bool:
        numbers = ' '.join(str(x)).split()
        for i, number in enumerate(numbers[:len(numbers) // 2]):
            if number != numbers[-(i+1)]:
                return False
        return True

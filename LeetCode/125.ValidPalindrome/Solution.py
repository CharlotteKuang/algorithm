class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        def alphanumeric(cur_s):
            return 'a' <= cur_s < 'z' or '0' <= cur_s <= '9'
        p1 = 0
        p2 = len(s)-1
        while p1 < p2:
            s1 = s[p1].lower()
            s2 = s[p2].lower()
            if alphanumeric(s1) and alphanumeric(s2):
                if s1 != s2: return False
                p1 += 1
                p2 -= 1
            else:
                if not alphanumeric(s1):
                    p1 += 1
                if not alphanumeric(s2):
                    p2 -= 1
        return True

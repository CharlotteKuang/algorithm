import pdb
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        preorder_list = preorder.split(",") 

        if len(preorder_list) == 0:    
            return True

        if preorder_list[0] == "#":
            return len(preorder_list) == 1

        s = [2] 
        preorder_list.pop(0)

        while len(s) and len(preorder_list): 
            if preorder_list[0] == "#":
                s[-1] -= 1
                while s and s[-1] == 0: 
                    s.pop() 
                    if s: s[-1] -= 1
            else:
                s.append(2)
            preorder_list.pop(0)
        return len(s) == 0 and len(preorder_list) == 0

if __name__ == "__main__":

    sol = Solution()

    cases = [
        "9,3,4,#,#,1,#,#,#,2,#,6,#,#",
        "9,3,4,#,#,1,#,#,2,#,6,#,#",
        "1,#",
        "9,#,#,1",
        "9,1,2,#,#,#,#",
        "9,#,4,#,#",
        "9,#,4,#",
        "#",
        "",
    ]

    for case in cases:
        print sol.isValidSerialization(case)

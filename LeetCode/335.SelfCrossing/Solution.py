import pdb

class Solution(object):
    def isGettingSmaller(self, bound, pos, arr, idx):
        for i in range(idx, len(arr)):
            mod = i % 4
            if mod == 0:
                if arr[i]+pos[1] >= bound["top"]: return False
                pos[1] += arr[i]
                bound["top"] = pos[1]
            if mod == 1:
                if pos[0]-arr[i] <= bound["left"]: return False
                pos[0] -= arr[i]
                bound["left"] = pos[0]
            if mod == 2:
                if pos[1]-arr[i] <= bound["bottom"]: return False
                pos[1] -= arr[i]
                bound["bottom"] = pos[1]
            if mod == 3:
                if pos[0]+arr[i] >= bound["right"]: return False
                pos[0] += arr[i]
                bound["right"] = pos[0]
        return True

    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """ 
        #pdb.set_trace()
        l = len(x)
        if l <= 3: return False

        rect = [(0,0),(0,x[0]),(-x[1],x[0]),(-x[1],x[0]-x[2])]
        cur_pos = [-x[1],x[0]-x[2]]

        if x[2] <= x[0]:
            bound = {
                "top": x[0],
                "right": 0,
                "bottom": x[0]-x[2],
                "left": -x[1],
            }
            return not self.isGettingSmaller(bound, cur_pos, x, 3) 

        if l >= 4 and x[3]-x[1] <= 0:
            cur_pos[0] += x[3]
            bound = {
                "top": x[0],
                "right": 0,
                "bottom": x[0]-x[2],
                "left": -x[1],
            }
            if x[3] == x[1]:
                bound["top"] = 0 
            return not self.isGettingSmaller(bound, cur_pos, x, 4) 

        cur_pos[0] += x[3]
        tmp = [(cur_pos[0],cur_pos[1])] 

        for i in range(4, l):
            mod = i % 4
            flag = False
            bound = None
        
            if mod == 0:
                cur_pos[1] += x[i]
                bottom = rect[0][1]
                top = rect[1][1]
                if cur_pos[1] <= top:
                    flag = True
                    if bottom <= cur_pos[1]: 
                        bound = {
                           "top": cur_pos[1],
                           "left": rect[0][0],
                           "bottom": cur_pos[1]-x[i],
                           "right": cur_pos[0],
                        }
                    else:
                        bound = {
                           "top": cur_pos[1],
                           "left": rect[2][0],
                           "bottom": cur_pos[1]-x[i],
                           "right": cur_pos[0],
                        }
            
            if mod == 1:
                cur_pos[0] -= x[i]
                left = rect[2][0]
                right = rect[1][0]
                if cur_pos[0] >= left:
                    flag = True
                    if cur_pos[0] <= right: 
                        bound = {
                           "top": cur_pos[1],
                           "left": cur_pos[0],
                           "bottom": rect[1][1],
                           "right": cur_pos[0]+x[i],
                        }
                    else:
                        bound = {
                           "top": cur_pos[1],
                           "left": cur_pos[0],
                           "bottom": rect[3][1],
                           "right": cur_pos[0]-x[i],
                        }

            if mod == 2:
                cur_pos[1] -= x[i]
                top = rect[1][1]
                bottom = rect[3][1]
                if cur_pos[1] >= bottom:
                    flag = True
                    if cur_pos[1] >= top:
                        bound = {
                           "top": cur_pos[1]-x[i],
                           "left": cur_pos[0],
                           "bottom": rect[1][1],
                           "right": tmp[1][0],
                        }
                    else:
                        bound = {
                           "top": cur_pos[1]-x[i],
                           "left": cur_pos[0],
                           "bottom": rect[3][1],
                           "right": tmp[3][0],
                        }

            if mod == 3:
                cur_pos[0] += x[i] 
                left = rect[3][0]
                right = rect[0][0]
                if cur_pos[0] <= right:
                    flag = True
                    if cur_pos[0] <= left:
                        bound = {
                           "top": tmp[2],
                           "left": cur_pos[0],
                           "bottom": cur_pos[1],
                           "right": rect[3][0],
                        }
                    else:
                        bound = {
                           "top": rect[2][1],
                           "left": rect[3][0],
                           "bottom": cur_pos[1],
                           "right": cur_pos[0],
                        }

            if flag: return not self.isGettingSmaller(bound, cur_pos, x, i+1)

            tmp.append((cur_pos[0], cur_pos[1]))
            if len(tmp) == 4:
                rect = [tmp[0], tmp[1], tmp[2], tmp[3]]
                tmp = []

        return False

if __name__ == "__main__":
    sol = Solution()

    cases = [
        [2,1,4,4,3,2,2,1,1],
        [1,1,3,2,1,1],
        [1,1,2,2,3,3,4,4,10,4,4,3,3,2,2,1,1],
        [1,1,2,2,3,1,1],
        [1,1,2,1,1],
        [3,3,4,2,2],
        [2,1,1,2],
        [3,4,5,6,9,15,20,30,41],
        [10,9,8,7,6,5,4,3,2,1],
        [2, 1, 1, 2],
        [1, 2, 3, 4],
    ]

    for case in cases:
        print sol.isSelfCrossing(case)

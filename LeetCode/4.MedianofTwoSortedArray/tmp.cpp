#include<iostream>
using namespace std;

class Solution {
public:
    double findMedianSortedArrays(int A[], int m, int B[], int n) {
        int k = (m + n + 1) / 2;
        if ((m + n) & 1)
        return FindKthElm(A, 0, m - 1,B,0,n - 1, k);
        else
        return (FindKthElm(A, 0, m-1, B, 0, n - 1, k) + FindKthElm(A, 0, m - 1, B, 0, n - 1, k + 1)) / 2.0;
    }
    double FindKthElm(int A[], int aBeg, int aEnd, int B[], int bBeg, int bEnd, int k){
        if (aBeg > aEnd)
        {
            return B[bBeg + k - 1];
        }
        if (bBeg > bEnd)
        {
            return A[aBeg + k - 1];
        }
        
        int aMid = aBeg + (aEnd - aBeg)/2;
        int bMid = bBeg + (bEnd - bBeg)/2;
        
        int halfLen = aMid - aBeg + bMid - bBeg + 2;
        
        if (A[aMid] < B[bMid])
        {
            if (halfLen > k)
            return FindKthElm(A, aBeg, aEnd, B, bBeg, bMid - 1, k);
            else
            return FindKthElm(A, aMid + 1, aEnd, B, bBeg, bEnd, k - (aMid - aBeg + 1));
        }
        else
        {
            if (halfLen > k)
            return FindKthElm(A, aBeg, aMid - 1, B, bBeg, bEnd, k);
            else
            return FindKthElm(A, aBeg, aEnd, B, bMid + 1, bEnd, k - (bMid - bBeg + 1));
        }
    }
    
};

int main() {
	Solution test = Solution();
	int a[] = {1};
	int b[] = {1};
	cout << test.findMedianSortedArrays(a,1,b,1) << endl;
}

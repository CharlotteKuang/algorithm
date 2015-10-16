#include<stdio.h>

// Rearrange the arrays from the tails.
void merge(int* nums1, int m, int* nums2, int n) {
	int pos = m+n-1;	    
	int p1 = m-1;
	int p2 = n-1;

	while(p1 >= 0 && p2 >= 0) {
		int n1 = nums1[p1];
		int n2 = nums2[p2];
		if(n1 > n2) {
			nums1[pos] = n1;
			p1--;
		} else {
			nums1[pos] = n2;
			p2--;
		}
		pos--;
	}

	if(p1 < 0 && p2 < 0) {
		return;
	}
	
	int *p; 
	int leftp;
	if(p1 < 0) {
		p = nums2;
		leftp = p2;
	} else {
		p = nums1;
		leftp = p1;
	}
	for(int i = leftp; i >= 0; i--) {
		nums1[pos] = p[i];
		pos--;
	}
}

int main() {
	int a[] = {5,14,20,0,0,0,0,0};
	int b[] = {4,15,28,42};
	merge(a, 3, b, 4);

	for(int i = 0; i < 11; i++) {
		printf("%d\n", a[i]);
	}
}

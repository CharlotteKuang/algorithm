#include<stdio.h>
#include<stdlib.h>

int cmp(const void* p1, const void* p2) {
	return (*(int*)p1 - *(int*)p2);
}

void nextPermutation(int* nums, int numsSize) {
	if(numsSize == 2) {
		int tmp = nums[0];
		nums[0] = nums[1];	
		nums[1] = tmp;
	}

	if(numsSize > 2) {
		int pos = -1;
		int i;
		for(i = numsSize-2; i >= 0; i--) {
			if(nums[i] < nums[i+1]) {
				pos = i;
				break;
			}
		}
		if(pos >= 0 && pos < numsSize) {
			qsort(nums+pos+1, numsSize-pos-1, sizeof(int), cmp);
			for(i = pos+1; i < numsSize; i++) {
				if(nums[i] > nums[pos]) {
					int tmp = nums[i];
					nums[i] = nums[pos];
					nums[pos] = tmp;
					break;
				}
			}
		} else {
			qsort(nums, numsSize, sizeof(int), cmp);
		}
	}
}

int main() {
	int a[] = {1,2,4,3,1};	
	nextPermutation(a, 5);
	for(int i = 0; i < 5; i++) {
		printf("%d\n", a[i]);
	}
	printf("\n");

	int a1[] = {1,2,4};	
	nextPermutation(a1, 3);
	for(int i = 0; i < 3; i++) {
		printf("%d\n", a1[i]);
	}

	printf("\n");
	int a2[] = {3,2,1};	
	nextPermutation(a2, 3);
	for(int i = 0; i < 3; i++) {
		printf("%d\n", a2[i]);
	}
}

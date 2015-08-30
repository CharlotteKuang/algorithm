void rotate(int nums[], int n, int k) {
	if(k<=0||k%n==0) return;
	int count = 0;
	int origin = 0;
	int dest;
	int tmp2;
	while(count<n) {
		int start = origin;
		int tmp=nums[origin];
		do {
			dest=(origin+k)%n;
			tmp2=nums[dest];
			nums[dest]=tmp;
			tmp=tmp2;
			origin=dest;
			count++;
		} while(start!=origin);
		origin = start+1;
	}
}

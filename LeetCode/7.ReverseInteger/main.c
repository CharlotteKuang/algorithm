#include<stdio.h>

int reverse(int x) {
	int result = 0;
	int sign = 1;
	if(x < 0) {
		x = -x;
		sign = -1;
	}
	while(x > 0) {
		if(result * 10 / 10 != result) {
		return 0;
		}
		result = result * 10 + x % 10;
		x /= 10;
	}
	return sign * result;
}

int main() {
	int test = 1534236469;	
	printf("%d", reverse(test));
}

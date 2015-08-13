#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int titleToNumber(char* s) {
	int len = strlen(s);		    
	int res = 0;
	int weight = 1;
	for(int i = len - 1; i >= 0; i--) {
		res += (s[i] - 'A' + 1) * weight;
		weight *= 26;
	}
	return res;
}

int main() {
	char *s = "AB";
	int number = titleToNumber(s);
	printf("%d\n", number);

	char *s2 = "A";
	int number2 = titleToNumber(s2);
	printf("%d\n", number2);
}

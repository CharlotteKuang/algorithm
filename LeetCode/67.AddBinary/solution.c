#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* addBinary(char* a, char* b) {
	int c1 = strlen(a) - 1;
	int c2 = strlen(b) - 1;
	int carry = 0;
	int len = (c1 > c2 ? c1 : c2) + 3;
	int c = len - 2;
	char *result = (char*)malloc(len);
	memset(result, 0, sizeof(char)*len);
	while(c1 >= 0 && c2 >= 0) {
		int v1 = a[c1] == '1' ? 1 : 0;
		int v2 = b[c2] == '1' ? 1 : 0;
		result[c] = (char)('0' + (v1 ^ v2 ^ carry)); 
		carry = v1 + v2 + carry >= 2 ? 1 : 0;
		c--;
		c1--;
		c2--;
	}
	if(c1 >= 0 || c2 >= 0) {
		char* tmp = c1 < 0 ? b : a;
		int tmpc = c1 < 0 ? c2 : c1;
		while(tmpc >= 0) {
			int v = tmp[tmpc] == '1' ? 1 : 0;
			result[c] = (char)('0' + (v ^ carry));
			carry = v & carry;
			tmpc--;
			c--;
		}
	}
	result[len-1] = '\0';
	if(carry) {
		result[0] = '1';
		return result;
	} else {
		return result + 1;
	}
	return result;    
}

int main() {
	char a[10] = {'1', '0', '0'};
	char b[10] = {'1', '1', '0', '0', '1', '0'};
	char* result = addBinary(a, b);
	printf("%s\n", result);
}

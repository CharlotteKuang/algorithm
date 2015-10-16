#include<stdio.h>
#include<string.h>

void reverseWord(char *start, char *end) {
	while(start < end) {
		char tmp = *start;
		*start = *end;
		*end = tmp;
		start++;
		end--;
	}
}

void reverseWords(char *s) {
	//reverse the whole string		    
	int len = strlen(s);
	int count = 0;
	for(int i = 0; i < len; i++) {
		if((i == 0 && s[i-1] != ' ') || (i > 0 && s[i-1] != ' ')) {
			s[count] = s[i];
			count++;
		} 
	}
	s[count] = '\0';
	printf("%s\n", s);
	char*start = s;
	char*end = s+count-1;

	reverseWord(start, end);
}

void trimString(char *s) {

}

int main() {
	char str[] = "  1x3"; 
	reverseWords(str);
	printf("%s\n", str);
}

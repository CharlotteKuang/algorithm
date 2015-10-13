#include<stdlib.h>
#include<stdio.h>
#include<string.h>

void swapC(char *a, char *b)
{
    char tmp = *a; *a = *b; *b=tmp;
}

void rev(char* start, char* end)
{
    while(end>start)  swapC(end--, start++);
}

void reverseWords(char *s)
{
    /* For C programmers: Try to solve it in-place in O(1) space. */
    /* 3-step algorthm
     1. use runner/chaser to eliminate all unnecessary spaces
     2. rev the entire string
     3. rev word by word*/
    int len = strlen(s);
    if(len < 2 && !isspace(*s)) return;
    
    /* 1. trim off all unnecessary spaces */
    char* runner, *chaser;
    for(runner = s, chaser=s; *runner!='\0'; runner++)
    {
        if(isspace(*runner))
        {
            while(isspace(*(runner+1)) && *(runner+1)!=0) runner++;
            if(*(runner+1) == 0) break;
            if(chaser == s) continue;
        }
        if(runner!=chaser)    swapC(runner, chaser);
        chaser++;
    }
    *chaser = 0;
    len = strlen(s);
    
    /* 2. rev the entire string */
    rev(s, s+len-1);
    
    /* 3. rev word by word */
    for(char *wHead =s, *wTail=s; wHead < s+len; wHead = wTail+2)
    {
        for(wTail=wHead; !isspace(*(wTail+1)) && *(wTail+1) != 0; wTail++);
        rev(wHead, wTail);
    }
}

int main() {
	char c[] = "abc";
	reverseWords(c);
}

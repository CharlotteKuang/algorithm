#include<string>
#include<stdio.h>
#include<stdlib.h>

bool isNumber(char *s) {
	bool hasNum = false;
	bool hasFaction = false;
	bool hasTail = false;
	while(*s == ' ') s++; /* Skip space */
	if (*s == '-' || *s == '+') s++;   /* Has sign? */
	if (*s >= '0' && *s <= '9'){
		hasNum = true;
		do  s++;   while (*s >= '0' && *s <= '9'); /* Number? */ 
	}
	if (*s == '.') {
		s++;
		while(*s >= '0' && *s <= '9'){
			hasFaction = true;
			s++;
		}
		if(!hasNum && !hasFaction) return false;
	}  /* Fractional part? */ 
	if (*s == 'e' || *s == 'E')     /* Exponent? */
	{  
		if(!hasNum && !hasFaction) return false;
		s++;
		if (*s == '+') s++; 
		else if (*s == '-') s++;      /* With sign? */
		while (*s >= '0' && *s <= '9') s++, hasTail = true;   /* Number? */
		if(!hasTail) return false;
	} 
	while(*s == ' ') s++;
	return *s == '\0' && (hasNum || hasFaction);	
}



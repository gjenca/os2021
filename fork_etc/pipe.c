#include <stdio.h>
#include <unistd.h>

int main () {

	int fd[2];
	char buf[10];

	pipe(fd);
	write(fd[1],"abc",4);
	read(fd[0],buf,4);
	printf("%s\n",buf);
}



	


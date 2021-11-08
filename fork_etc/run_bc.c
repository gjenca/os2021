#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <string.h>

int main() {

	pid_t pid;
	int status;
	int pipe_l[2];
	int pipe_r[2];
	int i;
	int n;
	int result;
	char buf[100];
	char priklad[100];
	FILE *f;

	// Vytvorime 2 rury
	if (pipe(pipe_l)<0) {
		perror("pipe");
	}
	if (pipe(pipe_r)<0) {
		perror("pipe");
	}
	pid=fork();
	if (pid<0) {
		perror("fork");
	}
	if (pid>0) {
		// Parent
		// Zavrieme nepotrebne konce rur
		close(pipe_r[0]);
		close(pipe_l[1]);
		f=fdopen(pipe_l[0],"r");
		for (i=0;i<10;i++) {
			sprintf(priklad,"%d*8\n",i);
			// Zapiseme priklad
			write(pipe_r[1],priklad,strlen(priklad));
			// Citame z druhej rury, tam ma byt vysledok
			//fgets(buf,sizeof(buf),f);
			//fputs(buf,stdout);
			fscanf(f,"%d",&result);
			printf("%d\n",result);
		}
		// Zavrieme ruru
		close(pipe_r[1]);
		// Koniec suboru na druhej rure
		// cakame na ukoncenie child
		wait(&status);
	} else {
		// Zavrieme nepotrebne konce rur
		close(pipe_r[1]);
		close(pipe_l[0]);
		// Duplikujeme na stdin/out
		dup2(pipe_r[0],0);
		dup2(pipe_l[1],1);
		// Uz tie file descriptors na rurach nepotrebujeme
		close(pipe_r[0]);
		close(pipe_l[1]);
		if (execl("/usr/bin/bc","/usr/bin/bc",NULL)) {
			perror("execl");
		}
	}

}

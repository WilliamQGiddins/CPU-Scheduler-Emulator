//William Giddins Hw #3 init
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main (int argc, char* argv[]){
	int cp,sp,status;

cp=fork();
	if(cp==0){
	execlp("python3", "python3", "cpu_emulator.py", NULL);
}

sp=fork();
	if(sp==0){
        sleep(3);
	execlp("python3", "python3", "scheduler.py", NULL);
	

}

waitpid(sp,&status,0);
waitpid(cp,&status,0);

printf("Both Children Have Died\n");


return 0;
}




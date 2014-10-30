/*
 * 测试两个进程对文件的操作：读、写、追加！
 *
 * 结论：
 * 用FILE *fp = fopen()来打开文件得到的文件指针fp.
 * 在不同的进程中分别打开，读写都是两个进程独立的文件指针，对于w模式打开，不会
 * 覆盖，是替换，最后的文件内容以最后写入的进程为准。
 *
 * 对于append模式，文件指针不是独立的，会不断向文件中添加内容。
 */
#include <stdio.h>
#include <unistd.h>

#define FILENAME "test.txt"

int main(void)
{
    pid_t pid = -1;
#ifdef FORK_READ
    if (pid=fork() > 0)
    {
        if (fork() == 0)
        {
            sleep(3);
            FILE *fp = fopen(FILENAME,"r");
            char str[6] = {0};
            fgets(str,5,fp);
            printf("process=%d(parent=%d),line=%d,%s\n",getpid(),getppid(),__LINE__,str);
            fclose(fp);
        }
    }
    if (pid == 0)
    {
        FILE *fp = fopen(FILENAME,"r");
        char str[6] = {0};
        fgets(str,5,fp);
        printf("process=%d(parent=%d),line=%d,%s\n",getpid(),getppid(),__LINE__,str);
        fclose(fp);
    }
#endif
#ifdef FORK_WRITE
    if (pid=fork() > 0)
    {
        if (fork() == 0)
        {
            FILE *fp = fopen(FILENAME,"w+");
            printf("line=%d,fp=%x\n",__LINE__,*fp);
            fputs("pl,okmijn**************",fp);
            printf("process=%d(parent=%d),line=%d,fp=%x\n",getpid(),getppid(),__LINE__,*fp);
            //fclose(fp);
        }
    }
    if (pid == 0)
    {
        sleep(1);
        FILE *fp = fopen(FILENAME,"w+");
        printf("line=%d,fp=%x\n",__LINE__,*fp);
        fputs("karottc",fp);
        printf("process=%d(parent=%d),line=%d,fp=%x\n",getpid(),getppid(),__LINE__,*fp);
        //fclose(fp);
    }
#endif
#ifdef FORK_APPEND
    if (pid=fork() > 0)
    {
        if (fork() == 0)
        {
            FILE *fp = fopen(FILENAME,"a");
            printf("line=%d,fp=%x\n",__LINE__,*fp);
            fputs("pl,okmijn",fp);
            printf("process=%d(parent=%d),line=%d,fp=%x\n",getpid(),getppid(),__LINE__,*fp);
            fclose(fp);
        }
    }
    if (pid == 0)
    {
        FILE *fp = fopen(FILENAME,"a");
        printf("line=%d,fp=%x\n",__LINE__,*fp);
        fputs("karottc",fp);
        printf("process=%d(parent=%d),line=%d,fp=%x\n",getpid(),getppid(),__LINE__,*fp);
        fclose(fp);
    }
#endif
    int status;
    while (wait(&status) != -1) ;
    return 0;
}


#include <stdio.h>
#include <signal.h>
#include <time.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>

#define FILE_NAME           "databases.db"

void callFunction(union sigval arg);
int ctoi(char n);
int timeCal(char *buffer);

int main(int argc, char **argv)
{
    struct sigevent timersig;
    struct itimerspec timerval;
    timer_t timerId; 

    memset(&timersig, 0, sizeof(struct sigevent));
    memset(&timerval, 0, sizeof(struct itimerspec));

    timersig.sigev_notify = SIGEV_THREAD;
    timersig.sigev_signo = SIGRTMIN;
    timersig.sigev_notify_attributes = 0;
    timersig.sigev_notify_function = callFunction;

    timerval.it_value.tv_sec = 60;   // 60 seconds
    timerval.it_interval.tv_sec = 60;

    if (timer_create(CLOCK_MONOTONIC, &timersig, &timerId) < 0)
    {
        fprintf(stderr,"ERROR: wifiDisableTime process can't create timer!!\n");
        return -1;
    }
    if (timer_settime(timerId, 0, &timerval, NULL) < 0)
    {
        fprintf(stderr,"ERROR: wifiDisableTime process can't set timer!!\n");
        return -1;
    }
    
    while (1)
    {
        sleep(60);
    }
    return 0;
}

void callFunction(union sigval arg)
{
    size_t n;
    char *buffer = NULL;    // line-by-line read "database" file's buffer
    int flag = 0;
    if (access(FILE_NAME,F_OK) != 0)
    {
        fprintf(stderr,"ERROR: %s file don't exist !!\n",FILE_NAME);
        return;
    }
    FILE *fp = fopen(FILE_NAME, "r");
    if (fp == NULL)
    {
        fprintf(stderr,"ERROR: Can't open file %s !!\n",FILE_NAME);
        return;
    }
    
    while (!feof(fp))
    {
        if (getline(&buffer, &n, fp) > 0)
        {
            //// TODO: do someting
            // exmple,set flag bit
            flag = 1;
        }
    }
    fclose(fp);
    if (buffer)
    {
        free(buffer);
    }

    return;
}

int ctoi(char n)
{
    int result = -1;
    switch (n)
    {
        case '0':
            result = 0;
            break;
        case '1':
            result = 1;
            break;
        case '2':
            result = 2;
            break;
        case '3':
            result = 3;
            break;
        case '4':
            result = 4;
            break;
        case '5':
            result = 5;
            break;
        case '6':
            result = 6;
            break;
        case '7':
            result = 7;
            break;
        case '8':
            result = 8;
            break;
        case '9':
            result = 9;
            break;
        default:
            result = -1;
            break;
    }

    return result;
}

int timeCal(char *buffer)
{
    /* time format: dd/mm/yyyy-hh:mm-1 
     * the last bit is 1 - valid; 0 - invalid.
     */
    char cday[6],cmon[6],cyear[6],chour[6],cmin[6];
    int day,mon,year,hour,min;

    int flag = 0;
    struct tm object_time;
    time_t now_time = 0;
    time_t seconds = 0;

    strncpy(cday,buffer,2);
    strncpy(cmon,buffer+3,2);
    strncpy(cyear,buffer+6,4);
    strncpy(chour,buffer+11,2);
    strncpy(cmin,buffer+14,2);

    day = atoi(cday);
    mon = atoi(cmon);
    year = atoi(cyear);
    hour = atoi(chour);
    min = atoi(cmin);

    flag = ctoi(buffer[17]);

    object_time.tm_sec = 0;
    object_time.tm_min = min;
    object_time.tm_hour = hour;
    object_time.tm_mday = day;
    object_time.tm_mon = mon - 1;
    object_time.tm_year = year - 1900;

    time(&now_time);
    seconds = mktime(&object_time);

    if (now_time - seconds < 60 && now_time - seconds >= 0 && flag == 1)
        return 1;
    return 0;
}

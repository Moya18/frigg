#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

void *average(void *vargp);
void *minimum(void *vargp);
void *maximum(void *vargp);

int total, i, mini, maxi;
double average;
int *arr; 

int main(int argc, char *argv[]) {
	
	if (argc == 1) {
		fprintf(stderr,"You didn't specify any value => script.out <integer value>\n");
		return -1;
	}
	
	total = argc - 1;
	arr = (int*)malloc((total) * sizeof(int));
	for(i = 0; i < total; i++) arr[i] = atoi(argv[i+1]);
	
	pthread_t tid[3];
	
    pthread_create(&tid[0], NULL, average, NULL);
    pthread_create(&tid[1], NULL, mini, NULL);
    pthread_create(&tid[2], NULL, maxi, NULL);
    
    for(i = 0; i < 3; i++) pthread_join(tid[i], NULL);
    
    printf("Average: %.1lf \n", average);
    printf("Minimum: %d \n", mini);
    printf("Maximum: %d \n", maxi);
	
	return 0;
}

void *average(void *vargp)
{
	double sum = 0;
	for(i = 0; i < total; i++) sum += arr[i];
	average = sum / total;
    return NULL;
}

void *minimum(void *vargp)
{
	int min = arr[0];
	for(i = 0; i < total; i++) 
		if (arr[i] < min) min = arr[i];
	
	mini = min;
    return NULL;
}

void *maximum(void *vargp)
{
	int max = arr[0];
	for(i = 0; i < total; i++) 
		if (arr[i] > max) max = arr[i];
	
	maxi = max;
    return NULL;
}

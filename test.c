#include <wiringPi.h>
#include <stdio.h>
#include <time.h>


int main(void){
	const int coinGpio = 15;
	const int aGpio = 0;
	const int bGpio = 1;
	const int cGpio = 16;
	wiringPiSetup();
	pinMode(coinGpio, INPUT);
	pinMode(aGpio, INPUT);	
	pinMode(bGpio, INPUT);
	pinMode(cGpio, INPUT);
	time_t start = time(NULL);
	int coin = 0;
	int lastState = digitalRead(gpio);
	for(time_t cur = start; cur - start < 20; cur = time(NULL))
	{	
		int curState = digitalRead(gpio);
		
		if(curState == 1 && lastState == 0)
		{
			coin++;
			printf("[%d] Coincidence, Time: %d \n", coin, (int)(cur-start));
		}
		lastState = curState;
	}
	printf("Coincidences: %i \n",coin);
}

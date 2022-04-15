#include <wiringPi.h>
#include <iostream>
#include <chrono>
#include <vector>
#include <algorithm>
#include <string>
#include <memory>

class Pin {
	public:
		Pin(int nr) 
			:
			id(nr)
		{ 
			pinMode(id, INPUT);
		}
		Pin(const Pin&) = default;
		Pin(Pin&&) = default;
		int Read() { 
			auto cur = digitalRead(id);
			slope = cur - old;
			old = cur;
			return old;
		}
		bool Slope() const
		{
			return slope > 0;
		}
		bool UpdateSlope()
		{
			Read();
			return Slope();
		}
	private:
		int id;
		int old = 0;
		int slope = 0;
};

int main(void){
	wiringPiSetup();
	//Coincidence
	Pin pin(15);
	int coin = 0;
	const double maxTime = 600.0;
	const int boxes = 20;
	std::array<int, boxes> graph = { 0 };
	pin.Read();
	std::chrono::time_point<std::chrono::steady_clock> start = std::chrono::steady_clock::now();
	std::chrono::time_point<std::chrono::steady_clock> cur = start;
	std::chrono::duration<double> diff = cur-start;
	for(; diff.count() < maxTime; cur = std::chrono::steady_clock::now(), diff = cur-start)
	{	
		if(pins.at(i).UpdateEvent()) 
		{
			coin++;
			std::cout << "[" << (int)diff.count() << "]s \t [" << realCoin << "] Coincidences" << std::endl;
			graph.at((int)diff.count() % ((int)maxTime/boxes))++;
		}
	}
	auto m = std::max_element(graph.begin(), graph.end());
	for(int i = 0; i < boxes; i++)
	{
		std::cout << 
	}
	
}

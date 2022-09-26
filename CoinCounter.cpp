#include <wiringPi.h>
#include <iostream>
#include <iomanip>
#include <numeric>
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

int main(int argc, char* argv[]){
	std::vector<std::string> args;
	for(int i = 0; i < argc; i++)
	{
		args.push_back(std::string(argv[i]));
	}
	if(argc != 3)
	{
		std::cout << "Use: ./test <maxTime> <boxes>" << std::endl;
		return 0;
	}
	
	wiringPiSetup();
	//Coincidence
	Pin pin(15);
	int coin = 0;
	double maxTime = std::stod(args.at(1));
	int boxes = std::stoi(args.at(2));
	std::vector<int> graph(boxes, 0);
	pin.Read();
	std::chrono::time_point<std::chrono::steady_clock> start = std::chrono::steady_clock::now();
	std::chrono::time_point<std::chrono::steady_clock> cur = start;
	std::chrono::duration<double> diff = cur-start;
	for(; diff.count() < maxTime; cur = std::chrono::steady_clock::now(), diff = cur-start)
	{	
		if(pin.UpdateSlope()) 
		{
			coin++;
			std::cout << "[" << (int)diff.count() << "]s \t [" << coin << "] Coincidences" << std::endl;
			graph.at((int)(diff.count() * (double) boxes / maxTime)) += 1;
		}
	}
	std::cout << std::endl;
	auto m = std::max_element(graph.begin(), graph.end());
	for(int i = 0; i < *m; i++)
	{
		for(int j = 0; j < boxes; j++)
		{
			std::cout << (graph.at(j) >= *m -i ? "====" : "    ");
		}
		std::cout << std::endl;
	}
	for(int j = 0; j < boxes; j++)
	{
		std::cout << "----";
	}
	std::cout << std::endl;
	for(int j = 0; j < boxes; j++)
	{
		std::cout << " " << std::setw(3) << graph.at(j);
	}
	std::cout << std::endl;
	for(int j = 0; j < boxes; j++)
	{
		std::cout << "[" << std::setw(2) << j+1 << "]";
	}
	std::cout << std::endl;
}

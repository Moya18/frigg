#include <iostream>
#include <vector>
#include <algorithm>
#define oo 10000000

using namespace std;

int X[10001];

int main()
{
	int numCoins, quantity, i, j, coin;
	vector<int> Coin;
	
	cin >> numCoins >> quantity;
	
	for(i=0; i<numCoins; i++)
	{
		cin >> coin;
		Coin.push_back(coin);
	}
	
	for(i=0; i<=quantity; i++)
		X[i] = 1;
	
	X[0] = 0;
	
	for(i=0; i<numCoins; i++)
	{
		coin = Coin[i];
		for(j=quantity; j>=coin; j--)
			X[j] += X[j-coin];
			
		for(int x = 0; x < quantity; x++) cout << X[x] << "   ";
		
		cout << endl;
	}
	
	cout << X[quantity] << endl;
	
	return 0;
}

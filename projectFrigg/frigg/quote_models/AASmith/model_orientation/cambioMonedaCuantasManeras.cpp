#include <iostream>
#include <vector>
#include <algorithm>
#define oo 10000000

using namespace std;

int X[10001];

int main()
{
	int n, k, i, j, c;
	vector<int> Coin;
	
	cin >> n >> k;
	
	for(i=0; i<n; i++)
	{
		cin >> c;
		Coin.push_back(c);
	}
	
	for(i=0; i<=k; i++)
		X[i] = 1;
	
	X[0] = 0;
	
	for(i=0; i<n; i++)
	{
		c = Coin[i];
		for(j=k; j>=c; j--)
			X[j] += X[j-c];
	}
	
	cout << X[k] << endl;
	
	return 0;
}

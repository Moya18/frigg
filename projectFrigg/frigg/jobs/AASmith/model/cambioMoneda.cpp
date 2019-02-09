// this algorithm answers the question to what is the minimum amount of coins needed to pay a certain amount of money

// $$       0 1 2 3 4 5 6 7 8 9 10
// Coins    0 1 1 2 2 1 2 2 3 3 2

#include <iostream>
#include <vector>
#include <algorithm>
#define oo 10000000 // define an infinite number
using namespace std;

int X[10001];

int main() {
    
    int numCoins, money;
    vector <int> coinArr;
    
    cin >> numCoins >> money;
    
    // get values of individual coins
    for (int i=0; i<numCoins; i++) {
        int coin;
        cin >> coin;
        coinArr.push_back(coin);
    }
    
    // set array to infinites
    for (int i=0; i<=money; i++) X[i] = oo;
    
    X[0] = 0;
    
    // fibonacci loop to get min amount of coins
    for (int i=0; i<numCoins; i++) {
        int coin = coinArr[i];
        for (int j=coin; j<=money; j++){
        	X[j] = min(X[j], X[j-coin] +1);
        	//for(int x = 0; x <= money; x++) cout << X[x] << "   ";
       		//cout << endl;
		} 
        
    }
    
    cout << X[money] << endl;
    
    return 0;
}



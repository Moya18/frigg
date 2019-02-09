#include <iostream>
using namespace std;
int a, m, b;
long long bigmod();

int main(){
	cin >> a >> b >> m;
	cout << bigmod();
}

long long bigmod(){
	int p = 1;
	while(b > 0){
		if(b % 2 == 1){
			p = (p * a) % m;			
		}
		a = (a * a) % m;
		b /= 2;
	}
	return p;
}

#include <iostream>
#define N 1000

using namespace std;

int X[N], L[N], P[N];
int n;

void printSequence(int);

int main()
{
    int i, j, k;
    
    cin >> n;
    
    for(i=0; i<n; i++)
        cin >> X[i];
    
    k = 0;
    for(i=0; i<n; i++)
    {
        L[i] = 1;
        P[i] = -1;
        
        for(j=0; j<i; j++)
        {
            if(X[j] > X[i] && L[j]+1 > L[i])
            {
                L[i] = L[j] + 1;
                P[i] = j;
            }
        }
        
        if(L[i] > L[k])
            k = i;
    }
    
    cout << L[k] << endl;
    printSequence(k);
    
    return 0;
}

void printSequence(int k)
{
    if(k == -1)
        return;
    
    printSequence(P[k]);
    cout << k << " ";
}

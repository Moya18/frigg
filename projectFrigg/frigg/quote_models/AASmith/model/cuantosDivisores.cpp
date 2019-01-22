#include <iostream>
#include <math.h>
using namespace std;
int main(){
int x;
int sum=0;
cin>>x;

int i =1;
for(i ;i<=sqrt(x); i++)
{
   if(x%i==0){

        if (x/i == i)
               sum++;
 
        else
            sum = sum+2;
   }
        
       
}
cout<<sum;
}

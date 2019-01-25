#include <iostream>
#include <string.h>
#include <fstream>
using namespace std;

struct estructura{
    int x;
    char c[5];
};

int main(){
    //Creamos la estructura en memoria
    estructura a1;
    
    //Rellenar la estructura con datos ejemplo
    a1.x=10;
    strcpy(a1.c, "bye");
    
    
    char bytes[512], bytes2[512];
    
    //Convertimos la estructura a un arreglo de bytes
    memcpy(bytes, &a1, sizeof(a1));
    
    //Guardamos nuestro arreglo de bytes como archivo binario
    ofstream file("datos");
    file.write(bytes, 512);
    file.close();
    //FIN DE LA PARTE DE ESCRITURA
    
    //INICIA LA PARTE DE LECTURA
    
    //Leemos la información previamente guardada y la escribimos en un arreglo de bytes
    ifstream file2("datos");
    file2.seekg(0, ios::beg);
    file2.read(bytes2, 512);
    file2.close();

    //Esto es para revisar la información byte por byte original y copia
    for (int i=0; i<9;i++)
        cout<<"  "  << (int)bytes[i]<<"\t"  << (int)bytes2[i]<<endl;
        
    //Formateamos nuevamente la información con la estructura previamente utilizada
    estructura a2;
    memcpy(&a2, bytes2, sizeof(a2));
    cout<<a2.x <<" " << a2.c;
    
    return 0;
}

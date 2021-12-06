#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;

ifstream loadFile(string filename){
    ifstream input;
    input.open(filename);

    if(!input.is_open()){
        throw "Couldnt open file";
    }

    if (input.is_open()) { 
        /* ok, proceed with output */ 
        cout << "Opened file\n";
        }
    else {
        cout << "NONO!\n";
    }
    return input;
}

int numberOfLines(string filename){
    int number_of_lines = 0;
    std::string line;
    ifstream dataFile=loadFile("dec5_input.txt");

    while (getline(dataFile, line))
        ++number_of_lines;
    std::cout << "Number of lines in text file: " << number_of_lines;

    return -1; //numberoflines but not working now
}


int main(){

    string filename= "dec5_input_test.txt";
    
    ifstream data=loadFile(filename);


    string line;
    while (getline(data,line)) {
        

        //getline(data,line,'>');
        

        //stringstream ss(line);
        //while(getline(ss,line,'-')){
        //    cout << line << endl;
        //}


        istringstream myStream(line);
        string n;
        
        cout << "######" << endl;
        for (int i=0;i<3;i++){
            myStream >> n;
            string la;
            cout << n << endl;
            cout << "la " << la << endl;
        }
        

        //cout << line << endl;

        







        //string hello;

        //int x1, y1, x2,y2;
        //data >> hello;

    }

    //data.close();




    /*
    

    string line;
    if (dataFile.is_open()){
        while(getline(dataFile,line)){
            cout << line << "\n";
        }
    }

    int a[10];
    int b[] {1,2,3,4};

    cout << "the size is: " << sizeof(a) << endl;
    cout << "the size is: " << sizeof(b) << endl;
    cout << b[0] << endl;

    //for (int i=0;i<sizeof(a);i++){
    //    cout << a[i] << endl;
    //}
    data.close();

    if (data.is_open() != true){
        cout << "File is closed\n";
    }
    */
    
    return 0;

}
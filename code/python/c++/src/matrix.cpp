#include "matrix.hpp"

void FileReading(){

    int line = 12, column = 12;

    int My_matrix[line][column];

    ifstream myfile;

	myfile.open("table.txt");

	if (myfile.is_open()) {

		while(!myfile.eof()) {

            for(int i = 0; i < line; i++){

                for(int j = 0; j < column; j++){

                    My_matrix[i][j] = i;

                    float Inv_matrix[line][column];

                    for (int x = line-1; x >= 0; x--){

                        for (int y = column - 1; y >= 0; y--){

                            
                            cout<< Inv_matrix[x][y]<<endl;
                        }

                        cout<<endl;
                    }

                }
            }
			
		}
	}else
        cout << "Unable to open file";

	myfile.close();
}
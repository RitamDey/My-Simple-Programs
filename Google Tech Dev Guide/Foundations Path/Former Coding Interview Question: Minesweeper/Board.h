#ifndef MATRIX_CLASS_H
#define MATRIX_CLASS_H
#include <vector>
#include <iostream>
#include "Cell.h"
using namespace std;


class Board {
    using matrix = vector<vector<Cell>>;
    private:
    int n_rows;
    int n_cols;
    matrix board;
    void populate_mines();
    void populate_neighbour(int r, int c);
    vector<pair<int, int>> neighbours(pair<int, int> cell);

    public:
    Board(int rows, int cols);
    int at(int row, int col);
    int rows();
    int columns();

    friend ostream& operator<<(ostream& stream, Board& obj);
};

#endif

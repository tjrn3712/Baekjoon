#include "coins.h"

std::vector<int> coin_flips(std::vector<int> b, int c) {
    std::vector<int> flips(1);
    int x = 0;
    for (int i=0;i<64;i++) if (b[i]) x^=i;
    return {x^c};
}

int find_coin(std::vector<int> b) {
    int x = 0;
    for (int i=0;i<64;i++) if (b[i]) x^=i;
    return x;
}

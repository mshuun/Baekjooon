#include "aplusb.h"
#include <vector>
#include <utility>

static std::vector<int> gA, gB;

void initialize(std::vector<int> A, std::vector<int> B) {
  gA = std::move(A);
  gB = std::move(B);
}

int answer_question(int i, int j) {
  return gA[i] + gB[j];
}
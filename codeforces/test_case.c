#include <stdio.h>
#include <stdlib.h>

int main() {
  int n = 200000;
  int m = 9007;
  printf("1\n");
  printf("%d %d\n", n, m);
  for (int i = 0; i < n; i++) {
    if (i == n - 1) {
      printf("%d\n", (rand() % 999));
    } else {
      printf("%d ", (rand() % 999));
    }
  }
  for (int i = 0; i < n; i++) {
    printf("%c", (rand() % 2) ? 'L' : 'R');
  }
  printf("\n");
}

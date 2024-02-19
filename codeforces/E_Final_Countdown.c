#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
  int t;
  scanf("%d", &t);
  for (int j = 0; j < t; j++) {
    int n, dig_sum, carry, value;
    scanf("%d", &n);
    char s[n], new_sum[n + 1];
    memset(new_sum, '0', sizeof(s));
    scanf("%s", s);
    dig_sum = 0;
    int sum_arr[n];
    memset(sum_arr, 0, sizeof(sum_arr));

    for (int i = 0; i < n; i++) {
      dig_sum += s[i] - '0';
      sum_arr[i] = dig_sum;
    }

    carry = 0;
    for (int i = n - 1; i >= 0; i--) {
      dig_sum = sum_arr[i] + carry;
      value = dig_sum % 10;
      carry = dig_sum / 10;
      new_sum[i + 1] = value + '0';
      // printf("Value: %d, Carry: %d\n", value, carry);
    }

    n++;
    if (carry) {
      new_sum[0] = carry + '0';
    }

    new_sum[n] = '\0';

    int start = 0;
    // printf("Start: %d\n", start);
    while (new_sum[start] == '0') {
      start++;
    }

    printf("%s\n", new_sum + start);
  }
}
#include <stdlib.h>
#include <stdio.h>

void reverse(int* nums, int size) {
    int temp = 0;

    for (int i = 0; i < size / 2; i++) {
        temp = nums[i];
        nums[i] = nums[size - i - 1];
        nums[size - i - 1] = temp;
    }
}

int* sortedSquares(int* nums, int numsSize, int* returnSize) {
    // Variables
    int start, end, appendCounter;
    int* returnArray;

    // Allocate and Assign
    returnArray = (int*) malloc(sizeof(int) * numsSize);

    if (returnArray == NULL) {
        printf("ALLOCATION FAILED\n");
        exit(-1);
    }

    start = 0;
    end = numsSize - 1;
    appendCounter = 0;

    while(start <= end) {
        if ( abs(nums[start]) >= abs(nums[end]) ) {
            returnArray[appendCounter] = nums[start] * nums[start];
            start++;
        }
        else {
            returnArray[appendCounter] = nums[end] * nums[end];
            end--;
        }

        appendCounter++;
    }

    reverse(returnArray, *returnSize);

    *returnSize = numsSize;
    return returnArray;
}
# Array (배열)

1. 배열 회전 프로그램

- 기본 배열 회전 프로그램

  ```python
  void leftRotatebyOne(int arr[], int n){
      int temp = arr[0], i;
      for(i = 0; i < n-1; i++){
         arr[i] = arr[i+1];
      }
      arr[i] = temp;
  }
  ```

- 저글링 알고리즘

  정의 : 최대공약수 gcd를 이용해 집합을 나누어 여러 요소를 한꺼번에 이동시키는 것

- 역전 알고리즘
  정의 : 회전시키는 수에 대해 구간을 나누어 reverse로 구현하는 방법

1. 배열의 특정 최대 합 구하기
2. 특정 배열을 arr[i] = i로 재배열 하기

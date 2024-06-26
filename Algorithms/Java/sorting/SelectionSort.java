package sorting;
class SelectionSort {
    public static void selectionSort(final int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            int min = arr[i];
            int index = i;
            for (int j = i; j < arr.length; j++) {
                if (min > arr[j]) {
                    index = j;
                    min = arr[j];
                }
            }
            int temp = arr[i];
            arr[i] = min;
            arr[index] = temp;
        }
    }

    public static void main(final String[] args) {
        int[] arr = { 7, 45, 82, 5, 72, 6, 36, 8 };
        selectionSort(arr);

        for (int i : arr) {
            System.out.print(i + " ");
        }
    }
}

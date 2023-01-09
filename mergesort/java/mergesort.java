public class MergeSort {

    public static void mergeSort(int[] arr) {
        // base case: if the length of the array is 1 or less, it's already sorted
        if (arr.length <= 1) return;

        // split the array into two halves
        int half = arr.length / 2;
        int[] left = new int[half];
        int[] right = new int[arr.length - half];
        for (int i = 0; i < half; i++) {
            left[i] = arr[i];
        }
        for (int i = 0; i < right.length; i++) {
            right[i] = arr[half + i];
        }

        // recursively sort the two halves
        mergeSort(left);
        mergeSort(right);

        // merge the sorted halves
        merge(arr, left, right);
    }

    public static void merge(int[] arr, int[] left, int[] right) {
        // create an index for the original array
        int i = 0;
        
        // while both lists have elements
        int j = 0, k = 0;
        while (j < left.length && k < right.length) {
            // if the first element of the left list is less than or equal to
            // the first element of the right list, append the left element
            // and increment the left index. Otherwise, do the same with the
            // right element.
            if (left[j] <= right[k]) {
                arr[i] = left[j];
                j++;
            } else {
                arr[i] = right[k];
                k++;
            }
            i++;
        }

        // if one list is empty, append all the remaining elements from the other
        // list
        while (j < left.length) {
            arr[i] = left[j];
            i++;
            j++;
        }
        while (k < right.length) {
            arr[i] = right[k];
            i++;
            k++;
        }
    }

}

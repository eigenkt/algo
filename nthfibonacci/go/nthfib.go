package main

import "fmt"

func fibonacci(n int) int {
	if n == 0 {
		return 0
	} else if n == 1 {
		return 1
	} else {
		return fibonacci(n-1) + fibonacci(n-2)
	}
}

// This function uses a recursive approach to calculate the Nth fibonacci number. 
// The function calls itself with smaller values of n until it reaches the base case (n == 0 or n == 1), 
// at which point it returns the value of the fibonacci number. 

// For example, when calculating fibonacci(10), the function calls itself with fibonacci(9) and fibonacci(8). 
// These calls in turn call fibonacci(8) and fibonacci(7), and so on, until the base case is reached and the function starts returning values. 
// These returned values are then used to calculate the final value of fibonacci(10).

// Keep in mind that this implementation has a time complexity of O(2^n), which means that it can be very slow for larger values of n. 
// If you need to calculate large fibonacci numbers efficiently, you may want to consider using a different algorithm.

func main() {
	fmt.Println(fibonacci(10)) // prints 55
}

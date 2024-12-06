package main

import (
	"bufio"
	"fmt"
	"log"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	file, err := os.Open("day1.txt")
	if err != nil {
		log.Fatalf("cannot open file %v", err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	left := make([]float64, 0)
	right := make([]float64, 0)
	for scanner.Scan() {
		line := scanner.Text()
		numbers := strings.Fields(line)
		fmt.Println(numbers)
		num1, err := strconv.ParseFloat(numbers[0], 64)
		fmt.Println(num1)
		if err != nil {
			log.Fatalf("Could not parse to float64 %v", err)
		}
		num2, err := strconv.ParseFloat(numbers[1], 64)
		if err != nil {
			log.Fatalf("Could not parse to float64 %v", err)
		}
		left = append(left, num1)
		right = append(right, num2)
		sort.Float64s(left)
		sort.Float64s(right)
	}

	result := 0
	for i := 0; i < len(left); i++ {
		result += int(math.Abs(left[i] - right[i]))
	}
	fmt.Println(result)
}

package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
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
	left := make([]string, 0)
	counter := make(map[string]int)
	for scanner.Scan() {
		line := scanner.Text()
		numbers := strings.Fields(line)
		left = append(left, numbers[0])
		if _, exists := counter[numbers[1]]; !exists {
			counter[numbers[1]] = 1
		} else {
			counter[numbers[1]] += 1
		}
	}

	result := 0
	for i := 0; i < len(left); i++ {
		if _, exists := counter[left[i]]; exists {
			leftNum, err := strconv.ParseInt(left[i], 10, 64)
			if err != nil {
				log.Fatalf("Could not parse string to int %v", err)
			}
			result += int(leftNum) * counter[left[i]]
		}
	}
	fmt.Println(result)
}

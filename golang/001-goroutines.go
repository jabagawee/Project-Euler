package main

import "fmt"

import "./util"

func makeMultipleChannel(n int) (ch chan int) {
	ch = make(chan int)
	go func() {
		for i := n; ; i += n {
			ch <- i
		}
	}()
	return
}

/*
Operates on several assumptions for simplicity's sake that are
justified by the problem being solved (Project Euler 1).

First, we assume that 0 will never be emitted by the channel.
Luckily, our makeMultipleChannel function will nto do so.
Next, we assume that ch1 and ch2 never stop.
*/
func mergeOrderedIntChannels(ch1, ch2 chan int) (out chan int) {
	out = make(chan int)
	var v1, v2 int
	go func() {
		for {
			if v1 == 0 {
				v1 = <-ch1
			}
			if v2 == 0 {
				v2 = <-ch2
			}
			if v1 < v2 {
				out <- v1
				v1 = 0
			} else if v2 < v1 {
				out <- v2
				v2 = 0
			} else {
				out <- v1
				v1, v2 = 0, 0
			}
		}
	}()
	return
}

func main() {
	var ans int
	three, five := makeMultipleChannel(3), makeMultipleChannel(5)
	merged := mergeOrderedIntChannels(three, five)
	limited := util.LimitIntChannel(merged, 1000)
	for value := range limited {
		ans += value
	}
	fmt.Println(ans)
}

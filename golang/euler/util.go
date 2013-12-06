package euler

func FilterIntChannel(predicate func(int) bool, in chan int) (out chan int) {
	out = make(chan int)
	go func() {
		for {
			if v := <-in; predicate(v) {
				out <- v
			}
		}
	}()
	return
}

func CapIntChannel(in chan int, limit int) (out chan int) {
	out = make(chan int)
	go func() {
		for {
			v := <-in
			if v >= limit {
				close(out)
				break
			}
			out <- v
		}
	}()
	return
}

func Fibonaccis() (ch chan int) {
	ch = make(chan int)
	go func() {
		for i, j := 0, 1; ; i, j = i+j, i {
			ch <- i
		}
	}()
	return
}

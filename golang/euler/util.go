package euler

func FilterIntChannel(predicate func(int) bool, in chan int) chan int {
    out := make(chan int)
	go func() {
		for {
			if v := <-in; predicate(v) {
				out <- v
			}
		}
	}()
	return out
}

func CapIntChannel(in chan int, limit int) chan int {
    out := make(chan int)
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
	return out
}

func Fibonaccis() chan int {
    ch := make(chan int)
	go func() {
		for i, j := 0, 1; ; i, j = i+j, i {
			ch <- i
		}
	}()
	return ch
}

func Triangles() chan int {
    ch := make(chan int)
    go func() {
        n := 0
        for i := 1; ; i++ {
            n += i
            ch <- n
        }
    }()
    return ch
}

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

func LimitIntChannel(in chan int, limit int) (out chan int) {
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

func MakeCounter(start, incr int) (ch chan int) {
    ch = make(chan int)
    go func() {
        for i := start; ; i += incr {
            ch <- i
        }
    }()
    return
}

func MakeFibonacciChannel() (ch chan int) {
	ch = make(chan int)
	go func() {
		for i, j := 0, 1; ; i, j = i+j, i {
			ch <- i
		}
	}()
	return
}

func MakePrimeChannel() (out chan int) {
    out = make(chan int, 1)
    out <- 2

    primes := MakeCounter(3, 2)
    go func() {
        for {
            prime := <-primes
            out <- prime
            predicate := func (n int) bool {return n%prime != 0}
            primes = FilterIntChannel(predicate, primes)
        }
    }()
    return
}

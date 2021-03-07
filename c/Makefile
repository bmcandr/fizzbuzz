TARGET = fizzbuzz

$(TARGET): fizzbuzz.c
	gcc -o $@ $<

.PHONY: test
test: $(TARGET)
	./fizzbuzz

.PHONY: clean
clean:
	rm $(TARGET)

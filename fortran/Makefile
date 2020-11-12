MODS = simple_fizzbuzz_mod.o

fizzbuzz : main.f90 $(MODS)
	gfortran $? -o $@

$(MODS) : $(wildcard *_mod.f90)
	gfortran -c $?

.PHONY : clean

clean :
	rm fizzbuzz *.mod *.o

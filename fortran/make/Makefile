TARGET = ../fizzbuzz

F90 = gfortran

SRCDIR = ../src
DRVDIR = ../driver
BUILDDIR = ../obj

VPATH = $(DRVDIR):$(SRCDIR):$(BUILDDIR)

FCFLAGS += -J $(BUILDDIR)
INCFLAGS += -I $(BUILDDIR)

MODS = utils.o simple_fizzbuzz_mod.o
MODOBJS = $(addprefix $(BUILDDIR)/,$(MODS))

$(TARGET) : main.f90 $(MODOBJS)
	$(F90) $? -o $@ $(INCFLAGS)

$(BUILDDIR)/%.o:%.f90 | $(BUILDDIR)
	$(F90) -c $< -o $@ $(FCFLAGS)

$(BUILDDIR):
	@echo "Folder $< does not exist. Creating now..."
	mkdir -p $@

.PHONY : clean

clean :
	rm -r $(TARGET) $(BUILDDIR)

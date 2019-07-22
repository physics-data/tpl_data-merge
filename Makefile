
# TODO: how to find data/*.in.h5 ?
INPUT  := 
# replace: %.in.h5 -> %.out.h5
OUTPUT := $(patsubst %.in.h5, %.out.h5, $(INPUT))

# all output files are outputs
all: $(OUTPUT)

%.out.h5: %.in.h5
	# TODO: how to invoke the python script ?

clean:
	# TODO: how to remove all outputs?

.DELETE_ON_ERROR:

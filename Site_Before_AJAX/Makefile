parts := $(shell ls /tmp/*.part)
res := $(parts:.part=.summary)
go: $(res)
%.summary: %.part
	python3 ./step2.py $< $@

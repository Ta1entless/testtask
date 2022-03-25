task:
	gcc -g -o task task.c

clean:
	rm task

install:
	mkdir -p $(DESTDIR)/usr/bin
	install -m 0755 task $(DESTDIR)/usr/bin/task

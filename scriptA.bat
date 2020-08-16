python ./step0.py $1 $2
if [ -f /tmp/flag ]
then
	python ./step1.py $1
	python ./split.py
	make -j4
	python ./resume.py
	python ./step3.py $1
	rm /tmp/flag
else
	echo "This Database already Exist !!"
	rm /tmp/flag
fi

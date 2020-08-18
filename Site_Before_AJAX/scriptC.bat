python ./step0.py $1 $2
if [ ! -f /tmp/flag ]
then
	python ./snpstep1.py $1
	python ./scriptxml.py $1

else
	echo "This Database already Exist !!"
	rm /tmp/flag
fi

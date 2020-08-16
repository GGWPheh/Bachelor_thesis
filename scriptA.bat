python ./step0.py $1
if [ -f flag ]
then
	python ./step1.py $1
	python ./split.py
	make -j4
	python ./resume.py
	python ./step3.py $1
else
	echo "This Database already Exist !!"
fi

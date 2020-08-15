python ./step0.py $1
python ./step1.py $1
python ./split.py
make -j4
python ./resume.py
python ./step3.py $1

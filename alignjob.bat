python ./scriptali.py $1
sh ./alijob $1 $2
python ./affichali.py $2
cat /tmp/$2_res.vcf

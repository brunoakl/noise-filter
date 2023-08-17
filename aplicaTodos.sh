varia_ps='5 105'
for ps in $varia_ps
do
	for f in *.jpg
	do 
	 echo $f $ps
	 python ruidoSuaveBordas.py -i $f -s 'gauss' -ps $ps -ig nao
	done
done



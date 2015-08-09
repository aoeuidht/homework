f='file.txt'
c=`head -n 1 $f| wc -w`
c=$[$c+1]
i="1"
while [ $i -lt $c ]
do
    awk "{print \$$i}" $f | xargs
    i=$[$i+1]
done
      

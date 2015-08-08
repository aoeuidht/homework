cat words.txt | tr -s " " "\012" | sort | uniq -c | sort -rnt1 | awk '{print $2 " " $1}'

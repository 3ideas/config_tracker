FILES="/Users/bt/localdev/CONFIG_TABLE_EXTRACTS/exports/server2/20211108/*"
for FILE in $FILES ; 
do 
        python csv_header_restore.py -n ../headers.txt -f $FILE ; 
done


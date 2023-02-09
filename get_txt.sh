#!/bin/bash
#echo "Key combination pressed!"


 read_line(){
	n=1
	while read line; do
	# reading each line
	echo "Line No. $n : $line"
	#echo "this line"
	tts --text "$line" --out_path speech.wav

	n=$((n+1))
	done < $filename
}


read_file() {
 
	text_file=$(<./text.txt)
	printf "%s" "$text_file"
	tts --text "$text_file" --out_path ~/tts/speech.wav	
}


#MAIN
# xsel -ob > ./text.txt

# filename='text.txt'

read_file 

#"$(xsel -ob)"

mpv ~/tts/speech.wav








#!/bin/bash
#By Nicolas Le Guerroué
function makeChart {

	#$1 : Directory to count 
	#$2 : Output filename
	#$3 : Title x axis
	#$4 : Title y axis 
	#$5 : Title

	echo "" > data.txt
	echo "" > graph.gnuplot
	for item in "$1"/*
	do
		name=`echo $item | cut -d'/' -f2 | cut -d'.' -f1`
		echo $name `wc -l $item | cut -d' ' -f1` >> data.txt
	done

	echo "set terminal png" >> graph.gnuplot
	echo "set output '"$2"'" >> graph.gnuplot
	echo "set title '"$5"'" >> graph.gnuplot
	echo "set xlabel '"$3"'" >> graph.gnuplot
	echo "set ylabel '"$4"'" >> graph.gnuplot
	echo "set grid" >> graph.gnuplot
	echo "" >> graph.gnuplot
	echo "set style data histogram" >> graph.gnuplot
	echo "set style histogram cluster gap 1" >> graph.gnuplot
	echo "set style fill solid border -1" >> graph.gnuplot
	echo "" >> graph.gnuplot
	echo "set xtics rotate by 60 right  " >> graph.gnuplot
	echo "plot 'data.txt' using 2:xtic(1)" >> graph.gnuplot

	gnuplot graph.gnuplot

}

function makeRecursiveChart {

	#$1 : Directory to count 
	#$2 : Output filename
	#$3 : Title x axis
	#$4 : Title y axis 
	#$5 : Title

	echo "" > data.txt
	echo "" > graph.gnuplot

	for dir in $part_dir/*
	do
		for file in $dir/*
		do
	
		name=`echo $file | cut -d'/' -f3`
		echo $name `wc -l $file | cut -d' ' -f1` >> data.txt

		done
	done

	echo "set terminal png" >> graph.gnuplot
	echo "set output '"$2"'" >> graph.gnuplot
	echo "set title '"$5"'" >> graph.gnuplot
	echo "set xlabel '"$3"'" >> graph.gnuplot
	echo "set ylabel '"$4"'" >> graph.gnuplot
	echo "set grid" >> graph.gnuplot
	echo "" >> graph.gnuplot
	echo "set style data histogram" >> graph.gnuplot
	echo "set style histogram cluster gap 1" >> graph.gnuplot
	echo "set style fill solid border -1" >> graph.gnuplot
	echo "" >> graph.gnuplot
	echo "set xtics rotate by 60 right  " >> graph.gnuplot
	echo "plot 'data.txt' using 2:xtic(1)" >> graph.gnuplot

	gnuplot graph.gnuplot

}
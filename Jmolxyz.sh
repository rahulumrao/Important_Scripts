#----------------------------------------------------------------------------
#!/bin/bash
# THIS IS A SCRIPT FOR Jmol PACKAGE TO OPEN THE GAUSSIAN OUTPUT FILE
# AND WRITE ALL THE CARTESIAN COORDINATES IN A 'traj.xyz
# Written by : Rahul Verma (vrahul@iitk.ac.in) {JUNE 15 , 2019} 
#
# Default Gaussian output file  : input.log
# Uncomment 'read' line and comment 'filename' line to manually provide file
#----------------------------------------------------------------------------
export jmol_path=/home/vrahul/Softwares/jmol-14.29.3/Jmol.jar	# change this according to the Jmol path in your computer
#!#echo 'ENTER GAUSSIAN OUTPUT FILE NAME WITH EXTENSION'
#!#read filename
#!#echo $filename
filename=input.log
java -jar $jmol_path -J "load TRAJECTORY '$filename'; write "traj.xyz"; exitjmol"
#echo "load TRAJECTORY '$filename'" > jmol.script
#echo "write traj.xyz"             >> jmol.script
#echo "exitjmol"                   >> jmol.script
#java -jar $jmol_path -J jmol.script


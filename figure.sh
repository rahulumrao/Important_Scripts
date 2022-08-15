#----------------------------------------------------------------------------------
#!/bin/bash
# Enhance the resolution of image file generated from VMD package
# 
# Prerequisite ; 
# VMD         : https://www.ks.uiuc.edu/Development/Download/download.cgi?PackageName=VMD
# ImageMagick : https://imagemagick.org/script/mogrify.php
# 
#----------------------------------------------------------------------------------
# Replace the resolution numeric value to increase the Resolution in DAT file created by VMD
#sed -i '11s/.*/Resolution 3200 1748/' vmdscene.dat
sed -i '11s/.*/Resolution  6400 3496/' vmdscene.dat
#Run VMD command to convert DAT file to an TGA format image file
/usr/local/lib/vmd/tachyon_LINUXAMD64 -aasamples 12 vmdscene.dat -format TARGA -o vmdscene.tga
#convert TGA image to JPEG format from imagemagick command line
#mogrify -format jpeg vmdscene.tga
mogrify -format jpeg vmdscene.tga
#convert TGA image to eps format from imagemagick command line
mogrify -format pdf vmdscene.tga

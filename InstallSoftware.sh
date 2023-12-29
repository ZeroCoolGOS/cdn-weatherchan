softwareFolder="$PWD"

mkdir Software
cd software

# --------------------------------------------------
# Python Update
# --------------------------------------------------
# https://raspberrytips.com/install-latest-python-raspberry-pi/
PythonVersion="3.9.15"

wget https://www.python.org/ftp/python/3.9.15/Python-3.9.15.tgz

tar -zxvf Python-3.9.15.tgz

cd Python-3.9.15

./configure --enable-optimizations

make altinstall

cd /usr/bin
rm python
sudo ln -s /usr/local/bin/python3.9 python
python --version
# --------------------------------------------------

# --------------------------------------------------
# PIP Update
# --------------------------------------------------
pip3 install --upgrade pip
pip3 --version
# --------------------------------------------------

# --------------------------------------------------
# PIP Install PreReqs
# --------------------------------------------------
pip3 install -r requirements.txt
# --------------------------------------------------


# --------------------------------------------------
# Font Download
# --------------------------------------------------
# https://www.dafont.com/vcr-osd-mono.font
wget https://dl.dafont.com/dl/?f=vcr_osd_mono

# https://blogfonts.com/7-segment-normal.font
wget https://blogfonts.com/download/0-53946-1/7-Segment%20Normal.file

# --------------------------------------------------

# --------------------------------------------------
# Font Install
# --------------------------------------------------
# https://raspberrytips.com/install-fonts-raspberry-pi/

mkdir ~/.fonts/
# cd ~/Downloads/source-sans-pro/
cp *.otf ~/.fonts/
cp *.ttf ~/.fonts/
fc-cache -v -f

# --------------------------------------------------


cd ..
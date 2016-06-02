# Parallel Corpora
<p>This repository stores all necessary data and Python-scripts for creating the Parallel Corpus.</p>
<p>Contact information: Naumov Alexander, headshoter13@gmail.com</p>

You can find the results of allignment in folder *Corpora*
<br>Source zip-files in folder *subs*
<br> Extracted srt-files in folder *Extracted_Data*
<br>
###How does it work?
In order to create the corpus you have to perform some actions:
<br> To install some modules and libraries for *Python 2.7* :urllib2, mechanize
<br> For *Python 3*: zipfile
<br>
#### 1) To launch the Download_Script.py with *Python 2.7*
This script collects the links for downloading the subs and downloads it in zips to the folder *sub*.
<br>In order to use this script you have to register your profile on the *OpenSubtitles.org* and put your data in a proper place in *def openBrow* or use my profile that's already put in.
<br> After you have your account you have to set the numbers in def subtitles. In line *for film in range(x, n)* You have to put the numbers you want. And the script will download the subs from x to n. For example: for film in range(1,101) <br>
In this case, you will have 100 different subtitles

#### 2) To launch the Extraction_SRT.py
The script extracts all the *srt*-subs from zips from folder *subs* to folder *Extracted_Data* and write down the statistics about the films and languages to file *MetaInfo.csv*

#### 3)To launch the Allignment.py
This big script perform the allignment of *srt*-files from folder *Extracted_Data* and create the additional file to new folder *Corpora*. In result, it creates 1 *xml*-file with all the languages for each film




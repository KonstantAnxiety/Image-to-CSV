# Image-to-CSV
A python script that converts a b/w image into a csv of pixel coordinates

```
usage: script.py [-h] [--fin FIN] [--fout FOUT] [--plot PLOT]
                 [--noise NOISE] [--haze HAZE] [--shrink SHRINK]

Convert b/w image to csv

optional arguments:
  -h, --help                  show this help message and exit
  --fin FIN, -i FIN           input image filename
  --fout FOUT, -o FOUT        output csv filename
  --plot PLOT, -p PLOT        plot the result [1/0]
  --noise NOISE, -n NOISE     noise amount (float)
  --haze HAZE, -z HAZE        amount of noize all around the image (int)
  --shrink SHRINK, -s SHRINK  shrinkage coefficient (float)  
```

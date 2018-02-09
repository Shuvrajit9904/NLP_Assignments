In Order to run the file please use 'python' as prefix and use the .py extension for the code. To use liblinar-1.91, please move all the required files(ner.py, test.txt.vector, train.txt.vector, train.txt, test.txt, locs.txt ) to the directory where you have the executable train and predict file. 
To run eval.py, the necessary files are gold.txt, prediction.txt

Run the following commands in sequence for the 1st part of the problem:
python ner.py train.txt test.txt locs.txt WORD WORDCON POS POSCON ABBR CAP LOCATION
./train -s 0 -e 0.0001 train.txt.vector classifier
./predict test.txt.vector classifier predictions.txt > accuracy.txt

For the 2nd part:
python eval.py prediction.txt gold.txt

I have tested the program in CADE Lab (1-14)

Thanks,
Shuvrajit
+13852422026
#This is a tool used to find the hash of the given word and can detect what hashing algorithm is used.
#To use this tool follow the below steps:

Step 1:
#Clone this in to your local repository
git clone https://github.com/Jishnu1008/HashFinder.git

Step 2:
#Move to the HashFinder Directory
cd HashFinder
#Install the requirements.txt using the given below command
pip install -r requirements.txt

Step 3:
#Now run the command to find the word and the hashing algorithm used in it by giving the "hash" and the "file" that is used to crack the word.
python hasher.py -i <hash_value> <path_of_the_file>


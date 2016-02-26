## 1. Implementation of BloomFilter

The implementation of the project entirely was done in python. I used jenkins hash implementation as base hash function.
In addition, I wrote another wrapper class for HashFunction which uses jenkins hash function as base and it takes 2 additional random parameters to differentiate each instance of the HashFunction class. 
I designed and implemented another BloomFilter class which takes M and K values in its constructor and use that wrapped HashFunction class to generate different K number of hash functions in the class.
M is used to set the size of the Bit Vector. In its constructor, all bits in the bit vector initialized to False at first.

BloomFilter class has 2 methods insert and check. Insert method takes a value as a parameter and hash the value through all K number of different hash functions. Set true to all indexes after that. 
However, check method basically hash the value again through hash functions and check if all set to True. If any of them set to False, it will return false otherwise True.

I implemented another class Experiment which basically takes B , N , M ,K values.

B is for number of iterations
N is for number of items to be added
M is for Bit vector size
K is for number of hash functions.

In this sense, by setting these parameters in Experiment class, the class itself will do the rest as following
- The experiment class sets constructor fields to its private properties.
- It has make_experiment method to perform experiment with given parameters.
- In make_experiment method, it will loop through B times , sum each result for the experiment with different hash functions and in the end, it will divide the sum by B again.

Jenkin's hash implementation is taken from http://stackoverflow.com/questions/3279615/python-implementation-of-jenkins-hash

## 2. Experiments.
##### 2.1 Number of Vector size VS False Positive Probability with constant number of HashFunctions
![alt tag](https://raw.githubusercontent.com/erenyagdiran/bloomfilter/master/images/90123647.png)
![alt tag](https://raw.githubusercontent.com/erenyagdiran/bloomfilter/master/images/exp1.png)

##### 2.2 Number of Hash Functions VS False Positive Probability with constant number of Vector Size
![alt tag](https://raw.githubusercontent.com/erenyagdiran/bloomfilter/master/images/20861426.png)
![alt tag](https://raw.githubusercontent.com/erenyagdiran/bloomfilter/master/images/exp2.png)

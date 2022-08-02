# Speed-Typing-Test
A python based typing speed test program using the libraries pandas, numpy, time and matplotlib.

A typing test interface which will take the timed inputs form the user according to his choice of precision and generate a final report for his performance among all other candidates through graph and percentile.
It will also maintain files for 3 fastest typing instances in 3 separate files.
Object Oriented Programming is used in implementing the project.
Two spreadsheets are used to store data in arranged fashion.

Libraries used:
1. Pandas: For handling data from the .csv files as Data Frames and easy conversion of data into dictionaries.
2. NumPy: For calculating average values of accuracies and typing speeds from a large database and by converting certain fields to array for easy manipulation i.e. sorting etc.
3. Matplotlib: For visualizing complex and bulky data in the form of plots for easy understanding.
4. csv: For appending the data in csv files after calculations.
5. Random: For getting random values as and when needed.
6. String: For operating on strings while generating IDs.
7. Time: For getting the timed inputs for calculation of Typing Speeds.

Following is the list of functions that I have used in our program along with their functionality:
1. Conversion Functions:  In our Project in order to have full freedom of using whichever data type one wish to operate with few conversion functions are used that uses Pandas and CSV libraries to convert dictionaries to data frames and vice versa.
2. Calculation Function: We have used multiple small sentences instead of single large paragraph in order to have a balanced as well as precise result. To accommodate a single final result for a candidate we have to perform certain calculations to find average values of a formed data set using NumPy.
3. Rank Maintaining Function: In order to have details about top three fastest contenders in our database we have defined a function to keep track of the three contenders as Class Objects in three separate text files.
4. Percentile Calculation: From the database stored as .csv file we have calculated the final performance of the current contender using NumPy library and sorting the data.
5. Data Sets: We have used two .csv spreadsheets. First one named as “individual.csv” holds the data of the current candidate for the generation of final result. Second file is named “database.csv”, which holds the data of entire contenders who have taken the test so far.
6. Text Files: We have maintained 3 text files named “first.txt”, “second.txt” and “third.txt” to store the details of the top performers of our Typing test.
7. Plot Generation: A function has been included in the file for generating the graph of all the performances of a single contender in one round to show the rise and fall in the Typing speed of the performer.
8. Key generator: A function has been used to generate random strings serving as the unique id for any contender for his/her unique identification.

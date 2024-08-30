Input Handling:

The script reads each line from sys.stdin.
It splits the line into parts and checks if the format is correct (i.e., at least 7 parts).
Data Processing:

It extracts the status code and file size.
The file size is accumulated to calculate the total size.
The status code count is updated for each valid status code.
Statistics Printing:

After every 10 lines, the script prints the total file size and the count of each status code that has appeared.
If a keyboard interruption (CTRL + C) occurs, it prints the statistics before exiting.
Final Output:

After processing all input lines, it prints the final statistics.

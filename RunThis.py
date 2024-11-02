import datetime;

date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S");
finalOutputString = "Test Successfully ran at:" + date

#open a text file
with open("testResults.txt", "w") as file:
    file.write(finalOutputString)

print("String has been written to output.txt")

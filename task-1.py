import pandas, os
from sklearn.linear_model import LinearRegression as lr

# download "tput" command to change text color in terminal
os.system("yum install /usr/bin/tput -y")

# read dataset file
ds = pandas.read_csv("salary_data.csv")
x = ds["YearsExperience"].values.reshape(30,1)
y = ds["Salary"]

# train model
model = lr()
model.fit(x,y)

print("_________________________________________LinearRegression Model in Docker Container________________________________________\n")

while True:
    # predict salary
    year = float(input("Enter year of experience :- "))
    predict = model.predict([[year]])
    
    # change color of text in terminal
    os.system("tput setaf 3")
    print("\nYou are having {} years of experience".format(year))
    
    # change color of text in terminal
    os.system("tput setaf 2")
    print("so your salary will be : {}".format(predict[0]))
    
    # change color of text in terminal
    os.system("tput setaf 1")
    final = input("\nPress 'c' for Continue \nor 'e' for exit :- ")
    
    if final == "e":
        os.system("tput setaf 7")
        exit()
        
    elif final == "c":
        os.system("tput setaf 2")
        print("Continue....")
        os.system("tput setaf 7")

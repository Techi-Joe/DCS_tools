'''
Predict MILs for a DCS F-5E Tiger II bombing run using linear regression based on input conditions.

The function prompts the user to select an ordnance type ('mk82' or 'snake').
It then extracts data points for the selected ordnance type from pre-defined dictionaries.
Next, it trains a linear regression model using the extracted data points.
After obtaining user inputs for attack angle, target altitude, aircraft altitude, and attack KIAS,
it predicts MILs using the trained model and displays the result.
Additionally, it includes an option to visualize the linear regression plane in a 3D plot.

The mk82_mils and snake_mils dictionaries contain information about the MIL settings for deploying
MK-82 or Snake Eye bombs at various angles, altitudes, and speeds (in knots indicated airspeed,
or KIAS). The value "-1" indicates that a condition is not maintainable, meaning the bombs 
cannot be accurately deployed under those specific conditions.

Created by Techi-Joe
'''

import os
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#----------------------------------------------------------------
# Dictionaries for MILs:

# format - angle:[{altitude:[{kias:mils}]}]

mk82_mils = {
    10:[{700:[{520:45}]}],

    15:[{1000:[{400:87},{450:57},{475:52},{500:42},{550:32}]},
        {1500:[{400:113},{450:92},{475:77},{500:65},{550:51}]},
        {2000:[{400:140},{450:107},{475:98},{500:83},{550:69}]},
        {3000:[{400:200},{450:146},{475:134},{500:122},{550:101}]}],

    20:[{1000:[{400:62},{450:44},{475:32},{500:30},{550:24}]},
        {1500:[{400:85},{450:61},{475:52},{500:48},{530:45},{550:38}]},
        {2000:[{400:112},{450:87},{475:75},{500:68},{550:54}]},
        {2500:[{530:68}]},
        {3000:[{400:154},{450:118},{475:105},{500:92},{550:82}]},
        {3500:[{555:92}]},
        {4000:[{400:185},{450:145},{475:133},{500:121},{550:102}]}],
    
    25:[{3000:[{560:60},{590:55}]}],

    30:[{1500:[{400:-1},{450:38},{475:30},{500:25},{550:18}]},
        {2000:[{400:-1},{450:54},{460:45},{475:43},{500:36},{550:30}]},
        {2500:[{575:35}]},
        {3000:[{400:-1},{450:78},{475:65},{500:62},{520:60},{550:51},{570:45}]},
        {4000:[{400:-1},{450:100},{475:87},{500:79},{550:65}]},
        {5000:[{400:-1},{450:118},{475:108},{500:97},{550:78}]}],

    35:[{3000:[{560:40}]},
        {3200:[{580:40}]}],
    
    40:[{3000:[{470:70}]},
        {3500:[{500:50}]},
        {4000:[{540:45}]},
        {6000:[{525:70}]}],
    
    45:[{3000:[{400:-1},{450:-1},{475:-1},{500:23},{550:19}]},
        {4000:[{400:-1},{450:-1},{475:-1},{500:35},{550:28}]},
        {5000:[{400:-1},{450:-1},{475:-1},{500:49},{550:38}]},
        {9000:[{520:90}]}],
    
    50:[{5000:[{500:45}]}],
    
    60:[{4000:[{400:-1},{450:-1},{475:-1},{500:5},{550:2}]},
        {5000:[{400:-1},{450:-1},{475:-1},{500:10},{550:7}]},
        {6000:[{400:-1},{450:-1},{475:-1},{500:18},{550:14}]},
        {7000:[{540:25}]},
        {10000:[{500:50}]}]
}

snake_mils = {
    0:[{100:[{530:40}]},
       {200:[{515:60},{570:55},{600:55},{520:65}]},
       {300:[{610:80}]},
       {350:[{540:105}]}],

    5:[{300:[{555:50},{450:80},{545:45}]},
       {350:[{560:45}]},
       {500:[{560:85},{540:95}]},
       {700:[{530:155}]}],

    10:[{500:[{560:50}]},
        {800:[{610:90}]},
        {900:[{560:125}]}],

    15:[{1000:[{550:124}]},
        {1200:[{570:120}]}],

    20:[{1000:[{600:60}]}]
}
#----------------------------------------------------------------
# constants:

ords = {"mk82", "snake"}

data_points = []

a,b,c,d = 0,0,0,0

X,y = np.array([]), np.array([])

#----------------------------------------------------------------
# functions:

# Extract data points from the dictionary
def extract_from_dict(dictionary):
    for angle, altitudes in dictionary.items():
        for altitude_dict in altitudes:
            for altitude, kias_dicts in altitude_dict.items():
                for kias_dict in kias_dicts:
                    for kias, mils in kias_dict.items():
                        data_points.append((angle, altitude, kias, mils))


# Function to predict MILs
def predict_mils(angle, altitude, kias):
    return round(a * angle + b * altitude + c * kias + d)

# Function to plot regression
def plot_regression():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Scatter plot of data points
    ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y, cmap='viridis', marker='o')

    # Create a grid for plotting the regression plane
    angle_range = np.linspace(X[:, 0].min(), X[:, 0].max(), 20)
    altitude_range = np.linspace(X[:, 1].min(), X[:, 1].max(), 20)
    angle_grid, altitude_grid = np.meshgrid(angle_range, altitude_range)
    kias_grid = a * angle_grid + b * altitude_grid + d

    ax.plot_surface(angle_grid, altitude_grid, kias_grid, color='red', alpha=0.5)

    ax.set_xlabel('Angle')
    ax.set_ylabel('Altitude')
    ax.set_zlabel('KIAS')
    ax.set_title('Linear Regression Plane')

    plt.show()

# handle the float inputs from the user
def float_input(q_string):
    usr_in = float(0)
    while True:
        usr_in = -1.1273894
        try:
            usr_in = float(input(q_string))
        except ValueError:
            print("Please enter valid numerical value")
        if usr_in == abs(usr_in):
            break
        else:
            print("Number cannot be negative")
    return usr_in


#----------------------------------------------------------------
# main code:

# ask user for ordanance type:
while True:
    ord_type = input("ordanance type (mk82 or snake): ")
    if ord_type not in ords:
        print ("Invalid ordanance type, try again.")
    else:
        break
if ord_type == "mk82":
    ord_dict = mk82_mils
elif ord_type == "snake":
    ord_dict = snake_mils

# extract the appropriate dictionary
extract_from_dict(ord_dict)

# Split the data into inputs (X) and outputs (y)
X = np.array([[point[0], point[1], point[2]] for point in data_points])
y = np.array([point[3] for point in data_points])

# Create and fit the model
model = LinearRegression()
model.fit(X, y)

# Coefficients
a, b, c = model.coef_
d = model.intercept_

# User input for prediction
in_angle = float_input("attack angle (degrees): ")
tgt_altitude = float_input("target's altitude (ft ASL): ")
true_altitude = float_input("your altitude (ft ASL): ")
in_kias = float_input("your attack KIAS: ")

in_altitude = true_altitude - tgt_altitude

# user input readback
os.system('cls')
print("ordanance : " + str(ord_type) + " | " + "speed : " + str(in_kias) + " KIAS"
      + " | " + "release altitude : " + str(int(true_altitude)) + " ft" + " | "
      + "angle : " + str(in_angle) + "°")

# output predicted MILs
predicted_mils = predict_mils(in_angle, in_altitude, in_kias)
if 0 < predicted_mils < 200:
    print(f"Predicted MILs: {predicted_mils}")
else:
    print(f"Conditions invalid. (MILs returned {predicted_mils})")

# exit
input("\npress enter to exit...")
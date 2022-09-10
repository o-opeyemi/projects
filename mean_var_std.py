
from math import sqrt
from statistics import variance, pvariance

# Calculate
def calculate(matrix_list):
    if len(matrix_list) < 9:
        raise ValueError
    else:
        output = {}

        # Serializing the matrix into list
        axis2 = []
        axis1 = []
        for i in range((len(matrix_list) + 1) // 3):
            temp_axis1 = []
            temp_axis1.append(matrix_list[i])
            temp_axis1.append(matrix_list[i+3])
            temp_axis1.append(matrix_list[i+6])
            axis1.append(temp_axis1)
            axis2.append(matrix_list[i*3:(i*3)+3])

        # Mean    
        mean_axis1 = [ Mean(i) for i in axis1]
        mean_axis2 = [ Mean(i) for i in axis2]
        mean_flattened = Mean(matrix_list)
        mean = [mean_axis1, mean_axis2, mean_flattened]
        output["mean"] = mean

        # Variance 
        var_axis1 = [Var(i) for i in axis1]
        var_axis2 = [Var(i) for i in axis2]
        var_flattened = Std(matrix_list)
        var = [var_axis1, var_axis2, var_flattened]
        output["variance"] = var

        # Standard Deviation 
        std_axis1 = [Std(i) for i in axis1]
        std_axis2 = [Std(i) for i in axis2]
        std_flattened = Std(matrix_list)
        std = [std_axis1, std_axis2, std_flattened]
        output["standard deviation"] = std

        # Minimum 
        min_axis1 = [Min(i) for i in axis1]
        min_axis2 = [Min(i) for i in axis2]
        min_flattened = Std(matrix_list)
        min = [min_axis1, min_axis2, min_flattened]
        output["min"] = min

        # Maximum 
        max_axis1 = [Max(i) for i in axis1]
        max_axis2 = [Max(i) for i in axis2]
        max_flattened = Std(matrix_list)
        max = [max_axis1, max_axis2, max_flattened]
        output["max"] = max

        # Summation 
        sum_axis1 = [Sum(i) for i in axis1]
        sum_axis2 = [Sum(i) for i in axis2]
        sum_flattened = Std(matrix_list)
        sum = [sum_axis1, sum_axis2, sum_flattened]
        output["sum"] = sum
        
        print(output)

# Helpers function
def Mean(data_list):
    mean = sum(data_list) / len(data_list)
    return mean

def Var(data_list):
    var = pvariance(data_list, Mean(data_list))
    return var

def Std(data_list):
    std = sqrt(pvariance(data_list, Mean(data_list)))
    return std

def Min(data_list):
    minimum = min(data_list)
    return minimum

def Max(data_list):
    maximum = max(data_list)
    return maximum
    
def Sum(data_list):
    summation = sum(data_list)
    return summation
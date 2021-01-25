import csv
import json
from itertools import zip_longest

name = ["name"]
bmi_value = ["BMI"]
bmi_category = ["Category"]
health_risk = ["Health risk"]
with open('data_file.json', 'r') as f:
    distros_dict = json.load(f)


def cal_bmi(mass, height):
    height_in_m = height / 100
    bmi_value_data = mass / (height_in_m ** 2)
    return bmi_value_data


def patient_data():
    for distro in distros_dict:
        value = cal_bmi(distro['WeightKg'], distro['HeightCm'])

        if value <= 18.4:
            name.append(distro['Name'])
            bmi_value.append(value)
            bmi_category.append("Under weight")
            health_risk.append("Malnutrition risk")
        elif 18.5 <= value <= 24.9:
            name.append(distro['Name'])
            bmi_value.append(value)
            bmi_category.append("Normal weight")
            health_risk.append("Low risk")
        elif 25.0 <= value <= 29.9:
            name.append(distro['Name'])
            bmi_value.append(value)
            bmi_category.append("Over weight")
            health_risk.append("Enhanced risk")
        elif 30.0 <= value <= 34.9:
            name.append(distro['Name'])
            bmi_value.append(value)
            bmi_category.append("Moderately obese")
            health_risk.append("Medium risk")
        elif 35.0 <= value <= 39.9:
            name.append(distro['Name'])
            bmi_value.append(value)
            bmi_category.append("Severely obese")
            health_risk.append("High risk")
        else:
            name.append(distro['Name'])
            bmi_value.append(value)
            bmi_category.append("Very severely obese")
            health_risk.append("Very high risk")
            
    csvrows = [name, bmi_value, bmi_category, health_risk]
    export_data1 = zip_longest(*csvrows, fillvalue='')
    with open('/home/rohit/Documents/patient_status.csv', 'w', encoding="utf8", newline='') as f:
        fwriter = csv.writer(f)
        fwriter.writerows(export_data1)


if __name__ == "__main__":
    patient_data()
    print(bmi_category.count("Over weight"))

import pandas as pd

my_data = {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
            "John, lanker"
        ],
        "Age": [22, 35, 58, 45],
        "Sex": ["male", "male", "female", "other"],
    }

val = pd.DataFrame(my_data)
val1 = pd.Series(my_data)
pd.Series(["India", "UK", "US", "Italy", "France", "China"], name="Countries")
val.to_excel("test1.xlsx", sheet_name="Test")

a = val[val["Age"]>40]
print(val.loc[val["Age"] > 40, "Name"])

@pytest.mark.parametrize("name", "password", [("n", "234323"), ("b", "4rer3434")])
def my_func():

#val = pd.Series
#csvFile = pd.read_csv("C:\\Users\\rawat\\Downloads\\annual-enterprise-survey-2021-financial-year-provisional-csv.csv")
#print(csvFile.values)

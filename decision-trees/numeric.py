import pandas as pd

MONTHS ={"Jan": 0, "Feb": 1, "Mar": 2, "Apr": 3, "May": 4, "Jun": 5, "Jul": 6, "Aug": 7, "Sep": 8, "Oct": 9, "Nov": 10, "Dec": 11}
WEEKDAYS = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}
VEHICLE_PRICE_BINS = {"less than 20000": 10_000, "20000 to 29000": 25000, "30000 to 39000": 35000, "40000 to 59000": 50000, "60000 to 69000": 65000, "more than 69000": 100000}
DAYS_POLICY_BINS = {"none": 0, "1 to 7": 3.5, "8 to 15": 11.5, "15 to 30": 22.5, "more than 30": 35}
PAST_NUMBER_BINS = {"none": 0, "1": 1, "2 to 4": 3, "more than 4": 5, 1: 1}
AGE_OF_VEHICLE_BINS = {"new": 0, "2 years": 2, "3 years": 3, "4 years": 4, "5 years": 5, "6 years": 6, "7 years": 7, "more than 7": 10}
AGE_OF_POLICY_HOLDER_BINS = {"16 to 17": 16.5, "18 to 20": 10, "21 to 25": 23, "26 to 30": 28, "31 to 35": 33, "36 to 40": 38, "41 to 50": 45.5, "51 to 65": 58, "over 65": 70}
NUMBER_OF_SUPPLIER_BINS = {"none": 0, "1 to 2": 1.5, "3 to 5": 4, "more than 5": 6}
ADDRESS_CHANGE_BINS = {"no change": 0, "under 6 months": 0.5, "1 year": 1, "2 to 3 years": 2.5, "4 to 8 years": 6}
NUMBER_OF_CARS_BINS = {"1 vehicle": 1, "2 vehicles": 2, "3 to 4": 3.5, "5 to 8": 6.5, "more than 8": 10}
NUMBER_OF_SUPPLIMENTS = {'none':0,'1 to 2':1,'3 to 5':3,'more than 5':6}


def get_numeric_df(original_fraud_df: pd.DataFrame) -> pd.DataFrame:
    numeric_fraud_df = original_fraud_df.copy()
    numeric_fraud_df.DayOfWeekClaimed = numeric_fraud_df.DayOfWeekClaimed.map(WEEKDAYS)
    numeric_fraud_df.DayOfWeek = numeric_fraud_df.DayOfWeek.map(WEEKDAYS)
    numeric_fraud_df.Month = numeric_fraud_df.Month.map(MONTHS)
    numeric_fraud_df.MonthClaimed = numeric_fraud_df.MonthClaimed.map(MONTHS)
    numeric_fraud_df.Sex = numeric_fraud_df.Sex.apply(lambda sex: 1 if sex == "Male" else 0)
    numeric_fraud_df.AccidentArea = numeric_fraud_df.Sex.apply(lambda area: 1 if area == "Urban" else 0)
    numeric_fraud_df.Fault = numeric_fraud_df.Fault.apply(lambda fault: 1 if fault == "Policy Holder" else 0)
    numeric_fraud_df.VehiclePrice = numeric_fraud_df.VehiclePrice.map(VEHICLE_PRICE_BINS)
    numeric_fraud_df.Days_Policy_Accident = numeric_fraud_df.Days_Policy_Accident.map(DAYS_POLICY_BINS)
    numeric_fraud_df.Days_Policy_Claim = numeric_fraud_df.Days_Policy_Claim.map(DAYS_POLICY_BINS)
    numeric_fraud_df.PastNumberOfClaims = numeric_fraud_df.PastNumberOfClaims.map(PAST_NUMBER_BINS)
    numeric_fraud_df.AgeOfVehicle = numeric_fraud_df.AgeOfVehicle.map(AGE_OF_VEHICLE_BINS)
    numeric_fraud_df.AgeOfPolicyHolder = numeric_fraud_df.AgeOfPolicyHolder.map(AGE_OF_POLICY_HOLDER_BINS)
    numeric_fraud_df.PoliceReportFiled = numeric_fraud_df.PoliceReportFiled.apply(lambda filed: 1 if filed == "Yes" else 0)
    numeric_fraud_df.WitnessPresent = numeric_fraud_df.WitnessPresent.apply(lambda present: 1 if present == "Yes" else 0)
    numeric_fraud_df.AgentType = numeric_fraud_df.AgentType.apply(lambda a_type: 1 if a_type == "External" else 0)
    numeric_fraud_df.AddressChange_Claim = numeric_fraud_df.AddressChange_Claim.map(ADDRESS_CHANGE_BINS)
    numeric_fraud_df.NumberOfCars = numeric_fraud_df.NumberOfCars.map(NUMBER_OF_CARS_BINS)
    numeric_fraud_df.NumberOfSuppliments = numeric_fraud_df.NumberOfSuppliments.map(NUMBER_OF_SUPPLIMENTS)
    # return numeric_fraud_df.drop("Unnamed: 0", axis=1)
    return pd.get_dummies(numeric_fraud_df).drop("Unnamed: 0", axis=1)
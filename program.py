import csv
import pandas as pd

category = "restaurantsdining" # UPDATE
keywordList = []

def get_key_list():
    global keywordList

    with open("./KEYWORDLIST.txt") as file: # UPDATE
        keywordList = file.readlines()
    print(f"keywordList={keywordList}")
    return keywordList

def labelCategory(row):
    if row.Credit > 0: # UPDATE
        return None

    label = str(row.Label_Category_Annotated) 
    if label == 'nan':
        label = ""

    for keyword in keywordList:
        if keyword in row.RawDescription:
            if label == "":
                return category
            elif label == category:
                return category
            else:
                return (label + "|" + category)

    return None

def main():
    
    keywordList = get_key_list()

    # READ CSV, LABEL
    df = pd.read_csv("./CSVNAMEHERE.csv") # UPDATE

    # CATEGORIZATION
    df['Label_Category_Annotated'] = df.apply( lambda row: labelCategory(row) , axis =1)

    # SORTING AND PACKAGING
    df.sort_values(['RawDescription', 'Credit', 'Debit'], ascending=[True, True, True], inplace=True)
    df.to_csv('CSVNAMEHERE.csv', index=False) # UPDATE

if __name__ == '__main__':
    main()
import csv
import pandas as pd

# SETUP
# SORT CSV BY DEPOSIT (LOW TO HIGH) THEN TRANSACTION (A TO Z)
# CTRL + SHIFT + Q FOR UPPERCASE
# REMEMBER TO DELETE CREDITS
category = "restaurants" # CHANGE CATEGORY LABEL

def labelCategory(x):
    with open("./restaurants.txt") as file: # CHANGE TXT FILE
        keywordList = file.readlines()
        for keyword in keywordList:
            if keyword in x:
                return category

    return None

def main():
    # READ CSV, LABEL
    df = pd.read_csv("./0a0a.csv")

    # TREAT FILLED WITH SAME LABEL AS EMPTY
    # df4 = df[df['Label_Category_Annotated']==category]
    dfe = df[(df['Label_Category_Annotated'].isna()) | (df['Label_Category_Annotated']==category)]  # EMPTY or FILLED WITH SAME
    dff = df[df['Label_Category_Annotated'].notna()] # FILLED and not FILLED WITH SAME & df['Label_Category_Annotated']!=category
    print('dfe')
    print(dfe['Label_Category_Annotated'].head(96))
    print('dff')
    print(dff['Label_Category_Annotated'].head(5))
    

    # CATEGORIZATION
    dfe['Label_Category_Annotated'] = dfe['RawDescription'].apply( lambda x: labelCategory(x) )
    dff['Comments'] = dff['RawDescription'].apply( lambda x: labelCategory(x) )

    # PACKAGING
    df3 = pd.concat([dfe, dff])
    df3.to_csv('Zeroa0a.csv', index=False)

if __name__ == '__main__':
    main()
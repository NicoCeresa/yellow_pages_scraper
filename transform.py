import pandas as pd
import ast


class Transform:

    def safe_literal_eval(s):
        try:
            return ast.literal_eval(s)
        except (ValueError, SyntaxError):
            return {"rating":None,"count":None}

    def transform(csv_file):

        df = pd.read_csv(csv_file)

        for column in df.columns:
            df[column] = df[column].apply(ast.literal_eval).str[0]

        df.pipe(lambda d: d.assign(
            ratings = d.ratings.apply(Transform.safe_literal_eval),
            stars = d.ratings.str['rating'],
            num_reviews = d.ratings.str['count'],
            years_open = d.years_open.fillna(0).astype(int),
        ))

        # df['ratings'] = df['ratings'].apply(Transform.safe_literal_eval)
        # df['stars'] = df['ratings'].str["rating"]
        # df['num_reviews'] = df['ratings'].str["count"]
        # df['years_open'] = df['years_open'].fillna(0).astype(int)
        df['stars'] = df['stars'].fillna(0.0).replace("",0.0).astype(float)
        df['num_reviews'] = df['num_reviews'].fillna(0).replace("",0).astype(int)
        
        df.to_csv('cleaned.csv')
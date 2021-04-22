from salesapp.models import Sale
import pandas as pd

df = pd.read_csv('C:\\Users\\nsush\\Desktop\\sales_data.csv', sep='delimiter')
sales = []

for i in range(len(df)):
    sales.append(
        Sale(
            invoice_id=df.iloc[i][0],
            branch=df.iloc[i][1],
            city=df.iloc[i][2],
            customer_type=df.iloc[i][3],
            gender=df.iloc[i][4],
            product_line=df.iloc[i][5],
            unit_price=df.iloc[i][6],
            quantity=df.iloc[i][7],
            tax=df.iloc[i][8],
            total=df.iloc[i][9],
            date=df.iloc[i][10],
            payment_method=df.iloc[i][11],
            cogs=df.iloc[i][12],
            gross_income=df.iloc[i][13],
            rating=df.iloc[i][14]

        )
    )
Sale.objects.bulk_create(sales)

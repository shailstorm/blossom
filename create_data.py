import pandas as pd

# load CSV file into a pandas dataframe
df = pd.read_csv('orders_data.csv')

# create empty list to store results
results = []

# groupby creates separate groups/sub-dataframes where each group contains rows w same 'order_id'
# ['product_id']: after grouping by 'order_id', selects 'product_id' column within each group. gives Series containing all 'product_id' values for each group
# .apply(list) applies python list function to each Series of 'product_id' values within the groups
# .reset_index() resets index of the resulting DataFrame, ensuring that 'order_id' values are preserved as a regular column in the DataFrame.
# this line effectively creates 2 columns of order_id and product_id (list of product_id's belonging to that order_id)
grouped = df.groupby('order_id')['product_id'].apply(set).reset_index()

# collect all order_ids into a list
order_ids = grouped['order_id'].tolist()

# iterate through unique pairs of order_ids
for i in range(len(order_ids)):
    for j in range(i + 1, len(order_ids)):
        order1 = order_ids[i]
        order2 = order_ids[j]

        # get sets of product_ids for the two orders
        products1 = grouped.loc[grouped['order_id'] == order1, 'product_id'].values[0]
        products2 = grouped.loc[grouped['order_id'] == order2, 'product_id'].values[0]
        
        # calculate the number of shared products by taking the intersection of sets
        totalshared = len(products1.intersection(products2))
        # append the result to the results list
        if totalshared > 0:
            results.append({'order1': order1, 'order2': order2, 'totalshared': totalshared})

# create a dataframe from the results list
results_df = pd.DataFrame(results)

# save results to an output CSV file
results_df.to_csv('data.csv', index=False)

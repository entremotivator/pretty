import streamlit as st
import pandas as pd
from datetime import datetime

# Sample data for demonstration
sample_data = {
    'Item': ['Apple', 'Banana', 'Orange', 'Mango'],
    'Quantity': [100, 50, 75, 30],
    'Price': [1.99, 0.99, 1.49, 2.49],
    'Category': ['Fruit', 'Fruit', 'Fruit', 'Fruit'],
    'Last Updated': [datetime(2022, 5, 1), datetime(2022, 4, 15), datetime(2022, 4, 20), datetime(2022, 4, 25)]
}

# Create a DataFrame from the sample data
df = pd.DataFrame(sample_data)

# Page title and subtitle
st.title('Restaurant Inventory Management')
st.subheader('Manage your restaurant inventory efficiently')

# Sidebar for navigation
menu_options = ['Home', 'View Inventory', 'Add Item', 'Edit Item', 'Delete Item', 'Low Stock Items', 'Total Inventory Value']
choice = st.sidebar.selectbox('Menu', menu_options)

# Home page
if choice == 'Home':
    st.write('Welcome to the Restaurant Inventory Management App!')
    st.write('Use the sidebar to navigate different sections.')

# View Inventory page
elif choice == 'View Inventory':
    st.subheader('Current Inventory')
    st.dataframe(df)

# Add Item page
elif choice == 'Add Item':
    st.subheader('Add New Item')
    item_name = st.text_input('Item Name')
    item_quantity = st.number_input('Quantity', min_value=0)
    item_price = st.number_input('Price', min_value=0.01)
    item_category = st.selectbox('Category', ['Fruit', 'Vegetable', 'Meat', 'Beverage'])

    if st.button('Add Item'):
        new_item = {'Item': item_name, 'Quantity': item_quantity, 'Price': item_price, 'Category': item_category, 'Last Updated': datetime.now()}
        df = df.append(new_item, ignore_index=True)
        st.success('Item added successfully!')

# Edit Item page
elif choice == 'Edit Item':
    st.subheader('Edit Item')
    edit_item = st.selectbox('Select Item to Edit', df['Item'])
    edit_quantity = st.number_input('Quantity', min_value=0)
    edit_price = st.number_input('Price', min_value=0.01)
    edit_category = st.selectbox('Category', ['Fruit', 'Vegetable', 'Meat', 'Beverage'])

    if st.button('Edit Item'):
        df.loc[df['Item'] == edit_item, ['Quantity', 'Price', 'Category', 'Last Updated']] = [edit_quantity, edit_price, edit_category, datetime.now()]
        st.success('Item edited successfully!')

# Delete Item page
elif choice == 'Delete Item':
    st.subheader('Delete Item')
    delete_item = st.selectbox('Select Item to Delete', df['Item'])

    if st.button('Delete Item'):
        df = df[df['Item'] != delete_item]
        st.success('Item deleted successfully!')

# Low Stock Items page
elif choice == 'Low Stock Items':
    low_stock_threshold = st.slider('Set Low Stock Threshold', min_value=0, max_value=100, value=10)
    low_stock_items = df[df['Quantity'] <= low_stock_threshold]
    if not low_stock_items.empty:
        st.subheader('Low Stock Items')
        st.dataframe(low_stock_items)
    else:
        st.info('No low stock items.')

# Total Inventory Value page
elif choice == 'Total Inventory Value':
    total_value = (df['Quantity'] * df['Price']).sum()
    st.subheader('Total Inventory Value')
    st.write(f'${total_value:.2f}')

# Update the DataFrame in the app state
st.write('Updated Inventory')
st.dataframe(df, edit=True)


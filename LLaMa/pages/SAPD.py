from db import df
import streamlit as st
import pandas as pd 

print(df.head())


df.to_csv('feedback.csv', index=False)





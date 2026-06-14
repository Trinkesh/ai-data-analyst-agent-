import pandas as pd 


def get_dataset_summary(df):

    summary  = {
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Column Names": list(df.columns),
        "Data Types": df.dtypes.astype(str).to_dict(),
        "Missing Values": df.isnull().sum().to_dict()
    }

    return summary


def detect_chart_request(question):

    question = question.lower()

    chart_words = [
        "chart",
        "graph",
        "plot",
        "visualize",
        "show"
    ]

    return any(word in question for word in chart_words)

def get_top_customer(df):
    result  = (
        df.groupby("customer")["sales"].sum().sort_values(ascending=False).head(1)
    )
    return result
    
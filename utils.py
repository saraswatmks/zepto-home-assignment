def build_recency_count(df: pd.DataFrame):
    max_date = df['purchase_date'].max()
    recency = df.groupby('user_id')['purchase_date'].max()
    recency = (max_date - recency).dt.days.reset_index().rename(columns={'purchase_date':'recency'})
    return recency

def build_frequency_count(df: pd.DataFrame):
    freq = df.copy()
    freq = freq.groupby('user_id')['purchase_date'].nunique().reset_index().rename(columns={'purchase_date' : 'frequency'})
    return freq

def build_monetary_value(df: pd.DataFrame):
    val=df.groupby('user_id')['purchase_value'].mean().reset_index().rename(columns={'purchase_value' : 'value'})
    return val

def build_age_count(df: pd.DataFrame):
    max_date = df['purchase_date'].max()
    age = df.groupby('user_id')['purchase_date'].min()
    age = (max_date - age).dt.days.reset_index().rename(columns={'purchase_date':'age'})
    return age
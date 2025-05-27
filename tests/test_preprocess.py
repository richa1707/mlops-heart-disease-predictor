import pandas as pd

def test_preprocessed_data():
    df = pd.read_csv('data/heart_clean.csv')
    assert not df.isnull().values.any(), "❌ Missing values found"
    assert 'target' in df.columns, "❌ 'target' column missing"
    assert df.shape[1] >= 10, "❌ Less than expected number of columns"

if __name__ == "__main__":
    test_preprocessed_data()
    print("✅ test_preprocessed_data passed.")


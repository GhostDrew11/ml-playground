"""
Utility functions for ML playground
"""


def hello_ml():
    """Simple function to test package imports"""
    print("Hello from ML Playground package! Tying these stuffs for the first time.")
    return "Package working correctly, hiyeee uh oh ah!"


def create_sample_data(n_samples=100, n_features=2):
    """Create sample classification data for testing"""
    import pandas as pd
    from sklearn.datasets import make_classification

    X, y = make_classification(
        n_samples=n_samples, n_features=n_features, n_redundant=0, random_state=42
    )

    df = pd.DataFrame(X, columns=[f"feature_{i+1}" for i in range(n_features)])
    df["target"] = y

    print(f"✅ Created dataset with {n_samples} samples and {n_features} features")
    return df


# More ML utility functions will go here later

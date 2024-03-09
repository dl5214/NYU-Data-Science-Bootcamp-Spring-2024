# 3) How to get the rows of a dataframe with row sum > 100?
# df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))

import pandas as pd
import numpy as np


def main():
    df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
    print("====== Original df ======")
    print(df)
    dest_rows = df[df.sum(axis=1) > 100]
    print("====== df with rows having row sum > 100 ======")
    print(dest_rows)


if __name__ == '__main__':
    main()
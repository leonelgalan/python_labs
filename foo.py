# %%
import numpy as np
import pandas as pd

ROWS = 100

data = pd.DataFrame({
    'outcome': np.random.randint(0, 2, ROWS),
    'foo': np.random.choice(list('ABC'), ROWS),
    'bar': np.random.choice(list('DEF'), ROWS),
})

data

# %%

df = data.groupby(['foo', 'bar'], as_index=False).agg({
    'outcome': ['count', 'mean', 'std']
})
df.columns = ['_'.join(filter(None, t)) for t in df.columns]
df

# %%

df = pd.pivot_table(data,
                    index=['foo', 'bar'],
                    values='outcome',
                    aggfunc=[np.mean, np.size, np.std])
df.columns = ['_'.join(filter(None, t)) for t in df.columns]
df

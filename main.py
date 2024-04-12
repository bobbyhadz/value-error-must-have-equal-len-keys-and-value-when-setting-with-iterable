# Must have equal len keys and value when setting with iterable

import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bobby', 'Carl', 'Dan'],
    'experience': [11, 14, 16, 18],
    'salary': [175.1, 180.2, 190.3, 210.4],
})

df['coords'] = ''

df['coords'] = df['coords'].apply(lambda x: ['X', 'Y'])

print(df)
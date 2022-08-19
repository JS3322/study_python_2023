import numpy as np
import pandas as pd

def export_csv():
    # import numpy as np
    area = ['번호', '이름', '1-1-2', '1-3-0', '2-1-3']
    input = [1, '김준석', 5, 4, 3]

    df = pd.DataFrame(area, row=['area'])
    df['input'] = input

    df.to_csv("source/output.csv", index = False)

    print(df)

    # list1 = [1,2,3,4]
    # a = np.array(list1)
    # print(a.shape)
    #
    # print("hello world")
for first in "XYZ":
    for second in "XYZ":
        if second != first:
            for third in "xyz":
                if third != first and third!= second:
                    print(first+second+third)
"""
    演示了finally
"""
try:
    res = 10 / 0
# except ZeroDivisionError as e:
except NameError as e:
    print(e)
else:
    print(res)
finally:
    print("finally")

print("end")
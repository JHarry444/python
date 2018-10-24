import os
try:
    # os.makedirs("C:/")
    raise NameError("Message")
except (PermissionError, NameError) as error:
    print("Error: ", error)
except:
    print("Unexpected error when creating directories.")
else:
    print("Directory successfully created!")
finally:
    print("This code always runs.")

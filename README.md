# ISS_LocationAndNotification

Features:
Checking if the ISS is close to your location.
Checking if the time is night, which is after sunset or before sunrise.
Sending email as a notification when ISS comes right above you.


## Installation:

Use the below packages:

```python
import time
import smtplib
import requests
from datetime import datetime
```

## API Usage:

1. http://api.open-notify.org/iss-now.json  ( Check latitude and longitude of ISS )
2. https://api.sunrise-sunset.org/json  ( Check the sunrise and sunset time at a position)

## References: 

[UDEMY: 100 DAYS OF PYTHON](https://www.udemy.com/course/100-days-of-code/learn/lecture/21232758#questions)

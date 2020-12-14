import pandas as pd
import numpy
import random
import datetime
from random import randrange
from datetime import datetime
from datetime import timedelta
from datetime import timezone


def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

start_date = datetime.strptime('1/1/2019 12:00 AM', '%m/%d/%Y %I:%M %p')
end_date = datetime.strptime('1/1/2020 12:00 AM', '%m/%d/%Y %I:%M %p')


status_type = {
	#Type: Weight of Occuring
	'COMPLETED': 7,
	'CANCELLED': 3
}

supply_data_normal = random.sample(range(9001,9800),40)
supply_data_outlier = random.sample(range(9801,9999),10)


columns = [ 'order_id', 'time_stamp', 'supply_id', 'status'] 


df = pd.DataFrame(columns = columns)

#For normal weighted case
for i in range(1,4501):
	status_list = [status for status in status_type]
	status_weights = [status_type[status] for status in status_type]
	status = random.choices(status_list, weights = status_weights)[0]
	supply_id = random.choice(supply_data_normal)
	date_time = random_date(start_date, end_date)
	utc_timestamp = date_time.replace(tzinfo=timezone.utc).timestamp()	
	df.loc[i] = [1000+i, utc_timestamp, supply_id, status]


#For inverse weighting to get outlier cases
for i in range(4501,5501):
	status_list = [status for status in status_type]
	status_weights = [10-status_type[status] for status in status_type]
	status = random.choices(status_list, weights = status_weights)[0]
	supply_id = random.choice(supply_data_outlier)
	date_time = random_date(start_date, end_date)
	utc_timestamp = date_time.replace(tzinfo=timezone.utc).timestamp()	
	df.loc[i] = [1000+i, utc_timestamp, supply_id, status]

#CSV Generation
df.to_csv('demo.csv',index=False)
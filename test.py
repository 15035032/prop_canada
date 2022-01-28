from unittest import result
from fastapi import FastAPI
from numpy import average
import pymongo
import datetime
from typing import List



myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["local"]
mycol = mydb["NewData"]




app = FastAPI()


now = datetime.datetime.now() - datetime.timedelta(days=180)
date_time = now.strftime("%Y-%m-%d %H:%M:%S")


@app.get('/root')
async def root():
    return {"Hello!"": World"}



@app.get('/prop/{result}') 
async def prop():  
          agg_result= mycol.aggregate([{"$match": { "Status.Status": "U", 
                             'updated_timestamp': {"$gte" : date_time}}
                            },
                        { "$group": {
                           "_id": {
                           "year": { "$substr": [ "$updated_timestamp", 0, 4 ] },
                           "month": { "$substr": [ "$updated_timestamp", 5, 2 ]}
                            },
                       "Average":{"$avg":"$price.Lp_dol"},
                       "count": { "$sum": 1 }
                           }}
                         ])

          
          x=[]
          for i in agg_result:
              x.append(i)
          return x
          
         
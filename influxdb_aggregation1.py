import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import dotenv

dotenv.load_dotenv()
token = os.environ.get("INFLUXDB_TOKEN")
org = "test influxb for energy networks"
url = "http://localhost:8086"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

query_api = client.query_api()

query = """from(bucket: "fskldfklsf")
  |> range(start: -10m)
  |> filter(fn: (r) => r._measurement == "measurement1")
  |> mean()"""
tables = query_api.query(query, org="test influxb for energy networks")

for table in tables:
    for record in table.records:
        print(record)

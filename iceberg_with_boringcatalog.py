from boringcatalog import BoringCatalog

catalog = BoringCatalog(name="boring", uri="warehouse/catalog/catalog_boring.json")

import pyarrow.parquet as pq
df = pq.read_table("data/yellow_tripdata_2023-01.parquet")
table = catalog.load_table(("ice_default", "yellow_tripdata_tbl"))
table.append(df)
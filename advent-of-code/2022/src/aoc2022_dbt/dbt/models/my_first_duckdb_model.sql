select col1, sum(cast(col1 is null as SMALLINT)) over (
    PARTITION BY col1
    -- ORDER BY
    -- ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ROWS BETWEEN 1 PRECEDING AND CURRENT ROW
  ) as col2
from {{ ref('day_01_example_input') }}

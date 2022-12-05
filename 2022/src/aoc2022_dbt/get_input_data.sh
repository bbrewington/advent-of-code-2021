git_repo_top_lvl=$(git rev-parse --show-toplevel)
aoc2022_dbt_seed_dirpath="${git_repo_top_lvl}/2022/src/aoc2022_dbt/dbt/seeds"

echo 'col1' > ${aoc2022_dbt_seed_dirpath}/day_01_example_input.csv
cat 2022/docs/day_01/example_input.txt >> ${aoc2022_dbt_seed_dirpath}/day_01_example_input.csv

library(readr)
library(purrr)
library(testthat)
library(here)

here::i_am("src/aoc2022_R")

day_01 <- function(file_dirpath, filename) {
  file_path <- paste0(file_dirpath, "/", filename)
  x <- as.integer(readr::read_lines(file_path))
  group_labels <- cumsum(is.na(x))
  x_split <- split(x, group_labels)
  return_val <- max(purrr::map_int(x_split, ~sum(., na.rm = TRUE)))
  return(return_val)
}

testthat::test_that("day_01 example tests pass", {
  testthat::expect_equal(
    day_01("https://raw.githubusercontent.com/bbrewington/advent-of-code/main/2022/docs/day_01",
           "example_input.txt"),
    24000
  )
})

day_01("https://raw.githubusercontent.com/bbrewington/advent-of-code/main/2022/docs/day_01",
       "input.txt")

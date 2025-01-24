# Keeping code below in case need to extend/wrap above test_that call
# Currently, can just run the tests as a test suite done in sequence

# tester <- function(input_function, expected_value, test_description, ...) {
#   testthat::test_that(
#     test_description,
#     {
#       testthat::expect_equal(input_function(...), expected_value)
#     }
#   )
# }

# # This acts as a unit test...script will fail here if anything changes in tester
# tester(input_function = day_01, expected_value = 24001, 
#        test_description = "example_input.txt", 
#        "../../docs", "/day_01", "example_input.txt")
# 
# try_input_file <- function(FUN, ...) {
#   out <- tryCatch({
#       tester(FUN, ...)
#     },
#     error = function(cond) {
#       message(paste("failed"))
#     }
#   )  
#   return(out)
# }
# 
# try_input_file(FUN = day_01, expected_value = 24001, 
#                test_description = "example_input.txt", 
#                "../../docs", "/day_01", "example_input.txt")
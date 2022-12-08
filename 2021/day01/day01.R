########################################
################ Part 1 ################
########################################

sample_sweep <- c(199, 200, 208, 210, 200,
                  207, 240, 269, 260, 263)

input <- as.integer(readLines("input.txt"))

count_deeper_measurements <- function(x) {
  len <- length(x)
  return(sum((x[2:len] - x[1:(len-1)]) > 0))
}

count_deeper_measurements(input)
# [1] 1184

########################################
################ Part 2 ################
########################################

# each 3-measure sum shares two values. So to
# compare the sums, need only compare the head
# of the first and the tail of the second.
count_deeper_3meassum <- function(x) {
  len <- length(x)
  return(sum((x[4:len] - x[1:(len-3)]) > 0))
}

count_deeper_3meassum(input)
# [1] 1158